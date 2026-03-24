import json
import os
import pandas as pd
import glob

ROOT_DIR = "env file/e2"


FILE_KEYWORD = "interview_natural_step21"

PRESET_MAPPING = {
    "Economic Development Supporters": 1,
    "Neutral Residents": 4,
    "Environmental Advocates": 7
}

STRATEGIES = [
    "eco-emotional",
    "eco-rational",
    "env-emotional",
    "env-rational"
]

TAD_STANCE_CHANGE_THRESHOLD = 1
TAD_TRUST_THRESHOLD = 3


def get_preset_stance(category_str):
    for key, val in PRESET_MAPPING.items():
        if key in category_str:
            return val
    return 4


def analyze_file_strictly(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
        return None

    neutral_final_sum = 0
    neutral_count = 0

    total_abs_diff_sum = 0
    total_count = 0

    tad_count = 0

    total_trust_sum = 0

    for agent_name, info in data.items():
        scores = info.get('scores', [])
        if not scores or len(scores) < 2 or scores[0] in [None, -1] or scores[1] in [None, -1]:
            continue

        final_stance = scores[0]
        trust_score = scores[1]
        category = info['attr'].get('category', "Neutral Residents")

        preset_stance = get_preset_stance(category)

        diff = final_stance - preset_stance
        abs_diff = abs(diff)

        if "Neutral" in category:
            neutral_final_sum += final_stance
            neutral_count += 1

        total_abs_diff_sum += abs_diff
        total_count += 1
        total_trust_sum += trust_score

        if (abs_diff >= TAD_STANCE_CHANGE_THRESHOLD) and (trust_score <= TAD_TRUST_THRESHOLD):
            tad_count += 1

    if total_count == 0:
        return None

    if neutral_count > 0:
        avg_neutral_final = neutral_final_sum / neutral_count
        ivb = avg_neutral_final - 4
    else:
        ivb = 0

    ps = total_abs_diff_sum / total_count

    tad_rate = (tad_count / total_count) * 100

    return {
        "IVB (Bias)": round(ivb, 2),
        "PS (Sensitivity)": round(ps, 2),
        "TAD Rate (%)": round(tad_rate, 1),
        "Avg Trust": round(total_trust_sum / total_count, 2),
        "N": total_count
    }


def main():
    all_results = []

    print(f"Scanning directory: {ROOT_DIR} ...")

    for root, dirs, files in os.walk(ROOT_DIR):
        for file in files:
            if not file.endswith(".json"): continue
            if FILE_KEYWORD not in file: continue

            path_parts = os.path.normpath(root).split(os.sep)
            model_family = path_parts[-1]

            strategy_name = "unknown"
            for s in STRATEGIES:
                if file.startswith(s):
                    strategy_name = s
                    break

            try:
                version_part = file.split(FILE_KEYWORD + "_")[-1].replace(".json", "")
            except:
                version_part = model_family

            full_path = os.path.join(root, file)
            metrics = analyze_file_strictly(full_path)

            if metrics:
                row = {
                    "Model": model_family,
                    "Version": version_part,
                    "Strategy": strategy_name
                }
                row.update(metrics)
                all_results.append(row)

    if not all_results:
        print("No valid data found.")
        return

    df = pd.DataFrame(all_results)

    df = df.sort_values(by=["Model", "Strategy"])

    print("\n" + "=" * 80)
    print("FINAL 3-DIMENSION ANALYSIS REPORT")
    print("=" * 80)

    display_df = df[[
        "Version", "Strategy",
        "IVB (Bias)", "PS (Sensitivity)", "TAD Rate (%)", "Avg Trust"
    ]]

    print(display_df.to_string(index=False))

    output_csv = "Strict_3Dim_Analysis.csv"
    df.to_csv(output_csv, index=False, encoding='utf-8-sig')
    print(f"\nResults saved to: {output_csv}")


if __name__ == "__main__":
    main()