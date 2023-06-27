#define the dictionary teams
teams = {'baseball' : 'Tigers','football' : 'Lions',
         'basketball' : 'Pistons','hockey': 'Red Wings'}

#calling within the dictionary
def main():
	search='nq'
	while search!='quit':
		search = input ('What sport key are you looking for ?')
		if search != 'quit':
			if search in teams.keys():
				print ("The sport ",search,' Associated team is ',teams[search])
			else:
				print ("No entry for that sport")
				addq = input('Would youlike to add one (yes/no) ?')
				if addq !='no':
					spname=input('What team name should be associated ?')
					teams[search]=spname
			print("\n Current Dictionary \n",teams)


if __name__ =='__main__':
        main()
