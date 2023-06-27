#!/usr/bin/python3
import socket

def bannertime(ip,port):
 try:
    socket.setdefaulttimeout(2)
    s=socket.socket()
    s.connect((ip,int(port)))
    banner=str(s.recv(1024))
    return banner
 except Exception as a:
    return ("Exception is "+str(a))

def main():
	ipa=str(input("What is the first three octects of IP address?"))

	port = [22, 53, 25, 443, 80]

	for lasto in range(1,255):
		for singleport in port:
			banner=bannertime(ipa+"."+str(lasto),int(singleport))
			print("Banner  "+ipa+"."+str(lasto)+" "+banner)

if __name__ =='__main__' :
	main()





'''
With your Kali Live version make sure you have established a network connection
After you have established an internet connection in the Kali terminal write your IP address (use ifconfig command or nmcli device show )


Using Python 3 version and the sample code provided within Week04 code samples run the program loopwithlastoctect.py entering the first three octects of your ipaddress. Run once with port 21 and another time with port 80.
Write a quick sum up of the running code

Modify the above code to create a list of ports 53,25,443,80 and instead of interactively entering in the port number use the list to look at all port numbers for each one.
Run the modified code and write a quick sum up of the running code

Attach the answers to the and attach the code as your three initials iss104lb42.py.txt (for myself it would be resiss104lb32.py.txt) and email to schultzr@kellogg.edu

'''
