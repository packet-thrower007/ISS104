import socket
#s = socket.socket()
#s.settimeout(2)

#port = int(input("Port number:"))

#s.connect(("ad.samsclass.info", port))
#print(s.recv(1024).decode())
#s.close()



import socket
s = socket.socket()
s.settimeout(2)

#port = int(input("Port number:"))

s.connect(("ad.samsclass.info", 3000))
print(s.recv(1024).decode())
s.close()
