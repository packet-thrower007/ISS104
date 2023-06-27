import maxminddb
import geoip2.database
import time

with geoip2.database.Reader('/home/kali/iss104/week8/geo.mmdb') as reader:    
    host = ["172.67.75.72", "50.63.7.243"]
    for i in host:
        response = reader.city(i)
#    response.country.iso_code
#    response.country.name
        response.location.latitude
        print(i)
        print("The Latitude of is: ", response.location.latitude)
        response.location.longitude
        print("The Longitude is: ", response.location.longitude)    
        print("Sleeping for 5")
        time.sleep(5)
reader.close()
