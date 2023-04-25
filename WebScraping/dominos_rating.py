from bs4 import  BeautifulSoup
import requests
import datetime
import  pandas as pd

base_url = "https://www.consumeraffairs.com/food/dominos.html"
all_pages_reviews =[]
# query_parameter = "?page="+str(i)
url=""
page_reviews=[]
for i in range(1,6):
    query_parameter = "?page="+str(i)
    r=requests.get(base_url+query_parameter)
    soup=BeautifulSoup(r.content,"html.parser")
    div_res=soup.findAll('div',attrs={'class':'rvw-bd'})
    for i in range(len(div_res)):
        page_reviews.append(div_res[i].find('p').text)
    for i in range(len(page_reviews)):
        all_pages_reviews.append(page_reviews[i])


print(all_pages_reviews)

i = range(1, len(all_pages_reviews)+1)
reviews_df = pd.DataFrame({'review':all_pages_reviews}, index=i)
reviews_df.to_csv('reviews.csv', sep='t')