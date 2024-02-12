'''
Accede a la clave anidada "salario" del siguiente JSON:

    import json

    sampleJson = """{
       "company":{
          "employee":{
             "name":"emma",
             "payble":{
                "salary":7000,
                "bonus":800
             }
          }
       }
    }"""
'''

import json
sampleJson = """{
       "company":{
          "employee":{
             "name":"emma",
             "payble":{
                "salary":7000,
                "bonus":800
             }
          }
       }
    }"""

data = json.loads(sampleJson)
print(data['company']['employee']['payble']['salary'])