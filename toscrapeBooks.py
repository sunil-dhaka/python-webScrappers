import requests
from bs4 import BeautifulSoup as bs

# pagination ul class page > li class next
#article class product_pod

baseURL='http://books.toscrape.com/'
basePageLink=baseURL+'catalogue/'


books=list()

# pagination restriction would be like
## toscrapeSoup.find('li',class_='next')!=None
#--------
for page in range(1,51):
    print('Getting book data from page ...',page)
    currLink=basePageLink+f'page-{page}.html'
    r=requests.get(currLink)
    toscrapeSoup=bs(r.text,features='html.parser')
    for book in toscrapeSoup.find_all('article',class_='product_pod'):
        item={
            'name':book.h3.a['title'],
            'link':baseURL+book.h3.a['href'],
            'image':baseURL+book.img['src'][3:], # ../,
            'price':book.find('p',class_='price_color').text,
            'availability':book.find('p',class_='instock availability').text.strip()
        }
        books.append(item)

print(len(books))