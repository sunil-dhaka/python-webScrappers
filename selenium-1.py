from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait

url='https://the-internet.herokuapp.com/login'

internet=webdriver.Firefox()
internet.get(url)

internet.implicitly_wait(10)

internet.find_element_by_xpath('//*[@id="username"]').send_keys('tomsmith')
internet.find_element_by_xpath('//*[@id="password"]').send_keys('SuperSecretPassword!')
internet.implicitly_wait(5)
internet.find_element_by_xpath('/html/body/div[2]/div/div/form/button/i').click()
# you need to find the xpath for right element for this to work. #
# don't forgegt to close the connection
internet.close() #or quit()