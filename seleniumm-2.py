from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import pandas as pd

#======= some useful selenium methods
#from selenium.webdriver.support.ui import WebDriverWait # <to eait for page to load
#from selenium.webdriver.chrome.options import Options # to set page loading strataegy
#======= see selenoum dev page on page-loading-strategy =========#
#options=Options()
#options.page_load_strategy = 'eager'
# does not waste data on image loading and css and etc
#=======
# since YT loads its data dinamically we can not use requests and BS4 for scrapping
#=======

url1='https://www.youtube.com/c/SBNCLASSES/videos' # default if there is not link
url2=input('Give channel videos page url --')

if len(url2)<1:
    url=url1
else:
    url=url2
internet=webdriver.Firefox()
internet.get(url)

time.sleep(5)
html=internet.find_element_by_tag_name('html')
for i in range(100): # should be enough but can not be sure
    html.send_keys(Keys.END)
    time.sleep(0.1)

vids=internet.find_elements_by_class_name('style-scope ytd-grid-video-renderer')
sbnData=list()

for vid in vids:
    item={
        # this '.' is imp
        'title':vid.find_element_by_xpath('.//*[@id="video-title"]').text,
        'link':vid.find_element_by_xpath('.//*[@id="video-title"]').get_attribute('href'),
        'views':int(vid.find_element_by_xpath('.//*[@id="metadata-line"]/span[1]').text[:-6]),
        'howOld':vid.find_element_by_xpath('.//*[@id="metadata-line"]/span[2]').text 
        # to only get text info from these tags
    }
    sbnData.append(item)

internet.close()
print(f'total no of videos on the channel: {len(sbnData)}')

sbnDF=pd.DataFrame(sbnData)
print(sbnDF.shape)
sbnDF.to_csv('sbnclasses-data.csv',index=False)