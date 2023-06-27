import hashlib

def crackPassword(username,hash):
    for i in range(0,100):
        if i < 10:
            password = "CCSF-" + username + "-0" + str(i)
        else:
            password = "CCSF-" + username + "-" + str(i)
        password2 = password
        for j in range(0,500):
            h = hashlib.new('md5', password2.encode())
            password3 = h.hexdigest()
            for k in range(0,500-j):
                h2 = hashlib.new('sha1', password3.encode())
                if h2.hexdigest() == hash:
                    print(j)
                    print(k)
                    return password
                else:
                    password3 = h2.hexdigest()
            password2 = h.hexdigest()

mingHash = "ce788ed5f855e51e6fd78f923b43a6407467c5f2"
mohammedHash = "582d99006950cddeb2df9f40b3f65ebc283dc378"
samHash = "da660655f4d4714fe605e9063d1ded4b749c50a9"

mingPassword = crackPassword("ming",mingHash)
mohammedPassword = crackPassword("mohammed",mohammedHash)
samPassword = crackPassword("sam",samHash)

print("Ming's Password is " + mingPassword)
print("Mohammed's Password is " + mohammedPassword)
print("Sam's Password is " + samPassword)
