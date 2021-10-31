#Michael's Functions
import pandas as pd
import numpy as np
def load_and_process(url_or_path_to_csv_file):
    df = pd.read_csv(url_or_path_to_csv_file)
    df[df ==".."] = np.nan
    df[df =="..t"] = np.nan
    df_cleaned = df.dropna(axis=0)
    df_cleaned = df_cleaned.T
    return df_cleaned