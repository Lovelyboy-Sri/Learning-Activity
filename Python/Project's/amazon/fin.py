# Package initialization
from bs4 import BeautifulSoup
import requests
import pandas as pd

# Title Section
def title(soup):
    try:
        # outer tag
        title = soup.find("span",attrs={'id':'productTitle'})

        # Inner Tag
        title_val = title.text

        # Title as string
        title_str = title_val.strip()

    except AttributeError:
        title_str = ""
    
    return title_str

# Brand Section
def brand(soup):
    try:
        brand = soup.find('a',attrs={'id':'bylineInfo'}).string
    except AttributeError:
        brand = ""
    return brand

# Price Section
def price(soup):
    try:
        price = soup.find("span",attrs={'id':'priceblock_ourprice'}).string
    except AttributeError:
        price = soup.find("span",attrs={'id':'productTitle'})
    return price

# Star Ratings Section
def rate(soup):
    try:
        Rating = soup.find('span',attrs={'class':"a-icon-alt"}).text.replace("out of 5 stars "," ")
    except AttributeError:
        Rating = " "
    return rate

# Ratings count
def count(soup):
    try:
        Review = soup.find('span',attrs={'id':'acrCustomerReviewText'}).text
    except AttributeError:
        Review = ""
    return count


# Main part of the coding
if __name__ == "__main__":

    # Take this one in whatismybrowser.com site
    head = ({'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36','Accept-Language':'en-in,en;q=0.5'})

    # Url initialize
    url = "https://www.amazon.in/s?i=grocery&bbn=16392737031&dc&page=2&ref=sr_pg_2"

    # webpage request testing
    w = requests.get(url,headers=head)
    soup = BeautifulSoup(w.content,"html.parser")

    l = soup.find_all("a",class_="a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal")

    # Link Storing part
    links = []

    # Loop Extracting and importing
    for li in l:
        links.append(li.get('href'))
    
    d = {'Name':[],'Brand':[],'Price':[],'Ratings':[],'Count':[]}

    # Loop extracting product link for eachone 
    for link in links:
        nw = requests.get(f'https://www.amazon.com/{link}',headers=head)
        ns = BeautifulSoup(nw.content,'html.parser')

        # function calls to display
        d['Name'].append(title(ns))
        d['Brand'].append(brand(ns))
        d['Price'].append(price(ns))
        d['Ratings'].append(rate(ns))
        d['Count'].append(count(ns))
    
    af = pd.DataFrame.from_dict(d)
    af['title'].replace('',np.nan,inplace=True)
    af = af.dropna(subset=['title'])
    af.to_excel('Final.xlsx',header=True,index=False)