#generate a random number 
#Get a guess from user and compare with your number
#keep asking till match is find
import random
c= random.randrange(1,10)

d = 0

while c!=d:
	d = int(input("Guess the number "))

print ("Right guess, your number is "+ str(d) )
