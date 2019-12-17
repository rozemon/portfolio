
# coding: utf-8

# # Recommendation system
# The two systems I evaluated are collaborative filtering and content based filtering.
# Maybe for perfums a collaborative filtering would be a better idea, but lacking data about users' buying patterns the only alternative was to use a content based filtering system.
# 
# In this version of the system I used only one feature: the main accords. Perfumes with identical accords can be different enough because the weights of the accords are different.
# The data is filtered by gender.
# In future versions there will be more filters based on seasons, sillage, longevity, etc...

# In[1]:


import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel


# In[2]:


df = pd.read_csv("data_clean.csv", sep = ";")
df.shape


# All unpopular/unknown perfumes are deleted to improve performance

# In[3]:


#filtering the dataframe to delete unpopular/unknown perfumes (and to improve performance)
df = df.loc[df["voters"]>10]
df.shape


# The dataframe is then filtered by gender

# In[4]:


#filtering the dataframe based on gender: 0 for men, 1 for women, 2 for unisex, 3 for all
def filtering(data, gender):
    data = data[["name", "main_accords", "gender"]]
    if gender == 0:
        data = data.loc[data['gender'] == "men"]
    if gender == 1:
        data = data.loc[data['gender'] == "women"]
    if gender == 2:
        data = data.loc[data['gender'] == "unisex"]
    if gender == 3:
        pass
    del data["gender"]
    return data

gender_select = int(input("Select one gender:\n1)Men\n2)Women\n3)Unisex\n4)All perfumes\n"))
df = filtering(df, gender_select)


# In[5]:


#preparing the text inside main_accords
for index, row in df.iterrows():
    df.at[index,"main_accords"] = row["main_accords"].replace(" ", "_").replace(",", " ")
df.reset_index(drop=True, inplace= True)


# Now a TF-IDF Vectorizer is created, and each accord is stored in an n-dimensional space and the cosine similarities method is used to determine the similarity between two accords.

# In[6]:


#using cosine similarities to find perfumes with similar notes
#creating TF-IDF vectorizer:
tfidf = TfidfVectorizer(analyzer='word', ngram_range=(1, 1), min_df=0)
tfidf_matrix = tfidf .fit_transform(df['main_accords'])

cosine = linear_kernel(tfidf_matrix, tfidf_matrix)
results = {}
for index, row in df.iterrows():
    sim_indices = cosine[index].argsort()[:-100:-1] 
    sim_items = [(cosine[index][i], df['name'][i]) for i in sim_indices] 
    results[row['name']] = sim_items[1:]


# In[7]:


def recommend(item_id, num):
    print(str(num) + " perfumes similar to " + item_id + ":")
    print("-------")
    recs = results[item_id][:num]
    for rec in recs:
        score_percent = int(rec[0]*100)
        print(rec[1] + " (score:" + str(score_percent) + "%)")


# The recommend function takes the name of a perfumes as input, and prints n perfumes similar to it. A perfume with 100% score has the same accords as the input, although the weights of the accords can differ.

# In[8]:


recommend(item_id="Reaction Kenneth Cole for men", num=20)

