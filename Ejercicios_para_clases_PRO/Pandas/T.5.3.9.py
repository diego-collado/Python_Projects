'''
Concatena dos dataframes utilizando las siguientes condiciones:
    - GermanCars = {'Company': ['Ford', 'Mercedes', 'BMV', 'Audi'], 'Price': [23845, 171995, 135925 , 71400]}
    - JapaneseCars = {'Company': ['Toyota', 'Honda', 'Nissan', 'Mitsubishi '], 'Price': [29995, 23600, 61500 , 58900]}
'''

import pandas as pd

# preparación de dataframes
GermanCars = {'Company': ['Ford', 'Mercedes', 'BMV', 'Audi'], 'Price': [23845, 171995, 135925 , 71400]}
JapaneseCars = {'Company': ['Toyota', 'Honda', 'Nissan', 'Mitsubishi '], 'Price': [29995, 23600, 61500 , 58900]}

# construcción del objeto dataframe desde el diccionario
germanCarsDf = pd.DataFrame.from_dict(GermanCars)
japaneseCarsDf = pd.DataFrame.from_dict(JapaneseCars)

# concatenación de ambos dataframes
conDF = pd.concat([germanCarsDf, japaneseCarsDf],keys=['Germany', 'Japan'])
print(f"{conDF}")