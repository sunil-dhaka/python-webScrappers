import requests
from bs4 import BeautifulSoup as bs

baseurl='https://www.thewhiskyexchange.com/'
url=baseurl+'/c/35/japanese-whisky?pg='
links=list()
for i in range(1,5):
    r=requests.get(url+str(i))
    soup=bs(r.text,'html.parser')
    for link in soup.find('div',class_='product-grid').find_all('a',class_='product-card'):
        links.append(baseurl+link['href'])

whiskeyData=[]
for link in links:
    r=requests.get(link)
    soup=bs(r.text,'html.parser')
    header=soup.find('header',class_='product-main__header')
    if header.find('span',class_='review-overview__count')!=None:
        reviews=header.find('span',class_='review-overview__count').text
    else:
        reviews='notFound'
    item={
        'names':header.h1.text,
        'meta_names':header.p.text,
        'reviews':reviews,
        'desc':soup.find('div',class_='product-main__description').p.text.strip(), # always can strip() to remove whitespaces and all
        'image':soup.find('img',class_='product-main__image')['src'],
        'price':soup.find('p',class_='product-action__price').text.strip()
    }
    whiskeyData.append(item)