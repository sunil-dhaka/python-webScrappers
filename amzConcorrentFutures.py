from asinScrapper import amzScrapper
from requests_html import HTMLSession
import pandas as pd
from time import sleep,time
import concurrent.futures

# although concorrent is really faster:
# but in getASINS case it is not rendering pages, wonder why?
# one problem still presists with this is that: -- most of the asins are getting stuck somewhere

asins=[]
queryData=[]
#=========
# without concurrents
def getASINS(query,pageCount=10):
    asins=[]
    for page in range(pageCount):
        url='https://www.amazon.in/s?k=' + '+'.join(query.split(' '))+'&page='+str(page+1)
        headers={'User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:92.0) Gecko/20100101 Firefox/92.0'}
        s=HTMLSession()
        r=s.get(url,headers=headers)
        r.html.render(sleep=8,timeout=100)
        if r.html.find('div[data-asin]'): #<--- see if this works
            products=r.html.find('div[data-asin]')
            for product in products:
                if len(product.attrs['data-asin'])!=0:
                    asins.append(product.attrs['data-asin'])
        else:
            break
        print('processed page ...',page+1)
    return asins

query=input('which product? type your search query for amzScrapper -- ')
pageCount=int(input('how many pages -- '))
tic=time()
asins=getASINS(query,pageCount)#can try out to get more pages
toc=time()
print(toc-tic)
print(len(asins))
sleep(2)

#========
# with concurrents applied
'''def getASINS(pageCount):
    print('starting ...')
    global asins
    # need to change searc hquery manually for now[after k= and before &,join using '+']
    url='https://www.amazon.in/s?k=trimmer&page='+str(pageCount)
    headers={'User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:92.0) Gecko/20100101 Firefox/92.0','Connection':'keep-alive'}
    s=HTMLSession()
    r=s.get(url,headers=headers)
    print('rendering ...')
    # it is not even rendering what could be the reason
    r.html.render(sleep=8,timeout=100)
    print('rendered.')
    if r.html.find('div[data-asin]'): #<--- see if this works
        products=r.html.find('div[data-asin]')
        for product in products:
            if len(product.attrs['data-asin'])!=0:
                asins.append(product.attrs['data-asin'])
        print('processed --- ',pageCount)
    else:
        print('no data on page')
    print('got total products on this page --- ',len(asins))
    return
#query=input('which product? type your search query for amzScrapper -- ')
query=input('which product? type your search query for amzScrapper -- ')
pageCount=int(input('how many pages -- '))
pages=list(range(1,pageCount+1))
print(pages)
tic=time()
with concurrent.futures.ThreadPoolExecutor() as executor:
    executor.map(getASINS,pages)
toc=time()
print(toc-tic)
sleep(2)'''


print(len(asins))
print(asins[0:5])
def extractor(asin):
    global queryData
    amzsessoin=HTMLSession()
    headers={
        'User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:92.0) Gecko/20100101 Firefox/92.0',
        'Connection':'keep-alive'
    }
    baseurl='https://www.amazon.in/dp/'
    r=amzsessoin.get(baseurl+str(asin),headers=headers)
    try:
        '''name=r.html.find('span#productTitle',first=True).text.strip()
        print('name -- ', name)
        price=r.html.find('span#priceblock_dealprice',first=True).text.strip()
        print('price -- ', price)
        return_policy=r.html.find('div#RETURNS_POLICY',first=True).text.strip()
        print('return-policy -- ', return_policy)
        review=r.html.find('span#acrCustomerReviewText',first=True).text.strip()
        print('review -- ', review)'''
        '''
        findings:
        1. price is the culprit here, it makes sense also because many items don't have prices where I am looking, they are shown after you choose something
        2. removed price and got all
        3. some products don't have reviews also, so that also can damp numbers of products getting back
        4. without price I got 47 out of 60, and with price was getting only about 20
        '''
        data={
            'name':r.html.find('span#productTitle',first=True).text.strip(),
            #'price':r.html.find('span#priceblock_dealprice',first=True).text.strip(),
            'return':r.html.find('div#RETURNS_POLICY',first=True).text.strip(),
            'review':r.html.find('span#acrCustomerReviewText',first=True).text.strip(),
        }
        print(data)
        queryData.append(data)
        return
    except:
        pass

with concurrent.futures.ThreadPoolExecutor() as executor:
    executor.map(extractor,asins)

print(len(queryData))
queryDf=pd.DataFrame(queryData)
queryDf.to_csv('-'.join(query.split(' '))+'.csv',index=False)
print(queryDf.shape)
print(queryData[0])
# I think with some time given it might not give that none type error for some asins
# also function is not stopping even after pages stops comming through