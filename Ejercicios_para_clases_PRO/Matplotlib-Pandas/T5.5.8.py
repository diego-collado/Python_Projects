'''
Utilizar el fichero csv: company_sales_data.csv
Calcula los datos de ventas totales del último año para cada producto y muéstralos mediante un gráfico circular.
Nota: En el gráfico circular muestra el número de unidades vendidas por año para cada producto en porcentaje.
'''
import matplotlib.pyplot as plt # Importación del módulo Matplotlib, submódulo Pyplot
import pandas as pd # Importación del módulo Pandas

# Lectura de dataframe desde CSV
df = pd.read_csv('data/company_sales_data-221102-123259.csv')

# Conversión de datos del dataframe de las columnas solicitadas: producto + mes del año
labels = ['Crema facial', 'Lavado de cara', 'Pasta de dientes', 'Gel de baño', 'Shampoo', 'Moisturizer']
salesData   = [df ['facecream'].sum(), df ['facewash'].sum(), df ['toothpaste'].sum(),
         df ['bathingsoap'].sum(), df ['shampoo'].sum(), df ['moisturizer'].sum()]

# Impresión de datos: ventas totales por producto -------------------------
plt.axis("equal")
plt.pie(salesData, labels=labels, autopct='%1.1f%%')

plt.legend(loc='lower right') # leyenda
plt.title('------ Datos de Venta ------')

plt.show() # mostrado de datos en pantalla