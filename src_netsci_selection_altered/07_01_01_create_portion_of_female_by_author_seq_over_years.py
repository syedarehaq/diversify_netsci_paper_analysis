import matplotlib.pyplot as plt
import pandas as pd
import matplotlib
import numpy as np
import datetime
from itertools import cycle
# %%
plot_code = "07_01_01"
now = datetime.datetime.now().strftime("%Y%m%d")
anomaly_type = "with_anomaly"
#anomaly_type = "without_anomaly"
year_after = 1997
year_until = 2019
# %%
title_fontsize = 17
label_fontsize = 15
legend_fontsize = 14
# %%

labels_to_legend_text = {
            "first": "First Author",
            "middle": "Middle Author",
            "last": "Last Author"
        }
colors = {
            "first": '#2D4DBF',
            "middle": '#E07A5F',
            "last": "#81B29A",
        }
# %%
df_yearly_netsci_paper_count = pd.read_csv("../data/bigquery/mag_syed_netsci_filtered_authors_20191025/x_yearly_netsci_paper_count.csv")
df_yearly_netsci_paper_count = df_yearly_netsci_paper_count[df_yearly_netsci_paper_count["year"].isin(range(year_after+1,year_until+1))]
years,netsci_paper_counts = df_yearly_netsci_paper_count["year"],df_yearly_netsci_paper_count["yearly_netsci_paper_count"]

# %%
df = pd.read_csv("../data/bigquery/mag_syed_netsci_filtered_authors_20191025/x_yearly_portion_of_female_unique_authors_by_authorship_netsci.csv")
df = df[df["year"].isin(range(year_after+1,year_until+1))]

fig, ax = plt.subplots(figsize=(15,5))
for key, grp in df.groupby(['authorship_type']):
    ax = grp.plot(ax=ax, kind='line', x='year', y='portion_of_female_unique_authors_by_authorship', label=key, color=[colors[i] for i in grp['authorship_type']])
ax.set_ylim(0,1)
ax_paper_cont = ax.twinx()
ax_paper_cont.plot(years,netsci_paper_counts)

## Legend stuffs
handles, labels = ax.get_legend_handles_labels()
labels_to_handles = {label:handle for label,handle in zip(labels,handles) }
labels_ordered, handles_ordered = [], []
for l in ["first","middle", "last"]:
    labels_ordered.append(labels_to_legend_text[l])
    handles_ordered.append(labels_to_handles[l])
ax.legend(handles_ordered, labels_ordered,loc='best')
## legend stuffs ends

plt.tight_layout()
plt.savefig("../figures_v3/%s_unique_author_by_year_and_authorship_type_%s" %(plot_code,now))
plt.show()

# %%
df = pd.read_csv("../data/bigquery/mag_syed_netsci_filtered_authors_20191025/x_yearly_portion_of_female_authorship_events_by_authorship_types_netsci.csv")
df = df[df["year"].isin(range(year_after+1,year_until+1))]

fig, ax = plt.subplots(figsize=(15,5))

for key, grp in df.groupby(['authorship_type']):
    ax = grp.plot(ax=ax, kind='line', x='year', y='portion_of_female_unique_authors_by_authorship', label=key, color=[colors[i] for i in grp['authorship_type']])
ax.set_ylim(0,1)
ax_paper_cont = ax.twinx()
ax_paper_cont.plot(years,netsci_paper_counts)
handles, labels = ax.get_legend_handles_labels()
labels_to_handles = {label:handle for label,handle in zip(labels,handles) }
labels_ordered, handles_ordered = [], []
for l in ["first","middle", "last"]:
    labels_ordered.append(labels_to_legend_text[l])
    handles_ordered.append(labels_to_handles[l])
ax.legend(handles_ordered, labels_ordered,loc='best')
plt.tight_layout()
plt.savefig("../figures_v3/%s_authorship_events_by_year_and_authorship_type_%s" %(plot_code,now))
plt.show()
# %%
if anomaly_type == "with_anomaly":
    df = pd.read_csv("../data/bigquery/mag_syed_netsci_filtered_authors_20191025/x_yearly_portion_of_citation_to_female_by_authorship_types_netsci.csv")
    df = df[df["year"].isin(range(year_after+1,year_until+1))]
elif anomaly_type == "without_anomaly":
    df = pd.read_csv("../data/bigquery/mag_syed_netsci_filtered_authors_20191025/x_yearly_portion_of_citation_to_female_by_authorship_types_netsci_without_anomaly.csv")
    df = df[df["year"].isin(range(year_after+1,year_until+1))]

fig, ax = plt.subplots(figsize=(10,5))

lines = ["-","--","-.",":"]
linecycler = cycle(lines)

for key, grp in df.groupby(['authorship_type']):
    x = grp["year"]
    y = grp["portion_of_female_unique_authors_by_authorship"]
    ax.plot(x,y,label = key, linestyle = next(linecycler), color = colors[key], zorder = 0)
    #ax = grp.plot(ax=ax, kind='line', x='year', y='portion_of_female_unique_authors_by_authorship', label=key, style=["-","--","."])#, color=[colors[i] for i in grp['authorship_type']] )
ax.set_ylim(0,1)
ax_paper_cont = ax.twinx()
#paper_count_line = ax_paper_cont.plot(years,netsci_paper_counts, linestyle = ":", color = "0.2", linewidth = 1, zorder = 0)
paper_count_bar = ax_paper_cont.bar(years,netsci_paper_counts, width=0.6, alpha=0.3, zorder = 5, color = "#fdbb84")#"0.2")

# legend stuffs
handles, labels = ax.get_legend_handles_labels()
labels_to_handles = {label:handle for label,handle in zip(labels,handles) }
labels_ordered, handles_ordered = [], []
for l in ["first","middle", "last"]:
    labels_ordered.append(labels_to_legend_text[l])
    handles_ordered.append(labels_to_handles[l])
ax.legend(handles_ordered + [paper_count_bar[0]], labels_ordered + ["Paper Count"],loc='upper left', fontsize = legend_fontsize)

ax.set_xlabel("Year", fontsize = label_fontsize)
ax.set_ylabel("Portion of citation received by female authors", fontsize = label_fontsize)
ax.set_title("Proportion of citation female authors received over time", fontsize = title_fontsize)


ax_paper_cont.set_ylabel("Network sciene paper count", fontsize = label_fontsize)

# x label stuffs
x_axis = ax.axes.get_xaxis()
x_label = x_axis.get_label()
##print isinstance(x_label, matplotlib.artist.Artist)
#x_label.set_visible(False)

## GRID
ax.xaxis.grid(linestyle=':', linewidth=0.75)
ax.yaxis.grid(linestyle=':', linewidth=0.75)


# tick stuffs
ax.tick_params(axis='both', which='major', labelsize=label_fontsize-1)
ax_paper_cont.tick_params(axis='both', which='major', labelsize=label_fontsize-1)

plt.tight_layout()
plt.savefig("../figures_v3/%s_citation_events_by_year_and_authorship_type_%s_%s" %(plot_code,anomaly_type,now))
plt.show()