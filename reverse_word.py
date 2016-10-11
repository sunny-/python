#This program reverses the given word
d=''
c=input('Enter the word')
for i in range(len(c)-1,-1,-1):
	d=d+c[i]
print (d)

