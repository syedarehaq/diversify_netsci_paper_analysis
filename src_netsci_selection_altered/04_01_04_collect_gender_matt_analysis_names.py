import glob
import datetime
# %%
plot_code = "04_01_03"
now = datetime.datetime.now().strftime("%Y%m%d")
## we created 58 files before
first_name_to_gender = dict()
fnames = sorted(glob.glob("../data/genderize/output_v2/output_02_01_02_matt_combined*"))
for fname in fnames:
    with open(fname,"r") as f:
        f.readline()
        for line in f:
            splitted_line = line.strip().split(",")
            first_name = splitted_line[0]
            gender = splitted_line[1]
            first_name_to_gender[first_name] = gender
# %%
output_fdir = "../output_v2/gender/"
output_fname = "%s_matt_analysis_first_name_to_gender_with_None_%s.csv" %(plot_code,now)
writelines = []
writelines.append(",".join(["first_name","gender"])+"\n")
for fname,gender in first_name_to_gender.items():
    #if gender != "None":
    writelines.append(",".join([fname,gender])+"\n")
with open(output_fdir+output_fname,"w") as f:
    f.writelines(writelines)