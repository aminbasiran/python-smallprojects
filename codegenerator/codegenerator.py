from operator import truediv
import random


lowercharacters = "qwertyuiopasdfghjklzxcvbnm"
uppercharacters = "QWERTYUIOPASDFGHJKLZXCVBNM"
numbers = "1234567890"
special = "!@#$%^&*()_+-="

numOfPasswords= int(input("how many passwords would you like us to generate"))
numOfChar = int(input("how many characters would you like your passwords to be"))
pick_lowercharacters = str(input("include lowercase chars?"))
pick_uppercharacters = str(input("include uppercase chars?"))
pick_numbers = str(input("include numbers?"))
pick_specials = str(input("include specials?"))


all = ""

if (pick_uppercharacters == "yes"):
    all = all + uppercharacters
if (pick_lowercharacters == "yes"):
    all = all + lowercharacters
if (pick_numbers == "yes"):
    all = all + numbers
if (pick_specials == "yes"):
    all = all + special


for x in range(0,numOfPasswords):
    # password = random.sample(lowercharacters+uppercharacters+numbers+special,k=numOfChar)
    password = random.sample(all,k=numOfChar)
    print("".join(password))