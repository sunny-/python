# Print different words based on given conditions
for i in range (1,51):
	if i%3 == 0 and i%5!=0:
		print('fizz')
	elif i%5 == 0 and i%3 != 0 :
		print('buzz')
	elif i%3 == 0 and i%5 == 0 :
		print('fizzbuzz')
	else:
		print(i)
