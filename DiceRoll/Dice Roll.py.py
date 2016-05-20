import random

dicesides = "6"
dicenum = raw_input("How many dice do you want to roll? ")
if (not(dicenum.isdigit())):
	print ("This is not a valid input")

if(int(dicenum) <= 0 or int(dicenum) >= 100):
	print("This is not a valid number of dice")
	
	diceList = []
	dice = []
	resultNums = []
for i in range(0,int(dicesides)):
	dice.insert(i,i+1)
for i in range(0,int(dicenum)):
	diceList.insert(i,dice)
for i in range(0,len(diceList)):
	result = random.randint(0,int(dicesides)-1)
	resultnums.insert(i,diceList[i][result])
	print("Here are you lucky numbers: ", str(resultnums)[1:-1])