import random
import string
#Receive user input user name 
username = input("Please enter your full name:")

#validate username/remove any whitespace
username = username.replace(' ','')

print(username)

#retrieve 3 random digit from user name
def randStr(chars = string.ascii_uppercase + string.digits, N=10):
	return ''.join(random.choice(chars) for _ in range(N))
    
# random string with characters picked from 'abcdef123456'
#generate 4 digit random number
def randNumbers(N=10):
    digits=''
    listOfNumbers = [random.randint(1,9) for i in range(0,N)]
    for i in listOfNumbers:
        digits+=str(i)
    return digits


print("Your password is: " +randStr(chars=username,N=3) + randNumbers(4))