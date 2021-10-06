import requests
from bs4 import BeautifulSoup as bs
import logindetails 
#-----------
# make a separate logindetails.py file in the same folder
# then add it to .gitignore to not upload on github
#-----------

payload={
    'username': logindetails.username,
    'password': logindetails.password
}

# a get request is our browser asking for information not the response #

loggedInUrl=('https://the-internet.herokuapp.com/secure') #<-- this is the url we would use after getting logged in
requestURL=('https://the-internet.herokuapp.com/authenticate') #<-- this is the url we would send our authentication crediantials when we wnat to log in

#----------------
# to get it look into the network section of inspection window and then look for a POST request and into its header
#----------------
'''r=requests.post(requestURL,data=payload)
# tihs posts our credantials to the request URL

print(r.status_code)
print(r.text)

r2=requests.get(loggedInUrl)
print(r.status_code)
print(r.text)'''

# to not be logged in after we are done with our session

with requests.session() as ourSession: #<-- this is where we are creating our context session ans it keeps us in logged in so that we can do our scrapping 
    ourSession.post(requestURL,data=payload)
    r=ourSession.get(loggedInUrl)
    soup=bs(r.text,'html.parser')
    print(soup.prettify())
