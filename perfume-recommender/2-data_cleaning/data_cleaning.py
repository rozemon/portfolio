
# coding: utf-8

# # DATA CLEANING
# 

# In[1]:


import pandas as pd


# In[2]:


df = pd.read_csv("scraped_data.csv", sep=";")
df.head()


# In[3]:


df.shape


# ## There are 27 columns.
# ## The following code joins correlated columns to help reduce the dataframe features.
# ## The groups of correlated columns are:
# 
# # 1) Seasons:
# "spring", "summer", "autumn", "winter". These are reduced to one column, representing the season(s) with most votes in the row.

# In[4]:


#adds a new column (called "seasons") to the original dataframe containing a list of the seasons with the highest values
season_list = ["spring", "summer", "autumn", "winter"]
df_season = df[season_list]
pd.options.mode.chained_assignment = None
df_season["season_1"] = df_season.idxmax(axis=1, skipna= True) #it only finds the highest score. If two season have equal score, it selects the first one.
df_season["season"] = ""

season_list_list = []
for index, row in df_season.iterrows():
    seasons_max = []
    seasons_max.append(row["season_1"])
    max_value = row[row["season_1"]]
    for seas in season_list:
        if row[seas] == max_value:
            if not seas in seasons_max:
                seasons_max.append(seas)
    df_season.at[index, 'season'] = seasons_max
col_season = df_season["season"]
df = pd.concat([df, col_season], axis=1)

#deletes the columns named after the single seasons
for seas in season_list:
    del df[seas]


# # 2) Like rating:
# "love", "like", "dislike". These Like rating column contains a score which is the weighted sum of these three values. This value is then divided by the total votes:  (a*love + b*like)/(love+like+dislike). The weights a and b are arbitrary and i set a=b=1.

# In[5]:


#adds a new column (called "like_rating") to the original dataframe containing a value that sums up the user rating. This value is a percentage
liking_list = ["love", "like", "dislike"]
df_liking = df[liking_list]
df_liking['total_votes'] = df_liking.sum(axis=1)
df_liking["like_rating"] = 0
#set a parameter called "love_par" to set the weight of love votes. Default = 1
love_par = 1
for index, row in df_liking.iterrows():
    denom = (love_par * row["love"] + row["like"] + row["dislike"])
    if denom != 0:
        like_rating = ((love_par * row["love"] + row["like"])*100// denom)
    else:
        like_rating = 0
    df_liking.at[index,"like_rating"] = like_rating
col_liking = df_liking["like_rating"]
df = pd.concat([df, col_liking], axis=1)
#deletes the columns named after elements of liking_list
for like in liking_list:
    del df[like]


# # 3) Sillage rating:
# "ssoft", "smoderate", "sheavy", "senormous". This represents the intensity of the perfume, and the formula is: (a*ssoft + b*smoderate + c*sheavy + d*senormous)/(ssoft + smoderate + sheavy + senormous). The resulting value then falls in one of the four categories.
# 

# In[6]:


#adds a new column (called "sillage_rating") to the original dataframe containing a value that sums up the sillage rating. This value is a percentage
sillage_list = ["ssoft", "smoderate", "sheavy", "senormous"]
df_sillage = df[sillage_list]
df_sillage['total_votes'] = df_sillage.sum(axis=1)
df_sillage["sillage_rating"] = ""
#set parameters to set the weight of votes. I set arbitrary parameters
soft_par = -2
moderate_par = -1
heavy_par = 1
enormous_par = 2
for index, row in df_sillage.iterrows():
    denom = (row["ssoft"] + row["smoderate"] + row["sheavy"] + row["senormous"])
    if denom != 0:
        sillage_score = ((soft_par * row["ssoft"] + moderate_par * row["smoderate"] + heavy_par * row["sheavy"] + enormous_par * row["senormous"])*100// denom)
        if sillage_score <(-100):
            sillage_rating = "soft"
        elif sillage_score <= 0:
            sillage_rating = "moderate"
        elif sillage_score > 100:
            sillage_rating = "enormous"
        else:
            sillage_rating = "heavy"
    else:
        sillage_rating = "No data"
    df_sillage.at[index,"sillage_rating"] = sillage_rating
col_sillage = df_sillage["sillage_rating"]
df = pd.concat([df, col_sillage], axis=1)
#deletes the columns named after elements of sillage_list
for sil in sillage_list:
    del df[sil]


# # 4) Longevity rating:
# "lpoor", "lweak", "lmoderate", "llong", "lverylong".

# In[7]:


#adds a new column (called "longevity_rating") to the original dataframe containing a value that sums up the longevity rating. This value is a percentage
longevity_list = ["lpoor", "lweak", "lmoderate", "llong", "lverylong"]
df_longevity = df[longevity_list]
df_longevity['total_votes'] = df_longevity.sum(axis=1)
df_longevity["longevity_rating"] = ""
#set parameters to set the weight of votes. I set arbitrary parameters
poor_par = -2
weak_par = -1
moderate_par = 0
long_par = 1
verylong_par = 2
for index, row in df_longevity.iterrows():
    denom = (row["lpoor"] + row["lweak"] + row["lmoderate"] + row["llong"] + row["lverylong"])
    if denom != 0:
        longevity_score = ((poor_par * row["lpoor"] + weak_par * row["lweak"] + moderate_par * row["lmoderate"] + long_par * row["llong"] + verylong_par * row["lverylong"])*100// denom)
        if longevity_score <(-120):
            longevity_rating = "poor"
        elif longevity_score <= (-40):
            longevity_rating = "weak"
        elif longevity_score <= 40:
            longevity_rating = "moderate"
        elif longevity_score <= 120:
            longevity_rating = "long"
        else:
            longevity_rating = "very long"
    else:
        longevity_rating = "No data"
    df_longevity.at[index,"longevity_rating"] = longevity_rating
col_longevity = df_longevity["longevity_rating"]
df = pd.concat([df, col_longevity], axis=1)
#deletes the columns named after elements of longevity_list
for lon in longevity_list:
    del df[lon]


# # 5) Day rating:
# "day", "night".

# In[8]:


#adds a new column (called "day_rating") to the original dataframe containing a value that sums up the user rating. This value is a percentage
day_list = ["day", "night"]
df_day = df[day_list]
df_day['total_votes'] = df_day.sum(axis=1)
df_day["day_rating"] = ""

for index, row in df_day.iterrows():
    if (row["day"] + row["night"]) == 0:
        day_rating = "No data"
    elif row["day"] >= row["night"]:
        day_rating = "day"
    else:
        day_rating = "night"

    df_day.at[index,"day_rating"] = day_rating
col_day = df_day["day_rating"]
df = pd.concat([df, col_day], axis=1)
#deletes the columns named after elements of day_list
for da in day_list:
    del df[da]


# # 6) Gender:
# the fragrance gender is extracted from the name of the perfume and is put in this column

# In[9]:


#create column to distinguish men perfumes from women perfumes
df["gender"] = ""
for index, row in df.iterrows():
    if "for women and men" in row["name"]:
        gender = "unisex"
    elif "for men and women" in row["name"]:
        gender = "unisex"
    elif "for men" in row["name"]:
        gender = "men"
    elif "for women" in row["name"]:
        gender = "women"
    else:
        gender = "No data"
    df.at[index,"gender"] = gender


# In[10]:


df.head()


# In[11]:


df.shape


# ## Now the are only 15 columns.

# In[12]:


df.to_csv("data_clean.csv", sep=';', encoding='utf-8', index = False)

