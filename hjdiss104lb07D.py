
text = "HELLO"
text2 = "VCVDVEKRIP"
key = -1


def encrypt_text(text,key):
    ans = ""
    # iterate over the given text
    for i in range(len(text)):
        ch = text[i]
        
        # check if space is there then simply add space
        if ch==" ":
            ans+=" "
        # check if a character is uppercase then encrypt it accordingly 
        elif (ch.isupper()):
            ans += chr((ord(ch) + key-65) % 26 + 65)
        # check if a character is lowercase then encrypt it accordingly
        
        else:
            ans += chr((ord(ch) + key-97) % 26 + 97)
    
    return ans

def encrypt_text2(text2,key):
    ans = ""
    # iterate over the given text
    for i in range(len(text2)):
        ch = text2[i]

        # check if space is there then simply add space
        if ch==" ":
            ans+=" "
        # check if a character is uppercase then encrypt it accordingly 
        elif (ch.isupper()):
            ans += chr((ord(ch) + key-65) % 26 + 65)
        # check if a character is lowercase then encrypt it accordingly

        else:
            ans += chr((ord(ch) + key-97) % 26 + 97)

    return ans



print("Flag VP 301.1: Encrypt Text")
print("Plain Text is : " + text)
print("Character Shift: " + str(key))
print("Excrypt Text: " + encrypt_text(text,key))


print("###########################################")

print("Flag VP 301.2: Dencrypt Text")      
print("Encrypted Text is : " + text2)
print("Character Shift: " + str(key))
print("Decrypted Text: " + encrypt_text2(text2,key))
