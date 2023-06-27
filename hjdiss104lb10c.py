import requests
import time
from bs4 import BeautifulSoup


address = ["http://courseres.org", "https://www.kellogg.edu"]

for i in address:
    page = requests.get(i)
    soup = BeautifulSoup(page.content, 'html.parser')    
    metatags = soup.find_all('meta',attrs={'name':'generator'})
    
    for tag in metatags:
        print("MetaData for:", i)
        print(tag)

    title = soup.title.text
    print(title)

#    print(res.text)
#    print(res.status_code)
    print("Sleeping for 10 Seconds before get request to next site in list")
    time.sleep(10)
