def name_checker():
	name_check = input("have you entered your names in the 2 txt files (name1.txt,name2.txt)")
	if(name_check.upper()=="Y"):
		print("good")
	elif(name_check.upper()=="N"):
		print("Do it")
		exit()
	else:
		print("incorrect input try again")
		name_checker()