import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import datetime
import numpy as np
import matplotlib.font_manager as font_manager
# %%
plot_code= "06_01_03"
now = datetime.datetime.now().strftime("%Y%m%d")
# %%
title_fontsize = 17
label_fontsize = 15
legend_fontsize = 14
subfield_synonym = "Keywords"
# %%
df = pd.read_csv("../data/bigquery/mag_syed_netsci_filtered_authors_20191025/for_box_plot_selected_author_paper_gender.csv")
# %%
ax = sns.violinplot(x="gender", y="netsci_paper_count", data=df,whis=[25,75])