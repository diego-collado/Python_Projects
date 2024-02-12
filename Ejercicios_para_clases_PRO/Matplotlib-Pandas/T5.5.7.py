'''
Utilizar el fichero csv: company_sales_data.csv
Lee el beneficio total de cada mes y muéstralo utilizando el histograma para ver los rangos de beneficio más comunes.
'''
import matplotlib.pyplot as plt # Importación del módulo Matplotlib, submódulo Pyplot
import pandas as pd # Importación del módulo Pandas


# Lectura de dataframe desde CSV
df = pd.read_csv('data/company_sales_data-221102-123259.csv')

# Conversión de datos del dataframe de las columnas solicitadas: producto + mes del año
total= df['total_profit'].tolist()
rango_beneficios = [100000, 150000, 200000, 250000, 300000, 350000]

# Impresión de datos: beneficios -------------------------
plt.title('---- Beneficios totales mensuales ---- ') # título

plt.hist(total, rango_beneficios, label='Beneficios')

plt.legend(loc="upper left") # leyenda

# labels y título
plt.xlabel('Beneficio en $ (dólares americanos)')
plt.ylabel('Beneficio actual en $ (dólares americanos)')

plt.title('---- Comparativa de beneficios ---- ')

plt.xticks(rango_beneficios) # se colocan el rango de beneficios en el eje X

# mostrado de datos en pantalla
plt.show()