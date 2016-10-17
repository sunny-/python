#This program reverses the given word
# d=''
# c=input('Enter the word')
# for i in range(len(c)-1,-1,-1):
# 	d=d+c[i]
# print (d)


def rev():
	global d
	d=''
	global c
	c=input('Enter the word')
	for i in range(len(c)-1,-1,-1):
		d=d+c[i]
	return d
	
def is_palindrome():
	if c == d:
		print("Palindrome")
	else:
		print("not a palindrome")
        
