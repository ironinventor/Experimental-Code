#Python password generator script using basic principles

# imports
import random


# the following is user input
amountoftimes = input("How many passwords would you like generated? ") 
Passcode_length = input("What's the length of characters in your password? ") 
lowercasetimes = input("Lowercase letters? ")
numbertimes = input("Numbers? ")
upcasetimes = input("Upper case? ")

# works out passcpasscoode
lowercase = "abcdefghijklmnopqrstuvwxyz" * lowercasetimes
number = "0123456789" * numbertimes
upcase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ" * upcasetimes

if (lowercasetimes == 0):
	alphabet = number + upcase
elif (numbertimes == 0):
	alphabet = upcase + lowercase
elif (upcasetimes == 0):
	alphabet = number + lowercase
else:
	alphabet = lowercase + number + upcase

# creates the file 'passwords.txt' for writing
file = open("passwords.txt","w")

# generates the passwords
for i in range(amountoftimes):
	mypw = ""
	for i in range(Passcode_length):
	    next_index = random.randrange(len(alphabet))
	    mypw = mypw + alphabet[next_index]

	file.write(mypw + '\n') # writes the password in the file

file.close() # closes the file when complete and saves to file
