from asinScrapper import amzScrapper
from requests_html import HTMLSession
import pandas as pd
from time import sleep
query=input('for which product: ')

url='https://www.amazon.in/s?k=' + '+'.join(query.split(' '))

headers={'User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:92.0) Gecko/20100101 Firefox/92.0'}
s=HTMLSession()
r=s.get(url,headers=headers)
r.html.render(sleep=8,timeout=100)
# render is important to get html rendered page
products=r.html.find('div[data-asin]')
asins=[]
for product in products:
    if len(product.attrs['data-asin'])!=0:
        asins.append(product.attrs['data-asin'])

print(len(asins))
sleep(5)
queryData=[]
for asin in asins:
    try:
        prod=amzScrapper() 
        queryData.append(prod.extractor(asin))
        '''print('sleeping ...')
        sleep(5)'''
        # sleep also can be avoided as this was not due to bot(that amz might detect we are automating) issue
        print(asin)
        print(queryData[-1])
        # can not scrape more than few elements that is some bullshit
        # might have to try out ````rotating proxies````
        # actually there was no issue with proxy in fact those asins were not all actually asins
        # so with try-except it was just nice and easy
    except Exception as e:
        print(e)
print(len(queryData))
queryDf=pd.DataFrame(queryData)
queryDf.to_csv('-'.join(query.split(' '))+'.csv',index=False)
print(queryData[0])