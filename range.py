# this program checks whether a given number lies between
#two given numbers
def num_check(n,s,e):
        if e == s:
                print ('Nothing in between')
                return None
        elif s<e :
                if n<s or n>e:
                        print ('Not in range')
                        return False
                else:
                        print ('In range')
                        return True

        elif s>e:
                if n<e or n>s:
                        print ('Not in range')
                        return False
                else:
                        print ('In range')
                        return True

	
