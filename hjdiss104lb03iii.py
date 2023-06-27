import re

try:
	with open('readfileISS104.txt') as f:
		org_string = f.read().replace('\n', '')


# printing original string 
		print("The original string : " + org_string) 
		result = re.findall(r'\d+',org_string)
		print (result)

except:
	print("An error occured, check the file formating or existance.")
