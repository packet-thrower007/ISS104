import socket
import re
 
port = 22020
 
def findNextPort(currentPort):
    s = socket.socket()
    try:
        s.connect(("target1.bowneconsulting.com",currentPort))
        try:
            banner = s.recv(1024).decode()
            print("port " + str(currentPort) + " is open with banner " + banner)
            newPort = re.findall('[0-9]{5}', banner)
            print(newPort)
            port = int("".join(newPort))
#            print("captured port", port)
            s.close()
            return port
        except:
            print("port " + str(currentPort) + " is open with no banner")
            s.close()
            return 0
    except:
        print("port " + str(currentPort) + " is closed")
        s.close()
        return 0
 
while port != 0:
    port = findNextPort(port)
