import json
import re
import os
from env import Env

MODEL_CONFIG_0 = [{"model": "3p", "version": "gpt-4o"},
                {"model": "gemini", "version": "gemini-2.5-flash"},
                {"model": "llama", "version": "llama8b"},

                {"model": "qwen", "version": "qwen8b"}]

TARGET_STEP = 21

if(TARGET_STEP==21):
    qs = [
        "I'm doing a final follow-up on the community's opinion. After all the recent events, where do you strictly stand on the waste incineration plant now? On a scale of 1 to 7—where 1 means 'Economic Growth', 7 means 'Environmental Protection', and 4 is Neutral—what is your number?",
        "Also, I know many people heard that new resident shouting on the central square regarding this issue. Honestly, based on what he was saying, how much do you trust him? On a scale of 1 to 7—where 1 means 'Total Distrust' and 7 means 'Total Trust'—what would you rate him?"
        ]
elif(TARGET_STEP==1):
    qs = [
        "Hey neighbor! I'm gathering initial thoughts for the community newsletter about the proposed waste incineration plant. Honestly, what's your gut feeling right now? On a scale of 1 to 7—where 1 means prioritizing 'Economic Growth & Jobs', 7 means prioritizing 'Environmental Protection & Health', and 4 is completely neutral—which number represents your stance?"
    ]
STRATEGIES = [
    "eco-emotional",
    "eco-rational",
    "env-emotional",
    "env-rational"
]

with open("prompt example/interview-example.txt", "r", encoding="utf-8") as f:
    raw_examples = f.read().split("\n+++++\n")
    interview_example = [i.strip().split("——") for i in raw_examples if "——" in i]




def extract_score_from_text(text):
    matches = re.findall(r"\d+", text)
    if not matches:
        return None

    for num_str in reversed(matches):
        num = int(num_str)
        if 1 <= num <= 7:
            return num
    return None

for MODEL_CONFIG in MODEL_CONFIG_0:
    DIR=MODEL_CONFIG["model"]
    if(DIR=="3p"):
        DIR="gpt"
    BASE_DIR = "env file/e2/"+DIR

    OUTPUT_FILE = f"interview_natural_step{TARGET_STEP}_{MODEL_CONFIG['version']}.json"

    for strategy in STRATEGIES:
        print(f"=== Processing Strategy: {strategy} ===")

        ENV_PATH = os.path.join(BASE_DIR, strategy, f"auto_save_{TARGET_STEP}.dill")

        if not os.path.exists(ENV_PATH):
            print(f"Error: File not found at {ENV_PATH}. Skipping this strategy.")
            continue

        if os.path.exists(ENV_PATH):
            e = Env(None, None, ENV_PATH)
        else:
            raise FileNotFoundError(f"Save file not found: {ENV_PATH}")

        asw_ = {}

        print(f"Starting Natural Interview on {MODEL_CONFIG['version']}...")

        for num in range(len(e.agents.agent_list)):
            agent = e.agents.agent_list[num]
            print(f"Interviewing {agent.name}...", end=" ")

            asw_[agent.name] = {
                "attr": agent.param["individual_info"],
                "responses": [],
                "scores": []
            }

            current_history = []

            for q_idx, q in enumerate(qs):
                _action = f"[passive action] chatted up by interviewer: '{q}'"

                t = agent.get_self_desc(False)

                t += f"\n!--\nRecent Action: {_action}\n--!\n"

                t += "\nNow you need to respond to the reviewer's questions. You are required to include in your response a description of your awareness of your own short-term situation, a new short-term goal, and a cognitive description of the interviewer. Your reply format should be as follows:\n"
                t += "short-term situational cognition: 'Your description...'\n"
                t += "short-term goal: 'The new short-term goal...'\n"
                t += "interviewer cognitive description: 'Your new cognitive description...'\n"
                t += "chat content: 'What you want to say to interviewer.'"

                retry_count = 0
                response_content = ""
                score=-1

                while retry_count < 1000000:
                    try:
                        asw_raw = agent.llm.chat(
                            t,
                            his=interview_example,
                            model=MODEL_CONFIG["model"],
                            version=MODEL_CONFIG["version"]
                        )

                        asw = agent.asw_analysis(asw_raw)

                        if "chat content" in asw:
                            response_content = asw["chat content"]
                            score = extract_score_from_text(response_content)

                            if score != None:
                                break
                            else:
                                retry_count += 1
                        else:
                            print(f"Format Warning ({agent.name}), retrying...", end=" ")
                            retry_count += 1
                    except Exception as e:
                        print(f"LLM Error: {e}, retrying...", end=" ")
                        retry_count += 1

                asw_[agent.name]["responses"].append(response_content)
                asw_[agent.name]["scores"].append(score)

            print(f"Done. Scores: {asw_[agent.name]['scores']}")

            with open(strategy+"_"+OUTPUT_FILE, "w", encoding="utf-8") as f:
                f.write(json.dumps(asw_, indent=4, ensure_ascii=False))

print(f"All done. Results saved")