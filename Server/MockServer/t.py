import json
data = open('test.txt','rb')
lines = data.readlines()
#print(lines)
D = str(lines).split('\n')
filtered = str(D).replace('', '')
#print(filtered)
Data = json.dumps(str(lines))
#print(type(Data))
#print(Data[0:100])

with open('data1.json','rb') as jsonF:
	data1 = json.load(jsonF)



import json

filename = 'test.txt'

commands = {}
with open(filename) as fh:
    for line in fh:
        command, description = line.strip().split(' ', 1)
        commands[command] = description.strip()

JsonData = json.dumps(filtered, indent=5, sort_keys=True)
#print(json.dumps(commands, indent=2, sort_keys=True))


with open('ResultJson.json', 'w') as json_file:  
    Result = json.dump(data1, json_file)
print(Result)



"""
with open('data1.json','r') as json_file:  
    data = json.load(json_file)
print(data[1:20])
"""
