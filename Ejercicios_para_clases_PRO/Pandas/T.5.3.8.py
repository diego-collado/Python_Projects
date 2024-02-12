'''
Ordena todos los coches por la columna Precio.
'''
import pandas as pd

# lectura CSV + carga de valores
auto_data = pd.read_csv("data/Automobile_data-221102-123259.csv", na_values= {
    'index': ["?","n.a"], 'company': ["?","n.a"], 'body-style': ["?","n.a"],
    'wheel-base': ["?","n.a"], 'length': ["?","n.a"], 'engine-type': ["?","n.a"],
    'num-of-cylinders': ["?","n.a"], 'horsepower': ["?","n.a"],
    'average-mileage': ["?","n.a"], 'price': ["?","n.a"]
})

# ordenación de valores por precio
auto_data = auto_data.sort_values(by=['price','horsepower'], ascending=False)
print(f"{auto_data.head(5)}") # impresión de los 5 primeros valores