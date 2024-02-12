'''
Utilizar el fichero csv: company_sales_data.csv
Lee todos los datos de las ventas de productos y muéstrelos mediante el diagrama de pila.
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

# Impresión de datos: ventas totales por producto ------------------------- [][] envío de datos
plt.plot([],[],color='c', label='Crema facial', linewidth=4)
plt.plot([],[],color='r', label='Jabón para la cara', linewidth=4)
plt.plot([],[],color='b', label='Crema de dientes', linewidth=4)
plt.plot([],[],color='g', label='Gel de baño', linewidth=4)
plt.plot([],[],color='k', label='Champú', linewidth=4)
plt.plot([],[],color='y', label='Hidratante', linewidth=4)

# diagrama de datos (apilados)
plt.stackplot(ejex_mes, crema_cara, jabon_cara, crema_dientes, gel_banio, champu, hidratante,
              colors=['c', 'r', 'b', 'g', 'k', 'y'])

plt.legend(loc="upper left") # leyenda
# labels y título
plt.xlabel('Mes del año')
plt.ylabel('Nº uds. ventas')
plt.title('---- Ventas totals de productos ---- ') # título

plt.show() # mostrado de datos en pantalla