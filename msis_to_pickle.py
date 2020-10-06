import pandas as pd 
import numpy as np
import os

from datetime import date
from datetime import datetime

print("Download report.xls...")
df_covid_msis = pd.read_excel("C:/Users/elga_/Downloads/report.xls", header=14, index_col=0)

print("Cleaning the data...")
df_covid_msis.replace("-", "0", inplace=True)

df_covid_msis["0 - 9"] = pd.to_numeric(df_covid_msis["0 - 9"])
df_covid_msis["10 - 19"] = pd.to_numeric(df_covid_msis["10 - 19"])
df_covid_msis["20 - 29"] = pd.to_numeric(df_covid_msis["20 - 29"])
df_covid_msis["30 - 39"] = pd.to_numeric(df_covid_msis["30 - 39"])
df_covid_msis["40 - 49"] = pd.to_numeric(df_covid_msis["40 - 49"])
df_covid_msis["50 - 59"] = pd.to_numeric(df_covid_msis["50 - 59"])
df_covid_msis["60 - 69"] = pd.to_numeric(df_covid_msis["60 - 69"])
df_covid_msis["70 - 79"] = pd.to_numeric(df_covid_msis["70 - 79"])
df_covid_msis["80+"] = pd.to_numeric(df_covid_msis["80+"])
df_covid_msis["Ukjent"] = pd.to_numeric(df_covid_msis["Ukjent"])

df_covid_msis["rep_date"] = np.datetime64(date.today())

print("Save to pickle...")
store_date = str(date.today())+'_'+ str(datetime.today().hour) +'_'+ str(datetime.today().minute)
df_covid_msis.to_pickle('D:/python workspace/ws1/covid19_related/data_covid/df_age_fylke_' + store_date + '.pkl')

print("Remove from disk...")
os.remove("C:/Users/elga_/Downloads/report.xls")

print("Finish.")
