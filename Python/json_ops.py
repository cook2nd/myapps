import json

with open('ex1.json', 'r') as f:
    data = json.loads(f.read())

# print(data)
# print(type(data))

data_output = []
for e in data:
    # print(e)
    # print(e.get('classes'))
    # print(e.get('data').get('id'))
    # if print(e.get('classes')) != 'green diamond' or print(e.get('data').get('id')) == 'po1':
    if e.get('classes') != 'green diamond' or e.get('data').get('id') == 'po1':
        data_output.append(e)

with open('ex1.json', 'w') as f:
    f.write(json.dumps(data_output, indent=2))
