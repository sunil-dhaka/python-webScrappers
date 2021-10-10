from requests_html import HTMLSession
# inspect html source code and see that it is not simple html pages there is JS everywhere
# that is why we need render and get nice html
url='https://www.beerwulf.com/en-gb/c/beer-kegs/sub-kegs'
session=HTMLSession()
r=session.get(url)
r.html.render(timeout=50,sleep=2)
# I have to read official docs for better and effecient work with this module
beers=r.html.xpath('//*[@id="product-items-container"]',first=True)
#print(beers.absolute_links)
beerData=[]
for beer in beers.absolute_links:
    try:
        r=session.get(beer)
        if r.html.find('div.add-to-cart-container'):
            inStock=True
        else:
            inStock=False
        beerdata={
            'name':r.html.find('div.product-detail-info-title',first=True).text,
            'meta':r.html.find('div.product-subtext',first=True).text,
            'stock':inStock
        }
        beerData.append(beerdata)
        print(beerdata)
        #print(r.html.find('div.product-detail-info-title',first=True).text)
        #print(r.html.find('div.product-subtext',first=True).text)
    except Exception as e:
        print(e)