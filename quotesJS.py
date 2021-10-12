import requests
from bs4 import BeautifulSoup as bs
from selenium import webdriver# rather use helium to make it easy going
from time import sleep
url='http://quotes.toscrape.com/js/'

quotePage=webdriver.Firefox()
quotePage.get(url)
quoteList=[]
for page in range(10):
    html=quotePage.page_source
    soup=bs(html,'html.parser')
    quotes=soup.find_all('div',class_='quote')
    for quote in quotes:
        tags=[]
        for tag in quote.find_all('a',class_='tag'):
            tags.append(tag.string)
        quoteData={
            'text':quote.find('span',class_='text').string,
            'author':quote.find('small',class_='author').string,
            'tags':tags
        }
        quoteList.append(quoteData)
    print('quotes collected after page no',str(page+1),'are',len(quoteList)) 
    try:
        nextPage=quotePage.find_element_by_css_selector('html body div.container nav ul.pager li.next a')
        sleep(5)
        nextPage.click()
    except Exception as e:
        print(e)
        #quotePage.quit()
quotePage.quit()
[print(str(i+1), '). quote text -- ',quoteList[i]['text'],'\n') for i in range(5)]
'''
using bs4 to parse requested data gives no quotes as this is js rendered website
although we see some nice quote class and all in web-browser but it is not what requests gets
to get what we saw on inspect have to use selenium rendered html 
'''
'''r=requests.get(url)
print(r.status_code)

soup=bs(r.content,'html.parser')

quotes=soup.find_all('div',class_='quote')
print(quotes) #<-- [] empty'''