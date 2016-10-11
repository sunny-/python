#Find sum of numbers which are divisible by 3 or 5
#euler-1
ans=0
for i in range(3,1000):
	if i%3==0 or i%5==0:
		ans+=i
print(ans)
