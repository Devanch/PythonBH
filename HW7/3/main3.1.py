import yaml
from pprint import pprint

with open('simple.yaml') as f:
    templates = yaml.safe_load(f)

pprint(templates)