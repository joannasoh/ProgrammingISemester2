import datetime;

now = datetime.datetime.now()
userInput = raw_input("Please enter your birthday in YYYY/MM/DD format: ")

if (len(userInput) == 10):
	userDay = userInput [9:10]
	userMonth = userInput[6:7]
	userYear = userInput [0:4]
	dage = now.day - int(userDay)
	mage = now.month - int(userMonth)
	yage = now.year - int(userYear)
	timeDif = (yage * 365 + mage * 30.4 + dage)
	endYage = int(timeDif/365)
	endMage = int(((timeDif - endYage * 365)-((timeDif - endYage *365)% 30.4))/30.4)
	
	endDage = int(timeDif - endYage *365 - endMage*30.4 )

	print"You are", endYage , " years", endMage, " months and ", endDage, "days old"
	
	endFullMonth = int(endYage *12 + endMage)
	
	endFullDay = int((endYage * 365) + (endMage * 30.4) + endDage)
	
	endMinute = int(endFullDay *1440)
	
	endSecond = int(endMinute *60)
	
	
	print "You are", endFullMonth, "months old"
	print "You are", endFullDay,"days old"
	print "You are about", endMinute, "minutes old"
	print "You are about", endSecond, "seconds old"
	
	
else : 
	print "Your input is wrong. Try again."
	
