'''
Utilizar el fichero csv: company_sales_data.csv
Lee los datos de ventas de jabón de baño de todos los meses y muéstralos mediante un gráfico de barras.
Guarda este gráfico en tu disco duro.
'''
import matplotlib.pyplot as plt # Importación del módulo Matplotlib, submódulo Pyplot
import pandas as pd # Importación del módulo Pandas


# Lectura de dataframe desde CSV
df = pd.read_csv('data/company_sales_data-221102-123259.csv')

# Conversión de datos del dataframe de las columnas solicitadas: producto + mes del año
ejex_mes = df['month_number'].tolist()
gel_banio = df['bathingsoap'].tolist()

# Impresión de datos por producto ------------------------- [a-0.25 for a in ejex_mes] separación a cada lado del eje Y
plt.bar(ejex_mes, gel_banio, width=0.6, color='#619cff', align='center') # gráfico de barras

plt.legend(loc="upper left") # leyenda

# labels y título
plt.xlabel('Mes del año')
plt.ylabel('Nº uds. vendidas')

plt.title('---- Ventas mensuales: Crema y jabón de cara ---- ') # título

plt.xticks(ejex_mes) # se colocan los meses en el eje X

# rejilla fondo
plt.grid(True, linestyle='--', linewidth=1)

# grabación en disco duro
plt.savefig('data/ventas_gel-baño.png', dpi=300)

# mostrado de datos en pantalla
plt.show()