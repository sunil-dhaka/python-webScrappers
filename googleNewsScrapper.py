from requests_html import HTMLSession
# inspect html source code and see that it is not simple html pages there is JS everywhere
# that is why we need render and get nice html
url='https://news.google.com/topstories?hl=en-IN&gl=IN&ceid=IN:en'
session=HTMLSession()
r=session.get(url)
r.html.render(timeout=100,sleep=2,scrolldown=10)
articles=r.html.find('article')
newsGoogle=[]
# some fact check (on left-side nav) articles does not have time of post
# but solution(now commented) does not seems to work??
# with scrolls increased even newsAgency can not be gotten since there are some blocks in articles that are different
# and without class it seems kind of tough
# without newsAgency we can get more articles with scrolldown value change
for article in articles:
    try:
        if article.find('h3',first=True):
            title=article.find('h3',first=True).text
            # can get link using ``````absolute_links``````
            link='https://news.google.com'+(article.find('h3',first=True).find('a',first=True).attrs['href'])[1:]
            '''foo=article.find('time',first=True)
            if foo!=None:
                time=foo.text
            else:
                time='FactCheck'
            '''
            #newsAgency=article.find('div',first=True).find('a',first=True).text
        else:
            title=article.find('h4',first=True).text
            link='https://news.google.com'+(article.find('h4',first=True).find('a',first=True).attrs['href'])[1:]
            
            '''foo1=article.find('time',first=True)
            if foo1!=None:
                time=foo1.text
            else:
                time='FactCheck'
            '''
            #newsAgency=article.find('div',first=True).find('a',first=True).text
        newsGoogle.append({'title':title,'link':link})
    except Exception as e:
        print(e)

print(newsGoogle[0:5])
print(len(newsGoogle))