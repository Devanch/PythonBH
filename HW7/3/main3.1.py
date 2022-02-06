import yaml
from pprint import pprint

data = {'age':45,'name':'Peter','children':[{'age':3,'name':'Alice'}],'married':True,'city':None}

with open("simple.yaml", "w") as json_file:
   yaml.dump(data, json_file, indent = 4)

with open('simple.yaml') as f:
    data_new = yaml.safe_load(f)

pprint(data_new)