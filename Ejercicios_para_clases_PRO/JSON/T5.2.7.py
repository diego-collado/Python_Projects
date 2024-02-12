'''
Convierte el siguiente JSON en un objeto de vehículo:

{"name": "Toyota Rav4", "engine":"2.5L", "price":32000}
Por ejemplo, deberíamos ser capaces de acceder al Objeto Vehículo utilizando el operador punto así:
    vehicleObj.name, vehicleObj.engine, vehicleObj.price
'''
import json
class Vehicle:
    def __init__(self, name, engine, price):
        self.name = name
        self.engine = engine
        self.price = price

def vehicleDecoder(object):
    return Vehicle(object['name'], object['engine'], object['price'])

vehicleObj = json.loads('{"name": "Toyota Rav4", "engine":"2.5L", "price":32000}', object_hook=vehicleDecoder)

print(vehicleObj.name, vehicleObj.engine, vehicleObj.price)