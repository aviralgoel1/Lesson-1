#Ask for name
Forename=input("Forename:")
Validname=Forename.isalpha()
print(Validname)
Validname=Forename.isalpha()
Surname=input("Surname:")
#different types of names
computername=Surname.upper()+", "+Forename.capitalize()
print("you will be stored as, "+computername)
normalname=Forename.capitalize()+" "+Surname.capitalize()
print("Hello, "+normalname+"!")
#number of letter in name
forenamecount=len(Forename)
surnamecount=len(Surname)
print("Your name has " + str(surnamecount+forenamecount) + " letters")
#defining variables for interest
principle=input("How much would you like to borrow, "+Forename+"? ")
term=input("How many years do you need to pay back? ")
bankrate=4.25
print("The current interest rate is "+str(bankrate))
#calculating simple interest
return1=int(principle)*int(term)*bankrate
totinterest=return1/100
#informing about interest
print(normalname+", you will need to pay "+str(totinterest)+" interest in "+str(term)+" years")
totalpay=int(principle)+int(totinterest)
print("You will need to pay back £"+str(totalpay)+" in total")
monthlypay=totalpay/int(term)/12
#very polite threat
print("You better pay £"+str(monthlypay)+" on time every month!")
print(" Otherwise, we will rename you to "+(Forename[::-1])+" "+(Surname[::-1])+"!")