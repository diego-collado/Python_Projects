'''
Limpia el conjunto de datos y actualiza el archivo CSV.
Reemplaza todos los valores de las columnas que contengan ?, n.a, o NaN.
'''
import pandas as pd

# lectura CSV + reemplazamiento de valores
auto_data = pd.read_csv("data/Automobile_data-221102-123259.csv", na_values= {
    'index': ["?","n.a"], 'company': ["?","n.a"], 'body-style': ["?","n.a"],
    'wheel-base': ["?","n.a"], 'length': ["?","n.a"], 'engine-type': ["?","n.a"],
    'num-of-cylinders': ["?","n.a"], 'horsepower': ["?","n.a"],
    'average-mileage': ["?","n.a"], 'price': ["?","n.a"]
})

print(auto_data)

# escritura de CSV
auto_data.to_csv('data/Automobile_data-new.csv')