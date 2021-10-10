import requests
from requests_html import HTMLSession

class amzScrapper:

    def __init__(self):
        self.amzsessoin=HTMLSession()
        # even with these many headers it does not work after some time 
        # might want to try out IP rotating
        self.headers={
            'User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:92.0) Gecko/20100101 Firefox/92.0',
            'Connection':'keep-alive',
            'Origin': 'https://www.amazon.in',
            'X-Requested-With': 'XMLHttpRequest'
        }
        self.baseurl='https://www.amazon.in/dp/'

    def extractor(self,asin):
        r=self.amzsessoin.get(self.baseurl+str(asin),headers=self.headers)
        data={
            'name':r.html.find('span#productTitle',first=True).text.strip(),
            'price':r.html.find('span#priceblock_dealprice',first=True).text.strip(),
            'return':r.html.find('div#RETURNS_POLICY',first=True).text.strip(),
            'review':r.html.find('span#acrCustomerReviewText',first=True).text.strip(),
        }
        return data