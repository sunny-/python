def prime(x):
	i=2
	if x < 2 or isinstance (x,float):# checks for float or negative
		return False
	elif x == 2 or x == 3: # return prime if x is 2 or 3
		return True
	else:
		while i <= x: #checks primarity for other numbers
			if x%i == 0:
				return False
				break
			i = i+1
		else:
			return True


