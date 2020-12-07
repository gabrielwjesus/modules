import requests 
from bs4 import BeautifulSoup
from urllib.parse import urlparse

address = input("Insert the Address to get all URL details: ")

o = urlparse(address)

if o.netloc == '':
    url = address
else:
    url = o.netloc
            
r = requests.get("https://www.iana.org/whois?q="+url)   
soup = BeautifulSoup(r.content, "html.parser")
showText = soup.find('pre').getText()   
print(showText)