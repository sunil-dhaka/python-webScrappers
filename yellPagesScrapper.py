import requests
from bs4 import BeautifulSoup as bs
from requests.api import head

def yellScrapper(businassQuery,location,totalPages=5):
    baseURL='https://www.yell.com'
    businassData=[]
    for page in range(totalPages):
        url='https://www.yell.com/ucs/UcsSearchAction.do?keywords='+'+'.join(businassQuery.split(' '))+'&location='+location+'&pageNum='+str(page+1)
        # when tried without headers got no result as it got blocked by yellow pages bot detector
        # with browser like user-agent did not got detected
        headers={'User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:92.0) Gecko/20100101 Firefox/92.0'}
        r=requests.get(url,headers=headers)
        print(r.status_code)
        soup=bs(r.text,'html.parser')
        businasses=soup.find_all('article')
        print(len(businasses))
        if len(businasses)>0:
            for businass in businasses:
                try:
                    mainContent=businass.find('div',class_='row businessCapsule--mainRow')
                    #print(mainContent)
                    businassdata={
                        'name':mainContent.find('a',class_='businessCapsule--title').text.strip(),
                        'category':mainContent.find('span',class_='businessCapsule--classification').string.strip(),
                        #'link':mainContent.find('img',class_='lazy-loaded').get('src'),
                        'meta':mainContent.find('span',{'itemprop':'address'}).text.strip(),
                        'website':mainContent.find('a',class_='btn btn-yellow businessCapsule--ctaItem').get('href')
                    }
                    businassData.append(businassdata)
                    #print(businassdata)
                except Exception as e:
                    print(e)
        else:
            break    
        print('processed page -- ',page+1)
    return businassData

businassQuery=input('which businass -- ')
location=input('where in UK -- ')
totalPages=int(input('how many pages -- '))
businassData=yellScrapper(businassQuery,location,totalPages)
print('Got total results  ',len(businassData))
print('first five -- ',businassData[0:5])