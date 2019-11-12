from genderize import Genderize
from time import sleep
# %%
plot_code = "03_01"
# %%
for chunk_num in range(0+1):
    print(chunk_num)
    ## genderizer_api_output = Genderize().get(['James', 'Eva', 'Thunderhorse'])
    genderize = Genderize(
        user_agent='GenderizeDocs/0.0',
        api_key='8ed9d26bd181ed45b928c6711f9f7806',
        timeout=30.0)

    open_dir = "../data/genderize/input_v2/"          
    open_file = "02_01_02_matt_combined_correct_new_names_to_be_genderized"
    #chunk_num = 0
    open_fname = open_dir+"%s_%d.csv" %(open_file,chunk_num)
    valid_first_names = []
    with open(open_fname,"r") as f:
        for line in f:
            valid_first_names.append(line.strip())
    writelines = []
    writelines.append(",".join(["name","gender","probability","count"])+"\n")
    try:
        for fname in valid_first_names:
            genderizer_api_output = genderize.get([fname])
            name_gender = genderizer_api_output[0]
            writelines.append(",".join(map(str,[name_gender["name"],name_gender["gender"],name_gender["probability"],name_gender["count"]]))+"\n")
    except:
        print(fname)
    savefig_dir = "../data/genderize/output_v2/"
    savefig_file = "output_%s_%d.csv" %(open_file,chunk_num)
        
    with open(savefig_dir+savefig_file, "w") as f:
        f.writelines(writelines)
        
    sleep(2)