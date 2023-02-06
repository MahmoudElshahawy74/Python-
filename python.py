'''print("I'm mahmoud Kamal")
print("My birth date is 26 Jul 1996")
print("I graduated from faculty of CS , Cairo Uni 2020")
'''


###########################################################################
'''
current_year=2023
birth_year=int(input("Enter your birth year : "))
age=current_year-birth_year
#print(type(age))
print(f"you are {age} years old")# f-------------->format
'''
##########################################################################
'''
loan_value=int(input("Enter the loan value : "))
years=int(input("Enter the number of years : "))
installment=(loan_value+(loan_value*.12*years))/(years*12)
print(f"ypur monthly installment : {installment}")
'''
#########################################################################
'''Timer overflow'''
'''timer_resolution =int(input("Enter the timer resolution : "))
freq=int(input("Enter the frequency in MHZ: "))
prescalar=int(input("Enter the prescalar value : "))
ticktime=prescalar/(freq*(10**6))
overflow=(ticktime*(2**timer_resolution))*1000
print(f"ypur monthly installment : {overflow} milliseconds ")
'''
##############################################################################
'''login system'''
'''
usernames=['Ahmed','Ali','Amr']
passwords=[1394,6078,9345]
name=input("Enter your name : ")

if name in usernames:
    password=int(input("Enter your password  : "))
    if password ==passwords[usernames.index(name)]:
        print(f" welcome back , {name}")
    else:
        print("incorrect password !")
else:
    print("incorrect user name !")
'''
'''------------------------------------Dictionary-----------------------------------------'''
'''
dictionary={'Ahmed':1394,'Ali':6078,'Amr':9345}
name=input("Enter your name : ")

if name in dictionary:
    password=int(input("Enter your password  : "))
    if password ==dictionary[name]:
        print(f" welcome back , {name}")
    else:
        print("incorrect password !")
else:
    print("incorrect user name !")
'''
#########################################################################################################
'''sentence=input("enter the sentence : ")
rev_string=""

for ch in sentence:
    rev_string=ch+rev_string
print(f"the sentence after reversed : {rev_string}")
'''
##############################################################################################################

