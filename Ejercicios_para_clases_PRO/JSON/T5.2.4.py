'''
Ordena las claves JSON por orden alfabético y escribelas en un fichero.
sampleJson = {"id": 1, "name": "value2", "age": 29}
'''
import json

sampleJson = {"id": 1, "name": "value2", "age": 29}

with open("sampleJson.json",'w') as fichero:
    print(json.dumps(sampleJson, sort_keys=True, indent=4))