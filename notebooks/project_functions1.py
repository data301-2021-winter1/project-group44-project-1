#Michael's Functions
import pandas as pd
import numpy as np



def load_and_process(url_or_path_to_csv_file):
    df = pd.read_csv(url_or_path_to_csv_file)
    df = df.T
    df[df ==".."] = np.nan
    df[df =="..t"] = np.nan
    df1 = (df.dropna(axis=0)
           .T)
    return df1

def clean_and_rename(df):
    df2 = (df.drop(df.columns[[1,2,3,4,10,15,16,17,18,19,20,21,22,23,24]], axis=1)
         .rename(columns={
         "Selected Government of Canada benchmark bond yields: 2 year": "S2Y",   
         "Selected Government of Canada benchmark bond yields: 3 year": "S3Y",
         "Selected Government of Canada benchmark bond yields: 5 year": "S5Y",
         "Selected Government of Canada benchmark bond yields: 7 year": "S7Y",
         "Selected Government of Canada benchmark bond yields: 10 year": "S10Y",
         "Government of Canada marketable bonds, average yield: 1-3 year 6": "M2Y",
         "Government of Canada marketable bonds, average yield: 3-5 year 6": "M4Y",
         "Government of Canada marketable bonds, average yield: 5-10 year 6": "M7Y",
         "Government of Canada marketable bonds, average yield: over 10 years 6": "M10Y",
         "Treasury Bills: 1 month": "T1M",
         "Treasury Bills: 2 month": "T2M",
         "Treasury Bills: 3 month": "T3M",
         "Treasury Bills: 6 month": "T6M",
         "Treasury Bills: 1 year": "T1Y",
         "Real return bonds, long-term": "Real Return"
                         }
                ))
    return df2

def new_dataframe(df1):
    df2 = (df1.assign(One_Month = df1["T1M"])
          .assign(Two_Month = df1["T2M"])
          .assign(Three_Month = df1["T3M"])
          .assign(Six_Month = df1["T6M"])
          .assign(One_Year = df1["T1Y"])
          .assign(Two_Year = (df1["S2Y"]+df1["M2Y"])/2)
          .assign(Three_Year = df1["S3Y"])
          .assign(Four_Year = df1["M4Y"])
          .assign(Five_Year = df1["S5Y"])
          .assign(Seven_Year = (df1["S7Y"]+df1["M7Y"])/2)
          .assign(Ten_Year = (df1["S10Y"]+df1["M10Y"])/2)
          .drop(df1.columns[[1,2,3,4,5,6,7,8,9,10,11,12,13,14]], axis=1)
      )
    return df2

def group_(df2):
    Return_Level = []
    for i in df2["Real Return"]:
        if i < 0:
            Return_Level.append("Negative")
        elif 0< i < 0.3:
            Return_Level.append("Low")
        elif 0.3<i<0.6:
            Return_Level.append("Medium")
        else:
            Return_Level.append("High")
    df2["Return Level"]=Return_Level
    df3 = (df2.assign(Short_Period = (df2["One_Month"]+df2["Two_Month"]+df2["Three_Month"]+df2["Six_Month"])/4)
          .assign(Medium_Period = (df2["One_Year"]+df2["Two_Year"]+df2["Three_Year"]+df2["Four_Year"])/4)
          .assign(Long_Period = (df2["Seven_Year"]+df2["Five_Year"]+df2["Ten_Year"])/3)
          .drop(df2.columns[[0,2,3,4,5,6,7,8,9,10,11,12]], axis=1)
      )
    df3
    return df3