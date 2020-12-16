
from http_request_randomizer.requests.proxy.requestProxy import RequestProxy
from selenium import webdriver


req = RequestProxy()
proxies = req.get_proxy_list()
PROXY = proxies[0].get_address()
print(PROXY)
webdriver.DesiredCapabilities.FIREFOX['proxy']={
    "httpProxy":PROXY,
    "ftpProxy":PROXY,
    "sslProxy":PROXY,
    "proxyType":"MANUAL",
}

driver = webdriver.Firefox(executable_path= r"C:\geckodriver.exe")
driver.get('http://ipv4.icanhazip.com')
addr = driver.find_element_by_xpath("//pre")

print(addr.text)
