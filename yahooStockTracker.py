import requests
from bs4 import BeautifulSoup as bs
import json
'''
checked source page and we can use bs to get our information;
although these classes seems a bit kind of machined
for more collection can use custom headers; because yahoo also does not allow after some time an automated header
so better use custom header to avoid such cases in multiple runs of code
even if you think you are not getting your info 
try to check print(r.text)
also check that soup is getting something or not
#print(soup.title.text) #<-- should give webpage title back if it is working

but my function does not seem to work all the time <-- funny thing I totally forgot f-string's Mr. f head
'''

'''
func that return stock current price and change in stock price
'''
def yahooStock(stockSymbol):
    url=f'https://finance.yahoo.com/quote/{stockSymbol}'
    headers={'User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:92.0) Gecko/20100101 Firefox/92.0','Connection':'keep-alive'}
    r=requests.get(url,headers=headers)
    soup=bs(r.text,'html.parser')
    #stockSymbol=soup.find('h1',class_='D(ib) Fz(18px)').string[-5:-1]
    priceData=soup.find('div',class_='D(ib) Mend(20px)').find_all('span')
    currPrice=priceData[0].text
    changePrice=priceData[1].text
    #print(stockSymbol)
    print(soup.title.text)
    print(currPrice)
    print(changePrice)
    stockItem={
        'symbol':stockSymbol,
        'price':currPrice,
        'priceChange':changePrice
    }
    return stockItem

portfolioStockList=['SOFI','AAPL','BABA','AMC','AMD']
portfolioStockInfo=[]
for item in portfolioStockList:
    portfolioStockInfo.append(yahooStock(item))

with open('portfolioData.json','w') as file:
    json.dump(portfolioStockInfo,file)