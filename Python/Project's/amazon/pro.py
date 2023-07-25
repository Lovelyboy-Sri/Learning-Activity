from bs4 import BeautifulSoup
import requests,time
import pandas as pd


# Url initialize
url = "https://www.amazon.in/s?i=grocery&bbn=16392737031&dc&page=2&ref=sr_pg_2"

# Take this one in whatismybrowser.com site
head = ({'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36','Accept-Language':'en-in,en;q=0.5'})

# webpage request testing
w = requests.get(url,headers=head)
soup = BeautifulSoup(w.content,"html.parser")

# Anyone product a-tag link
l = soup.find_all("a",class_="a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal")
link = l[0].get('href')

# New web page Request testing
nl = f"https://amazon.com/{link}"
nw = requests.get(nl,headers=head)
nsoup = BeautifulSoup(nw.content,"html.parser")

# Getting info from web pages
#name = nsoup.find('span',attrs={'id':"productTitle"}).text.strip()
#brand = nsoup.find('a',attrs={'id':'bylineInfo'}).string
price = nsoup.find('span',attrs={'class':'a-size-medium a-color-price'})
Rating = nsoup.find('span',attrs={'class':"a-icon-alt"}).text.replace("out of 5 stars "," ")
Review = nsoup.find('span',attrs={'id':'acrCustomerReviewText'}).text
print(Rating)

