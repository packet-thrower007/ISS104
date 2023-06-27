import hashlib


for i in range(0,100):        
	if i < 10:
#		print("if")
		password = "0" + str(i)
	else:
#		print("else")
		password = str(i)
	h = hashlib.new('md4', password.encode("utf-16le"))

	if "baad" in h.hexdigest():
		print(h.hexdigest())
		print(str(i) + " is the password of the hash")
