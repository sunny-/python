import json
import io
path = io.open('sample.txt',"r",encoding ='utf-8')

records = [json.loads(line) for line in path]

print(records[0])
print(len(records))

