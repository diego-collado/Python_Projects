'''
PrettyPrint el siguiente JSON con nivel de sangría 2 y los separadores clave-valor deben ser (",", " = ").
sampleJson = {"key1": "value1", "key2": "value2"}
'''

import json

sampleJson = {"key1": "value1", "key2": "value2"}
ppJson = json.dumps(sampleJson, indent=2, separators=(",", " = "))
print(ppJson)