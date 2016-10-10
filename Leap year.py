# Finding if a given year is a leap year or not
##
##y = 1600
##if y%4 == 0:
##    if y%100 == 0:
##        if y%400 == 0:
##            print ('Leap year')
##        else:
##            print ('Not a leap year')      
##    else:
##        print ('Leap year')
##else:
##    print ('Not a leap year')



y = 1664
if y%4 == 0 and y%100 != 0:
    print ('Leap year')
elif y%4 == 0 and y%100 == 0 and y%400 == 0:
    print ('Leap year')
else:
    print ('Not a leap year')

