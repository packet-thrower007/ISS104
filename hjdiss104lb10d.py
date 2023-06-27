#import requests
#import time
#from bs4 import BeautifulSoup


#address = ["http://courseres.org", "https://www.kellogg.edu"]

#for i in address:
#    page = requests.get(i)
#    soup = BeautifulSoup(page.content, 'html.parser')    
#    metatags = soup.find_all('meta',attrs={'name':'generator'})
    
#    for tag in metatags:
#        print("MetaData for:", i)
#        print(tag)

#    title = soup.title.text
#    print(title)

#    print(res.text)
#    print(res.status_code)
#    print("Sleeping for 10 Seconds before get request to next site in list")
#    time.sleep(10)


import requests
from bs4 import BeautifulSoup
# Make a request

address = ["http://courseres.org", "https://www.kellogg.edu"]

for i in address:
    page = requests.get(i)
    soup = BeautifulSoup(page.content, 'html.parser')
    page_title = soup.title.text
    print(page_title)
# Create top_items as empty list
    all_links = []

# Extract and store in top_items according to instructions on the left
    links = soup.select('a')
    for ahref in links:
        text = ahref.text
        text = text.strip() if text is not None else ''

        href = ahref.get('href')
        href = href.strip() if href is not None else ''
        all_links.append({"href": href, "text": text})

print(all_links)
