import socket

s = socket.socket()

for i in range(21000, 21031):
    try:
        s.connect(("target1.bowneconsulting.com",i))
        try:
            banner = s.recv(1024).decode()
            print("port " + str(i) + " is open with banner " + banner)
        except:
            print("port " + str(i) + " is open with no banner")
    except:
        print("port " + str(i) + " is closed")

s.close()
