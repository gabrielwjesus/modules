from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys


options = Options()
options.headless = True
#driver = webdriver.Firefox(options=options, executable_path=r'C:\geckodriver.exe')
driver = webdriver.Firefox(executable_path=r'C:\geckodriver.exe')

emailName = input('Insert email Here: ')
print('We are going to get details about email')

email = driver.find_element_by_tag_name('input')
email.send_keys(emailName)
driver.find_element_by_tag_name('input').send_keys(Keys.ENTER)

valid = driver.find_element_by
("//div[@class='col-md-12 text-center']/h2").text()
print(valid)

driver.quit()
