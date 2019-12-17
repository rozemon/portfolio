## There are currently three projects here:  
**1) A perfume recommender system**  
**2) A manga classifier**  
**3) Comtrade data visualization**

In addition to the code provided here, a web version of these projects was developed. A short description of the projects along
with the libraries used are provided.

## 1 - Perfume recommender system  
The goal of this project is to recommend a perfume similar to the one provided as input.  
Data was scraped from a well known website containing perfumes data: Fragrantica. After some features engineering, a recommender
system using content based filtering was built.  

***Future updates:*** right now the only features used are the main accords and the gender. Future versions will implement a filtering
based on other features too, like season, sillage of the perfume, longevity, etc..  

***Tech stack used:*** **Scrapy** for scraping data; **Pandas** and **Scikit-learn** for data cleaning and learning.  
***Web-app:*** **Flask** to create the api (on *AWS Elastic Beanstalk environment*); **jQuery** for data rendering.  

## 2 - Manga classifier  
The goal of this project is to build a multilabel classifier to assign a genre to a manga plot.  
Data was scraped from Mangapanda. After some NLP preprocessing, a neural network is built. This NN assigns a score from 0 to 1
to each possible genre.  

***Future updates:*** a pre-trained embedding like the Universal Sentence Encoder maybe would improve the score. Aside from that, the
main problem is the low number of data points: Mangapanda contains only about 3000 manga. There is nothing I can do about that.
There is also a bug in the web app that sometimes leads to a memory leak and crash of the AWS Elastic Beanstalk environment,
but I haven't identified it yet, nor I was able to reproduce it.  

***Tech stack used:*** **BeautifulSoup** for scraping data; **Pandas**, **nltk** and **Scikit-Learn** for data cleaning and 
text preprocessing; **Keras/Tensorflow** for building the neural network; **matplotlib** and **seaborn** for data visualization.  
***Web-app:*** **Flask** to create the api (on *AWS Elastic Beanstalk environment*); **D3js** and **D3plus** for data rendering.  

## 3- Comtrade data visualization  
The goal of this project is to build a visualization system for import/export data from/to Italy.  
Data was taken from Comtrade using their api. After deleting unimportant features, the data was stored in a MySQL database.
After a lot time spent with matplotlib, I realized D3js was much more powerful and less time consuming. The visualization is
then provided in the website.  

***Future updates:*** build other types of visualization.  

***Tech stack used:*** **Pandas** for data cleaning.  
***Web-app:*** **MySQL** for data storing, **D3js** and **D3plus** for data visualization.  

