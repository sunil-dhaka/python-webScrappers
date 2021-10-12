from requests_html import HTMLSession
import sqlite3
from time import sleep,time
import concurrent.futures

'''
create and connect to a database;
sqlite3 has a nice feature 
if a db exists it does not create that db again rather connects to it 
otherwise creates and then connects
'''
conn=sqlite3.connect('amzProduct.db')

c=conn.cursor()
'''uncomment to first create a database and in reruns commnet it out'''
#c.execute("create table amzproducts(name text, price text, return text, review text)")

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

print(len(asins))
print(asins[0:5])
def extractor(asin):
    global queryData
    amzsessoin=HTMLSession()
    headers={
        'User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:92.0) Gecko/20100101 Firefox/92.0'
        }
    baseurl='https://www.amazon.in/dp/'
    r=amzsessoin.get(baseurl+str(asin),headers=headers)
    try:
        if r.html.find('span#priceblock_ourprice',first=True)!=None:
            price=r.html.find('span#priceblock_ourprice',first=True).text.strip().replace(',','')
        else:
            price=r.html.find('span#priceblock_dealprice',first=True).text.strip().replace(',','')
        # using tuples to use executemany
        data=(
            r.html.find('span#productTitle',first=True).text.strip(),
            price,
            r.html.find('div#RETURNS_POLICY',first=True).text.strip(),
            r.html.find('span#acrCustomerReviewText',first=True).text.strip()
            )
        print(data)
        queryData.append(data)
        #print(queryData)
        return
    except:
        pass

with concurrent.futures.ThreadPoolExecutor() as executor:
    executor.map(extractor,asins)

print(len(queryData))

# also can use lower case query words 
# doing one by one is slower than executemany()
#c.executemany("insert into amzproducts values (?,?,?,?)",queryData)
c.executemany('''INSERT INTO amzproducts VALUES (?,?,?,?)''', queryData)
conn.commit()

#c.execute("select return from amzproducts")
c.execute('''SELECT return FROM amzproducts''')
results=c.fetchall()
print('return policy on items',results)

# can store in a nice df to view results
import pandas as pd
df=pd.read_sql_query("select * from amzproducts",conn)
print(df.shape)
conn.close()
