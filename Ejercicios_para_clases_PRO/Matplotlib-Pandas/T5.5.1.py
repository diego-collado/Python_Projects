'''
Utilizar el fichero csv: company_sales_data.csv
Lee el beneficio total de todos los meses y muéstralo mediante un gráfico de líneas.
Se proporcionan los datos del beneficio total de cada mes.
El gráfico de líneas generado debe incluir las siguientes propiedades:
    - Nombre de la etiqueta X = Número de mes (month_number)
    - Nombre de la etiqueta Y = Beneficio total (total_profit)
'''
import matplotlib.pyplot as plt # Importación del módulo Matplotlib, submódulo Pyplot
import pandas as pd # Importación del módulo Pandas

# Lectura de dataframe desde CSV
df = pd.read_csv('data/company_sales_data-221102-123259.csv')

# Conversión de datos del dataframe de las columnas solicitadas
ejex_mes = df['month_number'].tolist()
ejey_total= df['total_profit'].tolist()

# Impresión de datos -------------------------
# datos
plt.plot(ejex_mes, ejey_total)

#etiquetas y título
plt.xlabel('Mes del año')
plt.ylabel('Beneficio total')

plt.title('---- Beneficios totales mensuales ---- ') # título

plt.xticks(ejex_mes) # se colocan los meses en el eje X
plt.yticks([100000, 200000, 300000, 400000, 500000]) # se colocan los totales en el eje Y

# mostrado de datos en pantalla
plt.show()