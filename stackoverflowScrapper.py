import requests
from bs4 import BeautifulSoup as bs
import pandas as pd
import sqlite3

conn=sqlite3.connect('stackoverflow.db')
cur=conn.cursor()
cur.execute("create table questions(title text, views int, excerpt text, link text)")

questionList=[]

def getQestions(tag,page,tab):
    global questionList
    userAgent={'User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:92.0) Gecko/20100101 Firefox/92.0'}
    url=f'https://stackoverflow.com/questions/tagged/{tag}?tab={tab}&page={page}&pagesize=50'
    r=requests.get(url,headers=userAgent)
    soup=bs(r.text,features='html.parser')
    questions=soup.find_all('div',class_='question-summary')
    if len(questions)>0:
        for question in questions:
            views=question.find('div',class_='views supernova')
            if views:
                postView=int(views.get('title')[:-6].replace(',',''))
            else:
                postView=0
            summary=question.find('div',class_='summary')
            title=summary.find('h3').string.strip()
            link='https://stackoverflow.com'+summary.find('a',class_='question-hyperlink').get('href')
            excerpt=summary.find('div',class_='excerpt').string.strip()
            questionData=(title,postView,excerpt,link) #<-- tuple
            questionList.append(questionData)
            #print(questionData)
        print('page no', page, 'completed')
        print('total questions are',len(questionList),'after pages no',page)
        return
    else:
        print(f'{tag} tag does not have any question on page no {page} in {tab} tab .')
        return
    
tag=input('tag -- ')
tab=input('tab -- ')
pages=int(input('no of pages -- '))

print('starting ...')
for page in range(pages):
    getQestions(tag,str(page+1),tab)

cur.executemany("insert into questions values(?,?,?,?)",questionList)
conn.commit()
print('stored in DB.')
questionDF=pd.read_sql_query("select * from questions order by views",conn)
print(questionDF.shape)
#questionDF.to_csv(f'question-from-stackoverflow-{tag}.csv',index=False)

cur.execute("select views from questions order by views")
print(cur.fetchall())
conn.close()