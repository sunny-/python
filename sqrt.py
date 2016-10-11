x = 0.1
ans = 0

if x<=0:
        print ('Not a positive number')
else:

        while ans*ans < x:
              ans=ans+1

        if ans*ans==x:
                print (ans)
        else:
                print ('Not a perfect square')
