'''
Utilizar el fichero csv: company_sales_data.csv
Lee los datos de las ventas de pasta de dientes de cada mes y muéstralos mediante un gráfico de dispersión (scatter).
Además, añade una cuadrícula en el gráfico.
El estilo de la cuadrícula debe ser "-".
'''
import matplotlib.pyplot as plt # Importación del módulo Matplotlib, submódulo Pyplot
import pandas as pd # Importación del módulo Pandas

# Lectura de dataframe desde CSV
df = pd.read_csv('data/company_sales_data-221102-123259.csv')

# Conversión de datos del dataframe de las columnas solicitadas: producto + mes del año
ejex_mes = df['month_number'].tolist()
crema_dientes = df['toothpaste'].tolist()

# Impresión de datos por producto -------------------------
plt.scatter(ejex_mes, crema_dientes, label = 'Venta pasta de dientes')

plt.legend(loc="upper left") # leyenda

# labels y título
plt.xlabel('Mes del año')
plt.ylabel('Nº uds. vendidas')

plt.title('---- Ventas mensuales: Pasta de dientes ---- ') # título

plt.xticks(ejex_mes) # se colocan los meses en el eje X

# rejilla fondo
plt.grid(True, linestyle='--', linewidth=1)

# mostrado de datos en pantalla
plt.show()