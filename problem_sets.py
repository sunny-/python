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

## ***pseudo code***
    



##3. Write a recursive function which returns the sum of digits of a  number.





## 4. A palindromic number reads the same both ways.
##Find the largest palindrome made from the product of two 2-digit numbers
##(Hint- Ans is 9009 = 91 × 99 )
