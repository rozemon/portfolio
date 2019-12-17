
# coding: utf-8

# # SCRAPER
# This scraper gets the list of all urls from the home_url, then it goes through them and saves the data in a dataframe.

# In[3]:


import pandas as pd
from bs4 import BeautifulSoup
import requests


# In[4]:


home_url = "https://www.mangapanda.com/alphabetical"
r = requests.get(home_url)
html_soup = BeautifulSoup(r.text, 'html.parser')
manga_col_containers = html_soup.find_all('div', class_ = "series_col")

manga_urls = []
for col in manga_col_containers:
    links = col.findAll('a')
    for a in links:
        if a.has_attr('href') and a['href']!="#top":
            manga_urls.append("https://www.mangapanda.com" + a['href'])


# In[7]:


df = pd.DataFrame()
for url in manga_urls:
    entry_dict = {}
    r = requests.get(url)
    if r.status_code == 404:
        continue
    html_soup = BeautifulSoup(r.text, 'html.parser')
    div_container = html_soup.find("div", id = "mangaproperties")
    table_container = div_container.findChildren("tr")
    div_sum = html_soup.find("div", id = "readmangasum")
    summary = div_sum.findChild("p").text
    genre = []
    genre_col = table_container[7].find_all("span", class_= "genretags")
    for gen in genre_col:
        if gen.text.strip() != '':
            genre.append(gen.text.strip())
    i = 0
    while i<=5:
        columns = table_container[i].findChildren("td")
        entry_dict[columns[0].text.replace(':','').strip()] = columns[1].text.strip()
        i+=1
    entry_dict['Genre'] = genre
    entry_dict['Plot'] = summary
    df = df.append(entry_dict, ignore_index = True)

df.to_csv("mangadb.csv", sep=';', encoding='utf-8')

