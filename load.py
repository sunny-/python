import json
import io
path = io.open('sample.txt',"r",encoding ='utf-8')

records = [json.loads(line) for line in path]

time_zones = [rec['tz'] for rec in records if 'tz' in rec]



def tz_counts(seq):
    dics = {}
    for i in seq:
        if i in dics:
            dics[i] += 1

        else:
            dics[i] = 1
    return dics

counts = tz_counts(time_zones)




def top_counts(count_dict,n=10):

    value_key_pairs = [(count,tz)for tz, count in count_dict.items()]
    value_key_pairs.sort()
    return value_key_pairs[-n:]

    
    
