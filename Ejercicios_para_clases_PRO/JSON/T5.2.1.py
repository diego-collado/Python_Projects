'''
Convierte el siguiente diccionario en formato JSON:
    data = {"key1" : "value1", "key2" : "value2"}
'''
#IMPORTS
import json

#MAIN
data = {"key1" : "value1", "key2" : "value2"}

#codificación de json a partir de diccionario
print(json.dumps(data))
