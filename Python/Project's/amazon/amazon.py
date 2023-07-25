from bs4 import BeautifulSoup
import requests,time

def pro():
    h = requests.get("https://www.amazon.in/s?i=grocery&bbn=16392737031&dc&page=2&ref=sr_pg_2").text

    s = BeautifulSoup(h,'lxml')
    page = s.find_all('div',attrs={"class":'s-main-slot s-result-list s-search-results sg-row'})

    a = []
    for l in page:
        name = l.find("span",class_="a-size-base-plus a-color-base a-text-normal").text
        if name not in a:
            a.append(name)
            price = l.find("span",class_="a-price-whole").text
            Str = l.find("span",class_="a-icon-alt").text
            ratings = l.find("span",class_="a-size-base s-underline-text").text
            ab = f"""\n Name : {name},\n Price : {price},\n Str : {Str},\n Ratings : {ratings}"""
            a.append(name)
            print(ab)
        print(a)

if __name__ == "__main__":
    while True:
        time.sleep(1)
        pro()
        