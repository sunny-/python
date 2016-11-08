## def binary(s,e):
##    last = s[-1]
##    first = s[0]
##    if len(s) == 2 and (s[0] == e or s[1] == e):
##        return True
##    else:
##        mid = int(first+last+1)/2
##        if e<= mid:
##            last = mid
##        else:
##            first = mid





def selection_sort(l):
    for i in range(0,len(l)):
        min_value = l[i]
        min_index = i
        for j in range(i+1,len(l)):
            if min_value > l[j]:
                min_value = l[j]
                min_index = j
        temp = l[i]
        l[i] = l[min_index]
        l[min_index] = temp
        print ('partially sorted list = ' , l)
    

l = [21,6,45,87,12,1,37]
selection_sort(l)
print ('Sorted list =', l)

