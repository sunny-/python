def binary(s,e):
    last = s[-1]
    first = s[0]
    if len(s) == 2 and (s[0] == e or s[1] == e):
        return True
    else:
        mid = int(first+last+1)/2
        if e<= mid:
            last = mid
        else:
            first = mid






    
s=[1,3,5,6]
e=4
binary(s,e)
