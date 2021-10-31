#Michael's Functions
import pandas as pd
import numpy as np



def load_and_process(url_or_path_to_csv_file):
    df = pd.read_csv(url_or_path_to_csv_file)
    df = df.T
    df[df ==".."] = np.nan
    df[df =="..t"] = np.nan
    df_cleaned = df.dropna(axis=0)
    df1 = df_cleaned.T
    return df1

def mean_sd_calculation(dataframe):
    dic = dict(dataframe)
    del dic["Date"]
    d = {"Date":("Mean","Standard Deviation")}
  
    for key in dic:
        mean = (sum(dic[key])/len(dic[key]))
        sd = np.std(dic[key])
        d[key]= [mean,sd]
    df2 = pd.DataFrame.from_dict(d)
    right = dataframe
    left = df2
    result = pd.merge(right,left,how="outer")
    return result
