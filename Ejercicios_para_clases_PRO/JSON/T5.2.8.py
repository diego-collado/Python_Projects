'''
Comprueba si el siguiente json es válido o inválido. Si es inválido corrígelo.
{
   "company":{
      "employee":{
         "name":"emma",
         "payble":{
            "salary":7000
            "bonus":800
         }
      }
   }
}
'''
import json
def comprobandoJson(data):
    try:
        json.loads(data)
    except ValueError as ve:
        return False
    return True

#MAIN
invalidJsonData = """{ "company":{ "employee":{ "name":"emma", "payble":{ "salary":7000 "bonus":800} } } }"""
esValido = comprobandoJson(invalidJsonData)
print("Archivo Válido: ", esValido)