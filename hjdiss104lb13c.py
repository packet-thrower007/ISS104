import requests
from bs4 import BeautifulSoup

getpage= requests.get('http://www.python.org')
getpage_soup= BeautifulSoup(getpage.text, 'html.parser')

meta= getpage_soup.findAll('meta')


for m in meta:
    print(str(m)[6:-1])
