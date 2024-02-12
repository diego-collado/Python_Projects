'''
Convierte el siguiente objeto vehículo en JSON:
import json

class Vehicle:
    def __init__(self, name, engine, price):
        self.name = name
        self.engine = engine
        self.price = price

vehicle = Vehicle("Toyota Rav4", "2.5L", 32000)
'''
import json
from json import JSONEncoder

class Vehicle:
    def __init__(self, name, engine, price):
        self.name = name
        self.engine = engine
        self.price = price

class VehicleEncoder(json.JSONEncoder):
    def jsonDefault(object):
        return object.__dict__

vehicle = Vehicle("Toyota Rav4", "2.5L", 32000)

vehicleJson = json.dumps(vehicle, indent=4, cls=VehicleEncoder)#cls=conversión JSON a objeto Vehicle
print(vehicleJson)