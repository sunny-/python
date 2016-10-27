##1. Write a program to enter the numbers till the user wants and
##at the end it should display the count of positive, negative and
##zeros entered. Use functions.

def f(m):
    
    positive = 0 # use three counters to count +ve, -ve, 0
    negative = 0
    zero = 0
   
    while m >= 1: # if user gives input for m times, exit and print the result.

        n = int(input('enter a number')) # Get an input from a user

        if n > 0: # check the given number and increment a counter.
            positive += 1

        elif n < 0:
            negative += 1

        else:
            zero += 1
        m = m-1

    print ('positive numbers ' + str (positive))

    print ('negative numbers ' + str (negative))

    print ('zeroes ' + str (zero))
            
            

##2. Write a program for a matchstick game being played between
##the computer and a user. Your program should ensure that the
##computer always wins. Rules for the game are as follows:
##
##− There are 21 matchsticks.
##− The computer asks the player to pick 1, 2, 3, or 4 matchsticks.
##
##− After the person picks, the computer does its picking.
##
##− Whoever is forced to pick up the last matchstick loses the game.

def match_stick():
    c = 0 # input from a computer
    u = 0 # input from a user
    total = 0 # sum of c+u
    user_pick = 0 # number of pics by user
    com_pick = 0 # number of pics by computer
    while total <= 21:
        u = int(input('pick match stick from 1 to 4 ')) ##Ask a user to pick a number u from 1 to 4
        user_pick += 1 ##for every user pick increment user_pick by 1
        total = total + u
        if total < 21:
            c = 5-u ##Once the user picks, computer picks number 5-u
            com_pick += 1 ##for every computer pick increment com_pick by 1
            total = total + c
        else: continue

    if user_pick > com_pick:
        print ("computer wins")
        

    else:
        print ("user wins")



##3. Write a recursive function which returns the sum of digits of a number.

                
def sum_digits(n):
    s= str(n)
    if len(s) == 1:
        return int(s[0])

    else:
        return int(s[0]) + sum_digits(int(s[1:])) 
        
    




        
