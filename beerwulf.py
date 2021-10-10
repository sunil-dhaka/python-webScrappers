from requests_html import HTMLSession
# inspect html source code and see that it is not simple html pages there is JS everywhere
# that is why we need render and get nice html
url='https://www.beerwulf.com/en-gb/p/beers/krusovice-royal-dark-2l-kegs'
session=HTMLSession()
r=session.get(url)
#r.html.render(timeout=50,sleep=2)
title=r.html.find('div.product-detail-info-title',first=True)
print(title)
price=r.html.find('span.price',first=True).text
print(price)