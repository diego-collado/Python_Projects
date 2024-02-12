'''
Utilizar el fichero csv: company_sales_data.csv
Lee todos los datos de ventas de productos y mostrarlos mediante un gráfico multilínea.
Muestra el número de unidades vendidas por mes para cada producto utilizando gráficos multilínea
(es decir, una línea de trazado separada para cada producto).
'''
import matplotlib.pyplot as plt # Importación del módulo Matplotlib, submódulo Pyplot
import pandas as pd # Importación del módulo Pandas

# Lectura de dataframe desde CSV
df = pd.read_csv('data/company_sales_data-221102-123259.csv')

# Conversión de datos del dataframe de las columnas solicitadas: productos + mes del año
ejex_mes = df['month_number'].tolist()

crema_cara = df['facecream'].tolist()
jabon_cara = df['facewash'].tolist()
crema_dientes = df['toothpaste'].tolist()
gel_banio = df['bathingsoap'].tolist()
champu = df['shampoo'].tolist()
hidratante = df['moisturizer'].tolist()

# Impresión de datos por producto -------------------------
plt.plot(ejex_mes, crema_cara, color='b', label = 'Venta crema de cara', linewidth='3', marker='o')
plt.plot(ejex_mes, jabon_cara, color='g', label = 'Venta jabón para la cara', linewidth='3', marker='o')
plt.plot(ejex_mes, crema_dientes, color='r', label = 'Venta pasta de dientes', linewidth='3', marker='o')
plt.plot(ejex_mes, gel_banio, color='c', label = 'Venta gel de baño', linewidth='3', marker='o')
plt.plot(ejex_mes, champu,color='m', label = 'Venta champú', linewidth='3', marker='o')
plt.plot(ejex_mes, hidratante, color='y', label = 'Venta hidratante', linewidth='3', marker='o')

# leyenda
plt.legend(loc="upper left")

# labels y título
plt.xlabel('Mes del año')
plt.ylabel('Nº uds. ventas')

plt.title('---- Ventas mensuales por producto ---- ') # título

plt.xticks(ejex_mes) # se colocan los meses en el eje X
plt.yticks([1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, 11000, 12000, 13000, 14000,
            15000, 16000]) # se colocan los totales en el eje Y

# mostrado de datos en pantalla
plt.show()