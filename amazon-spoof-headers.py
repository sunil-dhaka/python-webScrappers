from lxml import html
from requests_html import HTMLSession

url='https://www.amazon.in/gp/product/B08VB57558/'

amzSession=HTMLSession()
#===============================
# amazon does not allow without headers
# notice user-agent is python without headers
# {'User-Agent': 'python-requests/2.23.0', 'Accept-Encoding': 'gzip, deflate', 'Accept': '*/*', 'Connection': 'keep-alive'}
#===============================

headers={'User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:92.0) Gecko/20100101 Firefox/92.0'}
r=amzSession.get(url,headers=headers)
itemData={
    'name':r.html.find('span#productTitle',first=True).text.strip(),
    'price':r.html.find('span#priceblock_dealprice',first=True).text.strip(),
    'return':r.html.find('div#RETURNS_POLICY',first=True).text.strip()
}
# choosing first by setting it to true is imp in request_html
print(itemData)

## things to notes:
# even with headers you could face this bot issue on other sites or even on amazon
# we could try giving other keys to the headers param