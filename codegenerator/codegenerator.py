import random

characters = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890!@#$%^&*()-=_+[]}{;':/,./<>"

numOfPasswords= int(input("how many passwords would you like us to generate"))
numOfChar = int(input("how many characters would you like your passwords to be"))

for x in range(0,numOfPasswords):
    mypassword= ""

    password = str(random.sample(characters,k=numOfChar))
    mypassword = mypassword +password
    a= ""
    for i in mypassword:
        a = a+str(i[0]).upper()
    print(a)

# characters = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890!@#$%^&*()-=_+[]}{;':/,./<>"

# numOfPasswords= int(input("how many passwords would you like us to generate"))
# numOfChar = int(input("how many characters would you like your passwords to be"))

# for x in range(0,numOfPasswords):
#     mypassword=""
#     password = str(random.choices(characters,k=numOfChar))
#     mypassword = mypassword +password
#     mystring = ''.join(map(str,mypassword))

#     print(mystring)