'''
Utilizar el fichero csv: company_sales_data.csv
Lee los datos de ventas de los productos crema facial y lavado de cara y muéstralos mediante el gráfico de barras.
El gráfico de barras debe mostrar el número de unidades vendidas por mes para cada producto.
Añade una barra distinta para cada producto en el mismo gráfico.
'''
import matplotlib.pyplot as plt # Importación del módulo Matplotlib, submódulo Pyplot
import pandas as pd # Importación del módulo Pandas

# Lectura de dataframe desde CSV
df = pd.read_csv('data/company_sales_data-221102-123259.csv')

# Conversión de datos del dataframe de las columnas solicitadas: producto + mes del año
ejex_mes = df['month_number'].tolist()
crema_cara = df['facecream'].tolist()
jabon_cara = df['facewash'].tolist()

# Impresión de datos por producto ------------------------- [a-0.25 for a in ejex_mes] separación a cada lado del eje Y
plt.bar([a-0.16 for a in ejex_mes], crema_cara, width=0.3, color='#619cff', align='edge') # gráfico de barras 1º producto
plt.bar([a+0.16 for a in ejex_mes], jabon_cara, width=0.3, color='#f8766d', align='edge') # gráfico de barras 2º producto

plt.legend(loc="upper left") # leyenda

# labels y título
plt.xlabel('Mes del año')
plt.ylabel('Nº uds. vendidas')

plt.title('---- Ventas mensuales: Crema y jabón de cara ---- ') # título

plt.xticks(ejex_mes) # se colocan los meses en el eje X

# rejilla fondo
plt.grid(True, linestyle='--', linewidth=1)

# mostrado de datos en pantalla
plt.show()