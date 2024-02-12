'''
Combina dos dataframes utilizando la siguiente condición:
    --> Crea dos dataframes utilizando los siguientes dos Dicts, fusiónalos
    --> Añade el segundo dataframe como una nueva columna al primer dataframe

Dataframes:
    - Car_Price = {'Company': ['Toyota', 'Honda', 'BMV', 'Audi'], 'Price': [23845, 17995, 135925 , 71400]}
    - car_Horsepower = {'Company': ['Toyota', 'Honda', 'BMV', 'Audi'], 'horsepower': [141, 80, 182 , 160]}

'''
import pandas as pd

# preparación de dataframes
Car_Price = {'Company': ['Toyota', 'Honda', 'BMV', 'Audi'], 'Price': [23845, 17995, 135925 , 71400]}
car_Horsepower = {'Company': ['Toyota', 'Honda', 'BMV', 'Audi'], 'horsepower': [141, 80, 182 , 160]}

# construcción del objeto dataframe desde el diccionario
car_price = pd.DataFrame.from_dict(Car_Price)
car_hp = pd.DataFrame.from_dict(car_Horsepower)

# fusión de ambos dataframes, añadiendo el 1º como 1ª columna del nuevo dataframe
carsDF = pd.merge(car_price, car_hp, on='Company')

print(f"{carsDF}")