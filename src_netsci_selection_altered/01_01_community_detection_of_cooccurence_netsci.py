import networkx as nx
from networkx.algorithms import community
import pandas as pd
from graph_tool import collection
import community
from collections import defaultdict
# %%
df = pd.read_csv("../data/bigquery/mag_20191025/untracked/FieldsOfStudy.csv")

field_id_to_name = df.set_index("FieldOfStudyId").to_dict()["NormalizedName"]
field_id_to_level = df.set_index("FieldOfStudyId").to_dict()["Level"]

# %%
df = pd.read_csv("../data/bigquery/mag_syed_netsci_filtered_authors_20191025/cooccurence_links_fields_level_012345_valid_netsci_papers.csv")
df["weight"] = df["common_papers"]
# %%
g = nx.from_pandas_edgelist(df, "field_1", "field_2", ["weight"])
# %%
partition = community.best_partition(g)
# %%
comms = defaultdict(list)
comms_names = defaultdict(list)
for field_id,comm in partition.items():
    comms[comm].append(field_id)
    comms_names[comm].append(field_id_to_name[field_id])
# %%
with open("communities.txt","w") as f:
    for comm_number, field_names in comms_names.items():
        f.write(str(comm_number)+"\n")
        f.write("Number of nodes in this community is %d\n" %len(field_names))
        f.write(",".join(field_names)+"\n")
        f.write("\n")
    
# %%
list(map(len,comms.values()))
# %%
g.remove_node(137753397)
#%%
partition = community.best_partition(g)
# %%
comms = defaultdict(list)
comms_names = defaultdict(list)
for field_id,comm in partition.items():
    comms[comm].append(field_id)
    comms_names[comm].append(field_id_to_name[field_id])
# %%
with open("communities_no_ego.txt","w") as f:
    for comm_number, field_names in comms_names.items():
        f.write(str(comm_number)+"\n")
        f.write("Number of nodes in this community is %d\n" %len(field_names))
        f.write(",".join(field_names)+"\n")
        f.write("\n")
# %%
list(map(len,comms.values()))
# %%
communities_generator = community.girvan_newman(g)
top_level_communities = next(communities_generator)
# %%
c = list(community.k_clique_communities(g,4))
# %%
g = collection.data["football"]
print(g)
