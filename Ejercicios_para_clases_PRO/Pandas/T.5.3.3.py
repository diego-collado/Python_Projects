'''
Encuentra el nombre de la empresa del coche más caro.
Imprime el nombre de la empresa del coche más caro y su precio.
'''

import pandas as pd

# lectura CSV + carga de valores
auto_data = pd.read_csv("data/Automobile_data-221102-123259.csv", na_values= {
    'index': ["?","n.a"], 'company': ["?","n.a"], 'body-style': ["?","n.a"],
    'wheel-base': ["?","n.a"], 'length': ["?","n.a"], 'engine-type': ["?","n.a"],
    'num-of-cylinders': ["?","n.a"], 'horsepower': ["?","n.a"],
    'average-mileage': ["?","n.a"], 'price': ["?","n.a"]
})
# Búsqueda por precio máximo e impresión de los datos
auto_data = auto_data[['company','price']][auto_data.price == auto_data['price'].max()]
print(f"{auto_data} ")