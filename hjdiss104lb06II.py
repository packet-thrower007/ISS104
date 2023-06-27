import hashlib

def crackPassword(username,hash):
    for i in range(0,100):
        if i < 10:
            password = "CCSF-" + username + "-0" + str(i)
        else:
            password = "CCSF-" + username + "-" + str(i)
        h = hashlib.new('md4', password.encode("utf-16le"))
        if h.hexdigest() == hash:
            return password
        else:
            continue

mingHash = "52c4859c0617e4a8fec24ba890c5fc57"
mohammedHash = "39057ef3a9fe57d98e7a9bab7cd2f4f9"
samHash = "19a641d2520b983abb7c931ceff933fa"

mingPassword = crackPassword("ming",mingHash)
mohammedPassword = crackPassword("mohammed",mohammedHash)
samPassword = crackPassword("sam",samHash)

print("Ming's Password is " + mingPassword)
print("Mohammed's Password is " + mohammedPassword)
print("Sam's Password is " + samPassword)
