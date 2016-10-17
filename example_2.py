# Finds number of chicks & pigs, if total
# head count and leg count given.

##def count(head,legs):
##        for chicks in range (1,head+1):
##                pigs = head - chicks
##                if (2*chicks) + (4*pigs) == legs:
##                        return print('Number of chicks are ' + str(chicks) + ' and number of pigs are ' + str(pigs)) 
##                        break
##        return print ('no solution')


def count(head,legs):
        for chicks in range (1,head+1):
                pigs = head - chicks
                if (2*chicks) + (4*pigs) == legs:
                        return [chicks,pigs]
        return[None,None]


def barn():
        head = int (input ('enter number of heads'))
        legs = int (input ('enter number of legs'))
        chicks,pigs = count(head,legs)
        if chicks == None :
        	print ('no solution')
        else:
        	print ('number of pigs ' + str (pigs))
        	print ('number of pigs ' + str (chicks))

