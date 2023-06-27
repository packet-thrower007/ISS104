import socket
s = socket.socket()
s.settimeout(2)

target = 'target1.bowneconsulting.com'

s.connect((target, 80))
req = '''POST /php/login2.php HTTP/1.1\r
Host: target1.bowneconsulting.com\r
Connection: keep-alive\r
Content-Length: 15\r
Cache-Control: max-age=0\r
Upgrade-Insecure-Requests: 1\r
Origin: http://target1.bowneconsulting.com\r
Content-Type: application/x-www-form-urlencoded\r
User-Agent: python\r
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7\r
Referer: http://target1.bowneconsulting.com/php/login2.php\r
Accept-Language: en-US,en;q=0.9\r
\r
u=dumbo&p=dumbo
'''

s.send(req.encode())
print(s.recv(1024).decode())
s.close()
