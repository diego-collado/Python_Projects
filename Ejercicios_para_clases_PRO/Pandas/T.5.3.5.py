'''
Cuenta el total de coches por empresa
'''

import pandas as pd

# lectura CSV + carga de valores
auto_data = pd.read_csv("data/Automobile_data-221102-123259.csv", na_values= {
    'index': ["?","n.a"], 'company': ["?","n.a"], 'body-style': ["?","n.a"],
    'wheel-base': ["?","n.a"], 'length': ["?","n.a"], 'engine-type': ["?","n.a"],
    'num-of-cylinders': ["?","n.a"], 'horsepower': ["?","n.a"],
    'average-mileage': ["?","n.a"], 'price': ["?","n.a"]
})

# impresión de número total de vehículos por compañía, sin el resto de los datos
print(auto_data['company'].value_counts())