import socket
import os
import sys

s = socket.socket()
s.settimeout(2)

target = 'www.courseres.org'

s.connect((target, 80))
req = 'HEAD / HTTP/1.1\r\nHost: ' + target + '\r\n\r\n'
s.send(req.encode())
#print(s.recv(1024).decode())


original_stdout = sys.stdout

with open('hjddata1.dat.txt', 'w') as f:
    sys.stdout = f
    print("Writing s.recv to hjddata1.dat.txt")
    print(s.recv(1024).decode())
    sys.stdout = original_stdout 
    print('Written to File: hjddata1.dat.txt')
    f.close()

    
s.close()
