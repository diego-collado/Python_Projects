'''
Encuentra el coche con el precio más alto de precio de cada empresa
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

# búsqueda de precio máximo por compañía e impresión
price_auto_manuf = auto_manuf['price'].max()
print(f"{price_auto_manuf}")