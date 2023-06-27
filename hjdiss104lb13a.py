import crypt


hash1 = "Cu5KfyQFmmX7favGSu7Aw8ajyX32hthPhLyS9G9lZ4LvW7nYC.Vq/QfcgR.cNqfymKmrH/h92QAqJt0OCF56h/"
hash2 = "Ue2qFwq/3O.Yg9pxGBGmsdPe36TQImsHD.asr5innNv8G8i202G7xOh06/uu25XPHjPJ1LxjF7MSPM9S3pLse/"
hash3 = "PeAzz2i9WCIxRQydwMQUaBsYSmB/mhHMfkqvuHrfGWQ4BpKKgnvvMlrO0Z3y2KRtBOSyxavv0FvnvCx3zXxP0"
salts = ["$6$EIPKy0ixJFya3SZJ", "$6$lZQBku5UUMxdrSTJ", "$6$oK3qy6RoJiJQBimi"]

#salt1 = "$6$EIPKy0ixJFya3SZJ"
#salt2 = "$6$lZQBku5UUMxdrSTJ"
#salt3 = "$6$oK3qy6RoJiJQBimi"	

def password():
		usernames = ["good", "better", "best"]
		for j in usernames:	
			for i in range(0, 10):
				password = str(i) + str(i) + str(i)
				pattern_1 = str(password) + str(j[::-1])
				pattern_2 = str(j[::-1]) + str(password)
				print("Pattern_1 Passwords", pattern_1, "--------------""Pattern_2 Passwords", pattern_2)

		x = crypt.crypt(pattern_1)
		z = crypt.crypt(pattern_2)
		for k in range(0, 1000000):
			for salt in salts:
				x = crypt.crypt(str(x), salt)
				z = crypt.crypt(str(z), salt)
				if k == x:
					print("Match Found Pattern_1")
					print(x)
					break
				if k == x:
					print("Match Found Pattern_1")
					print(x)
					break
				if k == x:
					print("Match FoundPattern_1")
					print(x)
					break
				elif k == z:
					print("Match Found Pattern_2")
					print(z)
					break
				elif k == z:
					print("Match Found Pattern_2")
					print(z)
					break
				elif k == z:
					print("Match Found Pattern_2")
					print(z)
					break				
password()
