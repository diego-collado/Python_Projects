'''
Analiza el siguiente JSON para obtener todos los valores de una clave 'nombre':

[
   {
      "id":1,
      "name":"name1",
      "color":[
         "red",
         "green"
      ]
   },
   {
      "id":2,
      "name":"name2",
      "color":[
         "pink",
         "yellow"
      ]
   }
]
'''
import json

sampleJson = [{"id":1, "name":"name1", "color":["red", "green"]},
              {"id":2, "name":"name2", "color":["pink", "yellow"]}
              ]

data = []

try:
    data = json.loads(sampleJson)
except Exception as exc:
    print("Se ha producido una excepción: ", exc)

print([item.get('name')for item in data])