
# coding: utf-8

# # COMTRADE SCRAPER
# This scraper generates api calls to the Comtrade Api (Documentation: https://comtrade.un.org/data/doc/api)
# It takes the input from external files in the folder "input".
# A lot of csv files are generated and then joined at the end. They are stored in the output folder.

# In[ ]:


import os
from os import listdir
from os.path import isfile, join
import pandas as pd
import requests
from io import StringIO
import uuid
import math
import time


# In[ ]:


current_path = os.getcwd()
input_path = os.path.join(current_path, "input")
output_path = os.path.join(current_path, "output")

partners_dummies = pd.read_csv(input_path + "/uncomtrade_partners.csv", sep = ",", encoding='latin-1').set_index('V0')
partners_list = partners_dummies.loc[partners_dummies['V3'] == 1]["V1"].tolist()

reporting_dummies = pd.read_csv(input_path + "/uncomtrade_reporting.csv", sep = ",", encoding='latin-1').set_index('V0')
reporting_list = reporting_dummies.loc[reporting_dummies['V3'] == 1]["V1"].tolist()

HS_dummies = pd.read_csv(input_path + "/HS5.csv", sep = ";", encoding='latin-1', dtype = "object")
HS_list = HS_dummies["V2"].tolist()

years_dummies = pd.read_csv(input_path + "/uncomtrade_years.csv", sep = ",", encoding='latin-1').set_index('V0')
years_list = years_dummies.loc[years_dummies['V3'] == 1]["V1"].tolist()

def group_elements(input_list, max_value, separator):
    list_process = input_list.copy()
    list_single_group = []
    list_grouped = []
    counter = 0
    while len(list_process) > 0:
        if len(list_process) < max_value:
            max_value = len(list_process)
        list_single_group = list_process[0:max_value]
        list_grouped.append(separator.join(list_single_group))
        list_process = list_process[max_value:]
    return list_grouped

HS_grouped_list = group_elements(HS_list, 19, "%2C")
years_grouped_list = group_elements(years_list, 5, "%2C")
url_list = []
url_error_list = []
max_number_requests = 99
time_stop = math.floor(3600/max_number_requests)


# In[ ]:


def getComtrade(url = "https://comtrade.un.org/api/get?",   #URL di base
                maxrec=50000,    #records max number
                tipe="C",    #trade type (C = commodities)
                freq="A",    #frequency: yearly, monthly, ecc...
                px="hs",    #classification type
                ps = "placeholder",     #time period
                r = "placeholder",    #reporting area
                p="all",    #country partner
                rg="all",    #trade flow
                cc = "placeholder",    #classification code
                fmt="csv"):    #save format
    query = (str(url) + "max=" + str(maxrec) + "&" + "type=" + str(tipe) + "&" + "freq=" + str(freq) + "&" 
               + "px=" + str(px) + "&" + "ps=" + str(ps) + "&" + "r=" + str(r) + "&" + "p=" + str(p) + "&" 
               + "rg=" + str(rg) + "&" + "cc=" + str(cc) + "&" + "fmt=" + str(fmt))
    
    try:
        response = requests.get(query)
        if response.status_code == 200:
            df_response = pd.read_csv(StringIO(response.text))
            saveComtrade(df_response, ps, r, p, cc) 
        else:
            url_error_list.append(query)
    except:
        url_error_list.append(query)
    time.sleep(time_stop)
    
def saveComtrade(df_argument ,ps = "Err" , r = "Err" , p = "Err", cc = "Err"):
    filename = ("tradefile" + str(uuid.uuid4()) + ".csv")
    #print("Saving dataset with reporter " + str(r) + " with partner " + str(p)+ " with HS " + str(cc) + " for year " + str(ps))
    filename_absolute_path = os.path.join(output_path, filename)
    df_argument.to_csv(filename_absolute_path, sep=',', encoding='utf-8')


# In[ ]:


total_queries = len(partners_list) * len(reporting_list) * len(HS_grouped_list) * len(years_grouped_list)
i = 1
for p1 in partners_list:
    for p2 in reporting_list:
        for p3 in HS_grouped_list:
            for p4 in years_grouped_list:
                getComtrade(p = p1, r = p2, cc = p3, ps = p4)
                print("\nQuery " + str(i) + "/" + str(total_queries) + "\n")
                print("\nElapsed time: " + str((i*time_stop)/60) + " minutes")
                print("\nRemaining time: " + str(((total_queries-i)*time_stop)/60) + " minutes")
                i = i+1


# In[ ]:


def csv_fusion():
    filelist = [f for f in listdir(output_path) if isfile(join(output_path, f))]
    filelist_csv = []
    for x in filelist:
        if x.startswith("trade") and x.endswith(".csv"):
            filelist_csv.append(x)

    dataframe_list = []
    for elem in filelist_csv:
        dataframe_temp = pd.read_csv(output_path + "/" + elem, sep = ",", encoding='latin-1')
        dataframe_list.append(dataframe_temp)
    final_df = pd.concat(dataframe_list, ignore_index=True)
    final_df.to_csv(output_path + "/" + "Comtrade_raw_data.csv", sep = ",", encoding='latin-1', index=False)

csv_fusion()

