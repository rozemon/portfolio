
# coding: utf-8

# # DATA CLEANING
# A sample csv file is included. The complete csv dataset containing all trades between Italy and all other countries from 2004 to 2017 was about 4.2Gb.

# In[1]:


import pandas as pd
import os
from os import listdir
from os.path import isfile, join


# In[2]:


filename = "Comtrade_raw_data.csv"
df = pd.read_csv(filename, sep = ",", encoding='latin-1')


# In[3]:


columns = ['Aggregate Level',
 'Alt Qty Unit',
 'Commodity Code',
 'Commodity',
 'Flag',
 'Netweight (kg)',
 'Partner Code',
 'Reporter Code',
 'Trade Flow Code',
 'Trade Value (US$)',
 'Year']
df = df[columns]


# In[4]:


df.isnull().any()
#null values are present in unimportant columns


# In[5]:


df.to_csv("Comtrade_clean_data.csv", sep = ",", encoding='latin-1', index=False)

