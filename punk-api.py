import requests
import json
#=========
# official docs: https://punkapi.com/documentation/v2
# also can give params to the link
#=========
link='https://api.punkapi.com/v2/beers?brewed_before=11-2012&abv_gt=6&per_page=39'

r=requests.get(link)
beerData=r.text # this is a str
# as we will be loading from a string so used loads rather than loading from a json-file
beerData=json.loads(beerData) 
# this is now converted into a json <=== not it is loads() ; not load() that is used to  json files 
print(len(beerData))
print(beerData[0])

# storing only interesting data and then storing into a df usual practice
# also user i/p can be taken for particular search