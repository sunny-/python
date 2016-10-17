# If a five-digit number is input through the keyboard, write a
# program to calculate the sum of its digits.
##n= int(input('Enter five digit number '))
##
##Q=1
##R=1
##Sum = 0
##Q = n//10000
##R = n%10000
##Sum = Sum + Q
##Q = R//1000
##R = R%1000
##Sum = Sum + Q 
##Q = R//100
##R = R%100
##Sum = Sum + Q
##Q = R//10
##R = R%10
##Sum = Sum + Q
##Q = R
##Sum = Sum + Q
##print(Sum)



#********************** new method ************
sum = 0
num = 1238128
c=str(num)
for i in range (0,len(c)):
	sum = sum + int(c[i])
print (sum)
	
