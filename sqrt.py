#this program gives square root of a given number.
def sqrt(x):
        '''The function give square-rrot of given number x'''
        ans = 0

        if x<=0:
                print ('Not a positive number')
                return None
        else:

                while ans*ans < x:
                      ans = ans+1

                if ans*ans == x:
                        return ans
                else:
                        print ('Not a perfect square')
                        return None
