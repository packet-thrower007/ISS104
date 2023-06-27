import json

count=0

with open("logins.json", "r") as read_file:
	data = json.load(read_file)
	for i in data.values():
		if i in data.values == "id":
			print(data, i)
#			print(['encryptedUsername'][2:])
#		count+=1
#		print(data["logins"][0]["id"])
#		print(data["logins"][0]["usernameField"][0:128])
#		print(data["logins"][0]["passwordField"][0:128]) 
#f.close()
