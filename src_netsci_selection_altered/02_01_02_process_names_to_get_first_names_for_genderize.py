import re
# %%
plot_code = "02_01_02"

# %%
## Lets create a set of the available valid first names
valid_first_names = set()
open_dir = "../data/bigquery/mag_syed_netsci_filtered_authors_20191025_matt/"
open_file = "matt_combined_correct_new_names_to_be_genderized.csv"
with open(open_dir+open_file, "r") as f:
    print(f.readline())
    for line in f:
        author_name = line.strip().split(",")[0]
        first_name = author_name.strip().split()[0]
        ## first must be greater than 1, must only have alphacharcters e.g. no numbers
        ## and we are also avoiding chinsese, japanse, korean etc unicode characters
        if len(first_name) > 1: # and re.match('^[a-zA-Z]+$',first_name):
            valid_first_names.add(first_name)
# %%
chunk_size = 1000
savefig_dir = "../data/genderize/input_v2/"          
savefig_file = open_file.split(".")[0]
sorted_names = sorted(valid_first_names)
chunk_number = 0
while(sorted_names):
    with open(savefig_dir+"%s_%s_%d.csv" %(plot_code,savefig_file,chunk_number), "w") as f:
        f.writelines("\n".join(sorted_names[:chunk_size]))
        sorted_names = sorted_names[chunk_size:]
    chunk_number += 1