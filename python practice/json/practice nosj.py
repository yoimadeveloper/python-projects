import json


input = '''
[
    { "id": "001",
      "x": "2",
      "name": "Mohit"
    } , 
    {
        "id": "001",
        "x": "7",
        "name": "panwar"
    }
]'''

info = json.loads(input)
print('user count:', len(info))

for item in info:
    print('name', item['name'])
    print('id', item['id'])