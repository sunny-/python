# Finds number of chicks & pigs, if total
# head count and leg count given.

##def count(head,legs):
##        for chicks in range (1,head+1):
##                pigs = head - chicks
##                if (2*chicks) + (4*pigs) == legs:
##                        return print('Number of chicks are ' + str(chicks) + ' and number of pigs are ' + str(pigs)) 
##                        break
##        return print ('no solution')


def count_cp(head,legs):
        for chicks in range (1,head+1):
                pigs = head - chicks
                if (2*chicks) + (4*pigs) == legs:
                        return [chicks,pigs]
        return[None,None]


def barn():
        head = int (input ('enter number of heads'))
        legs = int (input ('enter number of legs'))
        chicks,pigs = count_cp(head,legs)
        if chicks == None :
        	print ('no solution')
        else:
        	print ('number of pigs ' + str (pigs))
        	print ('number of pigs ' + str (chicks))



def count_cps(head,legs):
        for chicks in range(0,head+1):
                for pigs in range(0,head-chicks+1):
                        spiders=head-chicks-pigs
                        if (2*chicks) + (4*pigs) + (8*spiders) == legs:
                                return [chicks,pigs,spiders]
        return [None,None,None]


                

        
