from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
import time

options = Options()
options.headless = True
driver = webdriver.Firefox(options=options, executable_path=r'C:\geckodriver.exe')
#driver = webdriver.Firefox(executable_path=r'C:\geckodriver.exe')

#driver = webdriver.Firefox(desired_capabilities=capabilities,options=options, executable_path=r'C:\geckodriver.exe')

username = input('Insert username Here: ')
print('We are going to get all places where username has account')

driver.get('https://namecheckup.com/')
name = driver.find_element_by_id('serachText')
name.send_keys(username)
driver.find_element_by_id('serachText').send_keys(Keys.ENTER)
print('Waiting! We are trying to find')
time.sleep(20)

print('First we are find for USERNAMES')
taken = driver.find_elements_by_xpath("//div[@class='single_username_list taken']/a/span")
if taken != []:
    print('We found the links bellow')
    
    for x in taken:
        print(x.text)
else:
    print('Sorry, the user was not found')
    
print('\nNow We are finding for domain names (\nNOT WORKING YET)')
domains = driver.find_elements_by_xpath("//div[@class='single_d_name normal taken']/a")
if domains != []:
    print('We found the links bellow')
    
    for x in domains:
        print(x.text," for address "+username+x.text)
        
else:
    print('Sorry, the domain was not found')

driver.quit()


