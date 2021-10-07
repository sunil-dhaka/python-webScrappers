from requests_html import HTMLSession

oursession=HTMLSession()

url='https://www.youtube.com/c/JohnWatsonRooney/videos?view=0&sort=da&flow=grid'

r=oursession.get(url)
r.html.render(timeout=100,sleep=1,scrolldown=3,keep_page=True)
print(r.status_code)
data=list()

for item in r.html.find('#video-title'):
    minidata={
        'title':item.text,
        'link':item.absolute_links # relative VS absolute links
    }
    data.append(minidata)

print(len(data))
print(data[0])

#===================
# keep in mind depending on your connectoin or browser render speed it may take time
# in that case try to use high value of timeout(it is in secs <--user specified) for rendering; but the render function multiplies(internally) it with 1000 and works in mili-secs
# browser waits for all resources and content to load, and probably waits until functions set to run on page load finish execution.
# link: https://stackoverflow.com/questions/63653201/pyppeteer-errors-timeouterror-navigation-timeout-exceeded-8000-ms-exceeded
# link; https://stackoverflow.com/questions/57250102/python3-ssl-certificate-problem-when-requests-html-install-chromium-using-pyppet
# with increase in scrolldown and then rendering scrolled page; that will take time 
# so increase timeout in proportion 
# don't forget to keep page that way only ; you get all the rendered data 
# I don't think this method is faster than selenium webcontroller
# though both use quite a load of resources
#===================
# render is being used to scrape dynamic websites like YT
# it renders javascript and gives us nice HTML to work with
# official docs: https://docs.python-requests.org/projects/requests-html/en/latest/
#===================
