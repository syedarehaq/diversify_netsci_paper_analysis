# %%
import matplotlib
#matplotlib.font_manager._rebuild()
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib import rcParams
import matplotlib.pyplot as plt
import matplotlib.font_manager as font_manager

import numpy as np
import datetime
# %%
plot_code = "06_01_02"
#start_year_type = "whole_mag"
start_year_type = "gt_1997"
# %%
## Working with the fonts
fontpath = '/Users/arefindk/Library/Fonts/MyriadPro-Regular.ttf'
#fontpath = "/System/Library/Fonts/HelveticaNeue.ttc"
prop = font_manager.FontProperties(fname = fontpath)
plt.rcParams['font.family'] = prop.get_name()
# %%
#fig, ax = plt.subplots()
#ax.set_title('Text in a cool font', size=40)
#plt.show()
# %%
title_fontsize = 17
label_fontsize = 15
legend_fontsize = 14
# %%
if start_year_type == "whole_mag":
    df = pd.read_csv("../data/bigquery/mag_syed_netsci_filtered_authors_20191025/selected_authors_gender_proportion.csv")
    #df = df[df["country"] != "None"]
elif start_year_type == "gt_1997":
    df = pd.read_csv("../data/bigquery/mag_syed_netsci_filtered_authors_20191025/selected_authors_gender_proportion_gt_1997.csv")
    #df = df[df["country"] != "None"]
# %%
def func(pct, allvals):
    absolute = int(pct/100.*np.sum(allvals))
    #return "{:.1f}% ({:d} )".format(pct, absolute)
    return "{:.1f} %".format(pct)
# %%
color_dict = {'male': '#e64550', 'female': '#1f97ce'}
# %%
fig,axarr = plt.subplots(1,3,figsize = (16,5))
sub_titles = ["A) Gender Composition of Authors", "B) Papers by Author Gender", "C) Citations by Author Gender"]
for i,count_type in enumerate(["count", "paper_count", "author_citation_count"]):
    ax = axarr[i]
    genders, count = df["gender"].values, df[count_type].values
    colors = [color_dict[g] for g in genders]
    prob = np.array(count) / sum(count)
    
    #Create our plot and resize it.
    explode = [0,0.05]
    
    # borrowing from the following
    # https://www.machinelearningplus.com/plots/top-50-matplotlib-visualizations-the-master-plots-python/
    wedges, texts, autotexts = ax.pie(count, 
                                  autopct=lambda pct: func(pct, count),
                                  textprops=dict(color="w",size=20), 
                                  colors=colors,
                                 startangle=40,
                                 explode=explode)
    
    # Decoration
    if i == 2:
        ax.legend(wedges, [x.capitalize() for x in genders], loc="center left", bbox_to_anchor=(0.90, 0, 0.25, 1), fontsize = legend_fontsize+2)
    ax.set_title('%s' %sub_titles[i], y=0, x=0.5, fontsize = title_fontsize)
    #ax.set_title("A", loc = "bottom left")
    
    #Remove our axes and display the plot
    ax.axis('off')

#plt.title("Gender (by %s)" %count_type,fontsize=23,fontweight="bold")
now = datetime.datetime.now().strftime("%Y%m%d")
savefig_dir = "../figures_v3/"
fig.tight_layout()
plt.savefig(savefig_dir+"%s_gender_pie_charts_%s_%s_%s.png" %(plot_code,count_type,start_year_type,now), dpi = 300)
plt.show()


# %%
fig,axarr = plt.subplots(1,2,figsize = (8,5))
subtitle_alphabets = ["A", "B"]
subtitles = {"paper_count_per_head":"Paper Count Per Author",
             "author_citation_count_per_capita":"Citation Count Per Author",
             }
for i,data_type in enumerate(["paper_count_per_head","author_citation_count_per_capita"]):
    ax = axarr[i]
    genders = df["gender"].values
    genders = [x.capitalize() for x in genders]
    data = list(df[data_type].values)
    x_pos = np.arange(len(genders))
    new_x = [0.5*i for i in x_pos]

    
    ax.bar(new_x, data, align='center', alpha=1, color = colors, width = 0.3)
    ax.set_xticks(new_x)
    ax.set_xticklabels(genders, fontsize = label_fontsize)
    ax.tick_params(axis='y', which='major', labelsize=label_fontsize-1)
    #ax.axis('off')
    ax.set_title('%s) %s' %(subtitle_alphabets[i],subtitles[data_type]), y=-0.2, x=0.5, fontsize = title_fontsize)

now = datetime.datetime.now().strftime("%Y%m%d")
savefig_dir = "../figures_v3/"
fig.tight_layout()
plt.savefig(savefig_dir+"%s_gender_per_capita_paper_and_citation_%s_%s_%s.png" %(plot_code,count_type,start_year_type,now), dpi = 300)
plt.show()
