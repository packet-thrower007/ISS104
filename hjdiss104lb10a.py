import requests
import time

address = ["http://courseres.org", "https://www.kellogg.edu"]

for i in address:
    res = requests.get(i)
    print(res.text)
    print(res.status_code)
    print("Sleeping for 10 Seconds before get request to next site in list")
    time.sleep(10)
