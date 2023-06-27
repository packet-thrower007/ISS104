import requests
import time
from bs4 import BeautifulSoup


address = ["http://courseres.org", "https://www.kellogg.edu"]

for i in address:
#    res = requests.get(i)
    page = requests.get(i)
    soup = BeautifulSoup(page.content, 'html.parser')
    title = soup.title.text
    print(title)

#    print(res.text)
#    print(res.status_code)
    print("Sleeping for 10 Seconds before get request to next site in list")
    time.sleep(10)
