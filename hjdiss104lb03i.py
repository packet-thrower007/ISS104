hp=float(input("How much per hour?"))
hr=float(input("How many hours a week?"))
ot = input("Does overtime count? (yes or no)")


def calpay(pay, hours, overtime):
	if (overtime=='yes' and hours >40):
		ap = 52*((pay*40)+ (1.5*pay*(hours-40)))
		print("hello")
	else:
		ap = 52*(pay*hours)
	return ap

if __name__ =='__main__':
        print (calpay(hp, hr, ot))
