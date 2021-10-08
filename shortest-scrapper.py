# +++++++ only workd with HTML pages 
from requests_html import HTMLSession
session=HTMLSession() # calling an instance of class
r=session.get('https://metro.co.uk/news/uk/')
print(r.status_code)
postData=r.html.find('.metro-mosaic',first=True).find('.metro__post__title')
scrapeData=[(post.text,post.find('a',first=True).attrs['href']) for post in postData] # doing first=True is imp as find() method returns a list