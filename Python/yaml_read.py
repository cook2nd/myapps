# Imports the YAML module for use in our script
import yaml

# Opens the file ex1.yaml, and loads the contents in the variable 'result'
with open('ex1.yaml') as f:
    result =  yaml.safe_load(f)
print(type(result))

paas_details = result.get('spec').get('obs').get('DETAILS')

print(paas_details)

for paas in paas_details:
    print(paas.keys())
    print(paas.values())
