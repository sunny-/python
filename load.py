import json
#import io
#path = io.open('sample.txt',"r",encoding ='utf-8')
path = open('sample.txt')
records = [json.loads(line) for line in path]

time_zones = [rec['tz'] for rec in records if 'tz' in rec]


#
#def tz_counts(seq):
#    dics = {}
#    for i in seq:
#        if i in dics:
#            dics[i] += 1
#
#        else:
#            dics[i] = 1
#    return dics
#
#counts = tz_counts(time_zones)
#print (counts)



def top_counts(count_dict,n=10):

    value_key_pairs = [(count,tz)for tz, count in count_dict.items()]
    value_key_pairs.sort()
    return value_key_pairs[-n:]

    
##from collections import Counter
##
##counts = Counter(time_zones)
##
##print(counts.most_common(10))


from pandas import DataFrame, Series

import pandas as pd
frame = DataFrame(records)
#print (frame)

#print(frame['tz'][:10])


tz_counts = frame['tz'].value_counts()
#print (tz_counts[:10])

clean_tz = frame['tz'].fillna('Missing')

clean_tz[clean_tz == ''] = 'Unknown'

tz_counts = clean_tz.value_counts()

print tz_counts[:10]































