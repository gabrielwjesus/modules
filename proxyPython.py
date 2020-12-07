import requests 
from bs4 import BeautifulSoup

def getMyIP():
    url = "https://www.myip.com/"
    r = requests.get(url) 
    soup = BeautifulSoup(r.content, "html.parser")
    a = soup.find('span', attrs={"id":'ip'})
    print(a.get_text())    
    
def changeMyIp():
    URL = "http://api.proxiesapi.com"
    auth_key = "7715af50d5f11830e9750f695988bba1_sr98766_ooPq87"
    url = "https://www.myip.com/"
    PARAMS = {'auth_key':auth_key, 'url':url} 
    
    r = requests.get(url = URL, params = PARAMS) 
    soup = BeautifulSoup(r.content, "html.parser")
    a = soup.find('span', attrs={"id":'ip'})
    print(a.get_text())

ans = 0

while ans != 3:
    print('Menu')
    print('1 - Show My IP Address: ')
    print('2 - Change My IP Address  and Show with proxy: ')
    print('3 - Exit ')
    ans = int(input())
    if ans == 1 :
        getMyIP()
    elif ans == 2:
        changeMyIp()
    elif ans == 3:
        break




