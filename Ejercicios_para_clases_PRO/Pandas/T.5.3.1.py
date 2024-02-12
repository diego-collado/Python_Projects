'''
A partir del conjunto de datos dado, imprime las cinco primeras y últimas filas.
'''

import pandas as pd

# lectura CSV + carga de valores
auto_data = pd.read_csv("data/Automobile_data-221102-123259.csv", na_values= {
    'index': ["?","n.a"], 'company': ["?","n.a"], 'body-style': ["?","n.a"],
    'wheel-base': ["?","n.a"], 'length': ["?","n.a"], 'engine-type': ["?","n.a"],
    'num-of-cylinders': ["?","n.a"], 'horsepower': ["?","n.a"],
    'average-mileage': ["?","n.a"], 'price': ["?","n.a"]
})

print(f"{auto_data.head(5)}")# impresión de 5 primeros valores
print(f"{auto_data.tail(5)}")# impresión de 5 últimos valores