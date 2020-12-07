from bs4 import BeautifulSoup
import requests

URLextended = "https://urlex.org/" 

def extendUrl(URL):
    html = requests.get(URLextended+URL).content
    soup = BeautifulSoup(html, 'html.parser')
    extented = soup.findAll("a")[0].get('href')
    print('Your URL is:\n',extented)

url_short = input("Enter the Short URL: ")
extendUrl(url_short)