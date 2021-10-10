import requests
from bs4 import BeautifulSoup as bs

def mozillaScrapper(totalPages,baseURL):
    blogData=[]

    for page in range(totalPages):
        
        url=baseURL+'page/'+str(page+1)
        r=requests.get(url)
        soup=bs(r.text,features='html.parser')
        
        for blog in soup.find_all('section',class_='mzp-c-card mzp-has-aspect-1-1'):
            # tried and saw that for some posts image does not exists
            if blog.find('img',class_='mzp-c-card-image wp-post-image')!=None:
                imageLink=blog.find('img',class_='mzp-c-card-image wp-post-image')['src']
            else:
                imageLink='noLink'
            
            singleBlog={
                'title':blog.h2.text,
                'image':imageLink,
                'link':blog.a['href']
            }
            blogData.append(singleBlog)
        
        print('processed page no ...',page+1)

    return blogData

blogsOn=input('please type moxilla category:(internet-policy | firefox | mozilla-vpn | pocket | news | leadership | deep-dives | mozilla-explains | interviews | videos)  -- ')
# can be used prompt for better experience 
baseURL=f'https://blog.mozilla.org/en/category/{blogsOn}/'
r=requests.get(baseURL)
soup=bs(r.text,features='html.parser')

paginationData=soup.find_all('a',class_='page-numbers')

if len(paginationData)>0:
    noOfPages=int(paginationData[-2].text)
else:
    noOfPages=1

print('please give a number between 1 and ',noOfPages)

totalPages=int(input('How many pages -- '))

blogData=mozillaScrapper(totalPages,baseURL)
print(blogData[0:5])
# can store in a csv file