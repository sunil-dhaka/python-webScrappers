import requests
from bs4 import BeautifulSoup as bs
import gspread

def yellScrapper(businessQuery,location,totalPages=5):
    baseURL='https://www.yell.com'
    businessData=[]
    for page in range(totalPages):
        url='https://www.yell.com/ucs/UcsSearchAction.do?keywords='+'+'.join(businessQuery.split(' '))+'&location='+location+'&pageNum='+str(page+1)
        # when tried without headers got no result as it got blocked by yellow pages bot detector
        # with browser like user-agent did not got detected
        headers={'User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:92.0) Gecko/20100101 Firefox/92.0'}
        r=requests.get(url,headers=headers)
        print(r.status_code)
        soup=bs(r.text,'html.parser')
        businesses=soup.find_all('article')
        print(len(businesses))
        if len(businesses)>0:
            for business in businesses:
                try:
                    mainContent=business.find('div',class_='row businessCapsule--mainRow')
                    #print(mainContent)
                    # some businesses might not have 
                    if mainContent.find('a',class_='btn btn-yellow businessCapsule--ctaItem')!=None:
                        website=mainContent.find('a',class_='btn btn-yellow businessCapsule--ctaItem')['href']
                    else:
                        website=''
                    businessdata={
                        'name':mainContent.find('a',class_='businessCapsule--title').text.strip(),
                        'category':mainContent.find('span',class_='businessCapsule--classification').string.strip(),
                        #'link':mainContent.find('img',class_='lazy-loaded').get('src'),
                        'meta':mainContent.find('span',{'itemprop':'address'}).text.strip(),
                        'website':website
                    }
                    businessData.append(businessdata)
                    #print(businessdata)
                except Exception as e:
                    print(e)
        else:
            break    
        print('processed page -- ',page+1)
    return businessData

businessQuery=input('which business -- ')
location=input('where in UK -- ')
totalPages=int(input('how many pages -- '))
businessData=yellScrapper(businessQuery,location,totalPages)
print('Got total results  ',len(businessData))
print('first five -- ',businessData[0:5])

def gSheet(productList):
    googleCreds=gspread.service_account(filename='googleSheetsCreds.json')
    googleSheet=googleCreds.open('yellPagesUK').sheet1
    for i in range(len(productList)):
        product=productList[i]
        googleSheet.append_row([str(product['name']),str(product['category']),str(product['meta']),str(product['website'])])
    return None

gSheet(businessData)