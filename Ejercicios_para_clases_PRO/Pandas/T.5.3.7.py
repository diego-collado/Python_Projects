'''
Encuentra el kilometraje medio de cada empresa fabricante de automóviles.
'''

import pandas as pd

# lectura CSV + carga de valores
auto_data = pd.read_csv("data/Automobile_data-221102-123259.csv", na_values= {
    'index': ["?","n.a"], 'company': ["?","n.a"], 'body-style': ["?","n.a"],
    'wheel-base': ["?","n.a"], 'length': ["?","n.a"], 'engine-type': ["?","n.a"],
    'num-of-cylinders': ["?","n.a"], 'horsepower': ["?","n.a"],
    'average-mileage': ["?","n.a"], 'price': ["?","n.a"]
})

# selección de datos por compañía
auto_manuf = auto_data.groupby('company')

# búsqueda kilometraje medio por empresa fabricante e impresión de resultados
auto_manuf_Km = auto_manuf['average-mileage'].mean()
print(f"{auto_manuf_Km}")