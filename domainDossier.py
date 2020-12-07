from selenium import webdriver
from selenium.webdriver.firefox.options import Options
'''
from selenium.webdriver.common.proxy import Proxy, ProxyType

prox = Proxy()
prox.proxy_type = ProxyType.MANUAL
prox.http_proxy = "ip_addr:port"
prox.socks_proxy = "ip_addr:port"
prox.ssl_proxy = "ip_addr:port"

capabilities = webdriver.DesiredCapabilities.CHROME
prox.add_to_capabilities(capabilities)
'''

options = Options()
options.headless = True
driver = webdriver.Firefox(options=options, executable_path=r'C:\geckodriver.exe')
#driver = webdriver.Firefox(desired_capabilities=capabilities,options=options, executable_path=r'C:\geckodriver.exe')

URL = input('Insert your URL Here: ')
print('We are going to get all information about the URL for you')

driver.get('https://centralops.net/co/DomainDossier.aspx')

a = driver.find_element_by_id('addr')
a.send_keys(URL)

dom_whois = driver.find_element_by_id('dom_whois')
netWork = driver.find_element_by_id('net_whois')
dnsRecord = driver.find_element_by_id('dom_dns')
serviceScan = driver.find_element_by_id('svc_scan')
traceroute = driver.find_element_by_id('traceroute')

dom_whois.click()
netWork.click()
dnsRecord.click()
serviceScan.click()
traceroute.click()

clickGo = driver.find_element_by_id('go')
clickGo.click()

userDetails = driver.find_element_by_xpath('//table[1]')
print('Here is your User Details\n --> ')
print(userDetails.text)

findAddrLookUp = driver.find_element_by_xpath('//table[2]')
print('\nAddress lookup: ')
print(findAddrLookUp.text)

findDom_whois = driver.find_elements_by_xpath('//pre[1]')
print('\nDomain Whois Records')
for itemFindDom in findDom_whois:
    print(itemFindDom.text)

findNetwork = driver.find_element_by_xpath('//pre[2]')
print('\nNetwork Whois Records')
print(findNetwork.text)

findDNS = driver.find_element_by_xpath('//table[3]')
print('\nDNS Records')
print(findDNS.text)

driver.quit()