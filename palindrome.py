# Checks whether a given number is palindrome.
# d=''
# c=input('Enter the word')
# for i in range(len(c)-1,-1,-1):
# 	d=d+c[i]
# if d == c :
# 	print ('its a palindrome')
# else:
# 	print ('its not a palindrome')


def is_palindrome():
	d=''
	c=input('Enter the word')
	for i in range(len(c)-1,-1,-1):
		d=d+c[i]
	if d == c :
		print ('its a palindrome')
		return True
	else:
		print ('its not a palindrome')
		return False
