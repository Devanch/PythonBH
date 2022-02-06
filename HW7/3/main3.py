import json

a = {'age':45,'name':'Peter','children':[{'age':3,'name':'Alice'}],'married':True,'city':None}

with open("mains.json", "w") as json_file:
   json.dump(a, json_file, indent = 4)

with open("mains.json", "r") as json_file:
    b = json.load(json_file)

print(b)