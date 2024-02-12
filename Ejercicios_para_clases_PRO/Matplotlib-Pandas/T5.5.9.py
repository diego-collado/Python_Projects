'''
Utilizar el fichero csv: company_sales_data.csv
Lee el jabón de baño de todos los meses y visualízalo utilizando el Subplot.
'''
import matplotlib.pyplot as plt # Importación del módulo Matplotlib, submódulo Pyplot
import pandas as pd # Importación del módulo Pandas

# Lectura de dataframe desde CSV
df = pd.read_csv('data/company_sales_data-221102-123259.csv')

# Conversión de datos del dataframe de las columnas solicitadas: producto + mes del año
eje_mes  = df ['month_number'].tolist()
jabon_banio = df['bathingsoap'].tolist()
jabon_cara = df['facewash'].tolist()

# Impresión de datos: ventas totales por producto -------------------------
fig, ax_array = plt.subplots(2, sharex=True)
# Producto 1, posición 0 del array
ax_array[0].plot(eje_mes, jabon_banio, color='b', label = 'Venta gel de baño', linewidth='3', marker='o')
ax_array[0].set_title('Venta gel de baño')

# Producto 1, posición 1 del array
ax_array[1].plot(eje_mes, jabon_cara, color='g', label = 'Venta gel para la cara', linewidth='3', marker='o')
ax_array[1].set_title('Venta gel para la cara')

# labels
plt.xticks(eje_mes)
plt.xlabel('Nº de mes')
plt.ylabel('Nº de uds. vendidas')

plt.show() # mostrado de datos en pantalla