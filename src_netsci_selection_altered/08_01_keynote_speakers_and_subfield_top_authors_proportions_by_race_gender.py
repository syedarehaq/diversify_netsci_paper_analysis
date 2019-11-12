import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import datetime
import numpy as np
import matplotlib.font_manager as font_manager
# %%
plot_code= "08_01"
now = datetime.datetime.now().strftime("%Y%m%d")
# %%
title_fontsize = 17
label_fontsize = 15
legend_fontsize = 14
subfield_synonym = "Keywords"
# %%
## Working with the fonts
fontpath = '/Users/arefindk/Library/Fonts/MyriadPro-Regular.ttf'
#fontpath = "/System/Library/Fonts/HelveticaNeue.ttc"
prop = font_manager.FontProperties(fname = fontpath)
plt.rcParams['font.family'] = prop.get_name()
#%%
#create a custom color palette
palette21 = ['#21618C', '#3498DB', '#AED6F1', '#00838F', '#00BFA5',
             '#F1C40F', '#F9E79F', '#E67E22', '#922B21', '#C0392B', 
             '#E6B0AA', '#6A1B9A', '#8E44AD', '#D7BDE2', '#196F3D', 
             '#4CAF50', '#A9DFBF', '#4527A0', '#7986CB', '#555555', 
             '#CCCCCC']
#sns.palplot(palette21)
palette_race = sns.color_palette("Set1", n_colors=8, desat=.5)#sns.color_palette("muted")
#sns.palplot(palette_race)
color_dict = {'male': '#1f97ce', 'female': '#e64550'}
color_dict_race = {'Black/African':"#21618C", 'East Asian':"#3498DB", 'Hispanic/Latino':"#AED6F1", 'Indian Subcontinet':"#00838F",
       'Middle Eastern':"#F1C40F", 'Other':"#F9E79F", 'White/European':"#E67E22"}

## Syed suggestion
#palette_race_6 = ["#FF715B","#1f97ce", "#c994c7", "#61C9A8", "#FFE381", "#ADA8B6"]
#palette_race_7 = ["#FF715B","#1f97ce", "#c994c7", "#61C9A8", "#FFE381", "k", "#ADA8B6"]

## Dina Suggestion
palette_race_5 = ["#63388E", "#F4C724", "#15995A", "#FA8B00","#B5B5B5"]
palette_race_6 = ["#F45053","#63388E", "#F4C724", "#15995A", "#FA8B00","#B5B5B5"]
palette_race_7 = ["#F45053","#63388E", "#F4C724", "#15995A", "#FA8B00","#01618D","#B5B5B5"]
                  
palette_male_female = color_dict.values()#["#31a354", "#3182bd", "#636363"]
#palette_race = ["#2ca25f", "#ece2f0", "#43a2ca", "#dd1c77", "#e6550d", "#8856a7"]
# %%
df = pd.read_csv("../data/bigquery/mag_syed_netsci_filtered_authors_20191025/final_table_keynote_and_invited_speakers_with_gender_race.csv")

subtitles = ["A) Gender", "B) Race"]
fig,axarr = plt.subplots(1,2,figsize = (16,5))
ax = axarr[0]
df_bar = df.groupby(["gender"]).size().rename('count')
df_bar = df_bar / len(df)
df_bar = df_bar.to_frame().reset_index()
ax = df_bar.plot.bar(x="gender", y="count", ax = ax, color=palette_male_female, legend = False)
#ax1.xaxis.set_label_text('')
ax.xaxis.label.set_visible(False)
#ax.set_title("NetSci Keynote Speakers, Invited Speakers\nand Awardees for 2007-2019", fontsize = title_fontsize)
ax.set_ylim(0,1)

genders = ["Female", "Male"]
x_pos = np.arange(len(genders))


ax.set_xticks(x_pos)
ax.set_xticklabels(genders, fontsize = label_fontsize, rotation = 0)
ax.tick_params(axis='y', which='major', labelsize=label_fontsize)
ax.set_title('%s' %subtitles[0], y=1.0, x=0.5, fontsize = title_fontsize)



ax = axarr[1]
df_bar = df.groupby(["race"]).size().rename('count')
df_bar = df_bar / len(df)
df_bar = df_bar.to_frame().reset_index()
df_bar.plot.bar(x="race", y="count", ax =ax, color=palette_race_6, legend = False)
#ax1.xaxis.set_label_text('')
ax.xaxis.label.set_visible(False)

races = ["Black/African","East\nAsian", "Hispanic/\nLatinx", "South\nAsian", "Middle\nEastern", "White/\nEuropean"]
x_pos = np.arange(len(races))


ax.set_xticks(x_pos)
ax.set_xticklabels(races, fontsize = label_fontsize, rotation = 0)
ax.tick_params(axis='y', which='major', labelsize=label_fontsize)

#ax.set_title("Keynote speaker and awardees \n in NetSci conferences", fontsize = title_fontsize)
ax.set_ylim(0,1)

ax.set_title('%s' %subtitles[1], y=1.0, x=0.5, fontsize = title_fontsize)

fig.tight_layout(rect=[0, 0.03, 1, 0.95])
plt.suptitle("NetSci Keynote Speakers, Invited Speakers and Awardees for 2007-2019", fontsize = title_fontsize + 2, y=1)
plt.savefig("../figures_v3/%s_keynote_speakers_gender_race_%s.png" %(plot_code,now))
plt.show()

# %%
## Race of top 100 authors
fig,ax = plt.subplots(1,1,figsize = (10,5))
df = pd.read_csv("../data/bigquery/mag_syed_netsci_filtered_authors_20191025/final_table_top_100_authors_diff_field_with_gender_race.csv")

df_bar = df.groupby(["field_name","race"]).size().rename('count')
df_bar = df_bar / df_bar.groupby(level=0).sum()
df_bar = df_bar.to_frame().reset_index()
df_bar = df_bar.pivot("field_name","race","count").fillna(0)

flattened = pd.DataFrame(df_bar.to_records())
ax = flattened.plot(x='field_name', ax=ax, kind='barh', stacked=True, mark_right=True, color=palette_race_5)#["#2ca25f", "#ece2f0", "#43a2ca", "#dd1c77", "#e6550d", "#8856a7"])
ax.set_xlim(0,1)

ax.set_title('Breakdown by Race of the Top\n100 Cited Authors by %s' %subfield_synonym, fontsize = title_fontsize)

## Legend stuffs 
# Shrink current axis by 20%
box = ax.get_position()
ax.set_position([box.x0, box.y0, box.width * 0.8, box.height])

# Put a legend to the right of the current axis
lgd = ax.legend(["East Asian", "Hispanic/Latinx", "South Asian", "Middle Eastern", "White/European"],loc='center left', bbox_to_anchor=(1, 0.5), fontsize = legend_fontsize)


## y-axis stuffs
ax.yaxis.label.set_visible(False)
y_ticklabels = [l.get_text().title() for l in ax.yaxis.get_ticklabels()]
ax.set_yticklabels(y_ticklabels, fontsize = label_fontsize)

## x-axis stuffs
ax.tick_params(axis="x", labelsize=label_fontsize)

#fig.tight_layout()
# https://stackoverflow.com/questions/10101700/moving-matplotlib-legend-outside-of-the-axis-makes-it-cutoff-by-the-figure-box
fig.savefig("../figures_v3/%s_top_100_authors_race_proportions_by_subfield_%s.png" %(plot_code,now), bbox_extra_artists=[lgd], bbox_inches='tight')
plt.show()

# %%
## Gender of top 100 authors
fig,ax = plt.subplots(1,1,figsize = (10,5))
df = pd.read_csv("../data/bigquery/mag_syed_netsci_filtered_authors_20191025/final_table_top_100_authors_diff_field_with_gender_race.csv")
df_bar = df.groupby(["field_name","gender"]).size().rename('count')
df_bar = df_bar / df_bar.groupby(level=0).sum()
df_bar = df_bar.to_frame().reset_index()
df_bar = df_bar.pivot("field_name","gender","count").fillna(0)
flattened = pd.DataFrame(df_bar.to_records())
ax = flattened.plot(x='field_name', ax = ax, kind='barh', stacked=True, mark_right=True, color=palette_male_female)
ax.set_xlim(0,1)
ax.set_title('Breakdown by Gender of the Top\n100 Cited Authors by %s' %subfield_synonym, fontsize = title_fontsize)

## legend stuffs
# Shrink current axis by 20%
box = ax.get_position()
ax.set_position([box.x0, box.y0, box.width * 0.8, box.height])
lgd = ax.legend(["Female", "Male"], loc='center left', bbox_to_anchor=(1, 0.5), fontsize = legend_fontsize)
#flattened['total']= flattened.iloc[:, 1:2].sum(axis=1)

## y-axis stuffs
ax.yaxis.label.set_visible(False)
y_ticklabels = [l.get_text().title() for l in ax.yaxis.get_ticklabels()]
ax.set_yticklabels(y_ticklabels, fontsize = label_fontsize)

## x-axis stuffs
ax.tick_params(axis="x", labelsize=label_fontsize)

plt.tight_layout()
plt.savefig("../figures_v3/%s_top_100_authors_gender_proportions_by_subfield_%s.png" %(plot_code,now), bbox_extra_artists=[lgd], bbox_inches='tight')
plt.show()
# %%
with pd.option_context('display.max_rows', None, 'display.max_columns', None):  # more options can be specified also
    print(flattened)
# %%
## Race of top 100 paper authors
fig,ax = plt.subplots(1,1,figsize = (10,5))
df = pd.read_csv("../data/bigquery/mag_syed_netsci_filtered_authors_20191025/final_table_top_100_paper_authors_diff_field_with_gender_race.csv")
df_bar = df.groupby(["field_name","race"]).size().rename('count')

df_bar = df_bar / df_bar.groupby(level=0).sum()
df_bar = df_bar.to_frame().reset_index()
df_bar = df_bar.pivot("field_name","race","count").fillna(0)
flattened = pd.DataFrame(df_bar.to_records())
ax = flattened.plot(x='field_name', ax=ax, kind='barh', stacked=True, mark_right=True, color=palette_race_5)

ax.set_title('Breakdown by Race for Authors of\nthe Top 100 Cited Papers by %s' %subfield_synonym, fontsize = title_fontsize)

## Legend stuffs 
# Shrink current axis by 20%
box = ax.get_position()
ax.set_position([box.x0, box.y0, box.width * 0.8, box.height])

# Put a legend to the right of the current axis
lgd = ax.legend(["East Asian", "Hispanic/Latinx", "South Asian", "Middle Eastern", "White/European"],loc='center left', bbox_to_anchor=(1, 0.5), fontsize = legend_fontsize)


## y-axis stuffs
ax.yaxis.label.set_visible(False)
y_ticklabels = [l.get_text().title() for l in ax.yaxis.get_ticklabels()]
ax.set_yticklabels(y_ticklabels, fontsize = label_fontsize)

## x-axis stuffs
ax.tick_params(axis="x", labelsize=label_fontsize)


ax.set_xlim(0,1)

plt.savefig("../figures_v3/%s_top_100_paper_authors_race_proportions_by_subfield_%s.png" %(plot_code,now), bbox_extra_artists=[lgd], bbox_inches='tight')
plt.show()
# %%
## Sex of top 100 paper authors
fig,ax = plt.subplots(1,1,figsize = (10,5))
df = pd.read_csv("../data/bigquery/mag_syed_netsci_filtered_authors_20191025/final_table_top_100_paper_authors_diff_field_with_gender_race.csv")
df_bar = df.groupby(["field_name","gender"]).size().rename('count')

df_bar = df_bar / df_bar.groupby(level=0).sum()
df_bar = df_bar.to_frame().reset_index()
df_bar = df_bar.pivot("field_name","gender","count").fillna(0)
flattened = pd.DataFrame(df_bar.to_records())
ax = flattened.plot(x='field_name',ax=ax, kind='barh', stacked=True, mark_right=True, color=palette_male_female)

ax.set_title('Breakdown by Gender for Authors of\nthe Top 100 Cited Papers by %s' %subfield_synonym, fontsize = title_fontsize)

## Legend stuffs 
# Shrink current axis by 20%
box = ax.get_position()
ax.set_position([box.x0, box.y0, box.width * 0.8, box.height])

# Put a legend to the right of the current axis
lgd = ax.legend(["Female","Male"],loc='center left', bbox_to_anchor=(1, 0.5), fontsize = legend_fontsize)


## y-axis stuffs
ax.yaxis.label.set_visible(False)
y_ticklabels = [l.get_text().title() for l in ax.yaxis.get_ticklabels()]
ax.set_yticklabels(y_ticklabels, fontsize = label_fontsize)

## x-axis stuffs
ax.tick_params(axis="x", labelsize=label_fontsize)

ax.set_xlim(0,1)
plt.tight_layout()
plt.savefig("../figures_v3/%s_top_100_paper_authors_gender_proportions_by_subfield_%s.png" %(plot_code,now), bbox_extra_artists=[lgd], bbox_inches='tight')
plt.show()