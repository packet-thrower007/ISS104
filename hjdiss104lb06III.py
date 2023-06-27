import hashlib

def crackPassword(username,hash):
    for i in range(0,100):
        if i < 10:
            password = "CCSF-" + username + "-0" + str(i)
        else:
            password = "CCSF-" + username + "-" + str(i)
        password2 = password
        for j in range(0,100):
            h = hashlib.new('md5', password2.encode())
            if h.hexdigest() == hash:
                print(j)
                return password
            else:
                password2 = h.hexdigest()

mingHash = "7621eca98fe6a1885d4f5f56a0525915"
mohammedHash = "b2173861e8787a326fb4476aa9585e1c"
samHash = "42e646b706acfab0cf8079351d176121"

mingPassword = crackPassword("ming",mingHash)
mohammedPassword = crackPassword("mohammed",mohammedHash)
samPassword = crackPassword("sam",samHash)

print("Ming's Password is " + mingPassword)
print("Mohammed's Password is " + mohammedPassword)
print("Sam's Password is " + samPassword)
