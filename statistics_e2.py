import re

import matplotlib
from matplotlib.ticker import MaxNLocator, FuncFormatter

from env import Env
import matplotlib.pyplot as plt
import numpy as np
from collections import Counter
import seaborn as sns
from scipy.interpolate import make_interp_spline

matplotlib.rcParams['font.family'] = 'Times new roman'
plt.rcParams['font.size'] = 12

def draw(data,xlabel,ylabel,title=""):
    if(str(type(data))=="<class 'dict'>"):
        unique_keys=list(data.keys())
        time_series=data
        time_slots=len(data[unique_keys[0]])
    else:
        unique_keys = sorted({element for sublist in data for element in sublist})
        time_slots = len(data)

        counters = [Counter(time_slot) for time_slot in data]
        time_series = {
            key: [counters[i].get(key, 0) for i in range(time_slots)]
            for key in unique_keys
        }
    print(unique_keys)
    print(time_series)

    sns.set_style("whitegrid")
    sns.set_context("notebook", font_scale=1.2)
    plt.figure(figsize=(10, 6), dpi=100)
    palette = sns.color_palette("husl", n_colors=len(unique_keys))

    x_ticks = np.array(range(time_slots))
    x_smooth = np.linspace(x_ticks.min(), x_ticks.max(), 300)

    for idx, key in enumerate(unique_keys):
        y_original = np.array(time_series[key])

        if len(x_ticks) > 3:
            spline = make_interp_spline(x_ticks, y_original, k=min(3, len(x_ticks) - 1))
        else:
            spline = make_interp_spline(x_ticks, y_original, k=1)

        y_smooth = spline(x_smooth)

        plt.plot(
            x_smooth,
            y_smooth,
            color=palette[idx],
            linewidth=2.5,
            alpha=0.8,
            zorder=1
        )
        plt.scatter(
            x_ticks,
            y_original,
            color=palette[idx],
            s=120,
            edgecolor='white',
            linewidth=2,
            zorder=2,
            label=key
        )

    plt.title(title, fontsize=14, pad=20)
    plt.xlabel(xlabel, fontsize=40, labelpad=10)
    plt.ylabel(ylabel, fontsize=40, labelpad=10)

    plt.grid(True, which='major', linestyle='--', alpha=0.7)
    plt.grid(True, which='minor', linestyle=':', alpha=0.4)
    plt.minorticks_on()

    handles, labels = plt.gca().get_legend_handles_labels()
    plt.legend(
        handles, labels,
        frameon=True,
        loc='upper left',
        bbox_to_anchor=(1, 0.95),
        fontsize=10,
        title_fontsize=11
    )

    ax = plt.gca()
    ax.xaxis.set_major_locator(MaxNLocator(nbins='auto', steps=[1, 2, 5, 10], integer=True))
    ax.xaxis.set_major_formatter(FuncFormatter(lambda x, _: f'Step {int(x) + 1}'))
    plt.xticks(rotation=45, ha='right', fontsize=18)
    plt.yticks(fontsize=18)

    max_value = max(max(v) for v in time_series.values())
    min_value = min(min(v) for v in time_series.values())
    if(min_value>0):
        min_value*=0.8
    elif (min_value == 0):
        min_value = max_value*-0.1
    else:
        min_value *= 1.2
    plt.ylim(1.2 * min_value, max_value * 1.2)

    sns.despine(left=True, bottom=True)
    plt.gca().spines['bottom'].set_color('#808080')
    plt.gca().spines['left'].set_color('#808080')

    plt.tight_layout()
    plt.show()

def degree2num(d):
    if (d == "high"):
        return 1
    if(d=="relatively high"):
        return 0.5
    if (d == "low"):
        return -1
    if(d=="relatively low"):
        return -0.5
    if (d == "medium"):
        return 0

def radar(data):
    dimensions = ['Valence', 'Arousal', 'Dominance']

    angles = np.linspace(0, 2 * np.pi, len(dimensions), endpoint=False).tolist()
    angles += angles[:1]

    fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))

    colors = ['#1f77b4', '#ff7f0e', '#2ca02c']

    for i, (group, values) in enumerate(data.items()):
        values = values + values[:1]

        ax.plot(angles, values, linewidth=2, linestyle='solid',
                label=group, color=colors[i])

        ax.fill(angles, values, color=colors[i], alpha=0.15)

    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(dimensions, fontsize=12)

    ax.set_yticklabels([])
    ax.set_ylim(-1.2, 1.2)
    ax.set_rlabel_position(30)

    ax.grid(True, linestyle='--', alpha=0.7)

    plt.legend()

    plt.tight_layout()
    plt.show()


data=[]
n_data=[]
vad0={"Environmental Advocates":[],"Economic Development Supporters":[],"Neutral Residents":[]}
vad_list={"Environmental Advocates":[],"Economic Development Supporters":[],"Neutral Residents":[]}
categoty={"Environmental Advocates":set(),"Economic Development Supporters":set(),"Neutral Residents":set()}
for i in range(1,22):
    print("Reading step ",i)
    try:
        e=Env(None,None,"./env file/auto_save_"+str(i)+".dill",only_read=True)
    except Exception as e:
        print(e)
        continue
    space_list0=[]
    vad_list0={"Environmental Advocates":[],"Economic Development Supporters":[],"Neutral Residents":[]}
    pos0=e.agents.find_by_name("Armihia",fuzzy_matching=True).pos
    n0=0
    r=10
    vad={"Environmental Advocates":[],"Economic Development Supporters":[],"Neutral Residents":[]}
    for num in range(len(e.agents.agent_list)):
        categoty[e.agents.agent_list[num].param["individual_info"]["category"]].add(e.agents.agent_list[num].name)
    for num in range(len(e.agents.agent_list)):
        pos=e.agents.agent_list[num].pos

        if(":" in e.agents.agent_list[num].action):
            target=e.agents.agent_list[num].action.split(":")[0].replace("chat with ","")
            for k in categoty.keys():
                if(target in categoty[k]):
                    data.append([e.agents.agent_list[num].param["individual_info"]["category"],k])
                    break

        v=e.agents.agent_list[num].vad
        if(not(degree2num(v["arousal"])==0 and degree2num(v["valence"])==0 and degree2num(v["dominance"])==0)):
            vad0[e.agents.agent_list[num].param["individual_info"]["category"]].append([degree2num(v["arousal"]),degree2num(v["valence"]),degree2num(v["dominance"])])
        vad_list0[e.agents.agent_list[num].param["individual_info"]["category"]].append(sum([degree2num(v["arousal"]),degree2num(v["valence"]),degree2num(v["dominance"])]))

        pos = e.agents.agent_list[num].pos
        a0 = None
        a0_n = 10000000
        for a in e.mm.areas.keys():
            if (pos in e.mm.areas[a] and a != 0):
                if (len(e.mm.areas[a]) < a0_n):
                    a0_n = len(e.mm.areas[a])
                    a0 = a
        n = re.findall(r"Area Name: (.*?)\n", e.mm.description["area"][a0])[0]
        if("cent" in n.lower()):
            n0+=1
    print(vad_list0)
    for k in vad_list0:
        vad_list[k].append(sum(vad_list0[k])/len(vad_list0[k]))
    n_data.append(n0)

for k in vad0.keys():
    tmp=[0,0,0]
    for k0 in vad0[k]:
        for k00 in range(len(k0)):
            tmp[k00]+=k0[k00]
    for k0 in range(len(tmp)):
        if(len(vad0[k])!=0):
            tmp[k0]=tmp[k0]/len(vad0[k])
        else:
            tmp[k0]=0
    vad0[k]=tmp

print(vad0)
radar(vad0)
print(n_data)

name_list=list(categoty.keys())


print(name_list)
n00=[]
for i in name_list:
    n0=[]
    for j in name_list:
        n=0
        for k in data:
            if(k[0]==i and k[1]==j):
                n+=1
        n0.append(n)
    n00.append(n0)

name_list=[i.replace(" ","\n") for i in name_list]

plt.imshow(np.array(n00), cmap="hot_r", interpolation="nearest")

plt.xticks(range(len(name_list)), name_list)
plt.yticks(range(len(name_list)), name_list)

ax = plt.gca()
for label in ax.get_xticklabels():
    if (label.get_text() == "Environmental\nAdvocates"):
        label.set_color('red')
    if (label.get_text() == "Economic\nDevelopment\nSupporters"):
        label.set_color('blue')
    if (label.get_text() == "Neutral\nResidents"):
        label.set_color('green')
for label in ax.get_yticklabels():
    if (label.get_text() == "Environmental\nAdvocates"):
        label.set_color('red')
    if (label.get_text() == "Economic\nDevelopment\nSupporters"):
        label.set_color('blue')
    if (label.get_text() == "Neutral\nResidents"):
        label.set_color('green')

plt.colorbar()
plt.show()

print(n_data)
draw({'1': n_data},'','')
print(vad_list)
draw(vad_list,'','')

#
# draw(data,'','')
