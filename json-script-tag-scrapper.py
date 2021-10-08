import requests,json
from bs4 import BeautifulSoup as bs
from requests.api import patch

link='https://www.accommodationforstudents.com/london'
r=requests.get(link)
s=bs(r.text,'html.parser')
data=((s.find_all('script')))
data=data[-2]
print(data)
data=data.text
# in json formatter it was all right
#https://jsonformatter.org/#
data=json.loads(data.strip())
print(len(data))
print(len(data['props']['pageProps']['viewModel']['areasToShowInAreaLinksSectio']))