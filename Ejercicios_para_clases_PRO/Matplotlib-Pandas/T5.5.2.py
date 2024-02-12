'''
Utilizar el fichero csv: company_sales_data.csv
Obtenga el beneficio total de todos los meses y muestre un gráfico de líneas con las siguientes propiedades de estilo:
    - Estilo de línea punteada y el color de la línea debe ser rojo (dashed / --)
    - Mostrar la leyenda en la parte inferior derecha (lower right)
    - Nombre de la etiqueta X = Número de mes
    - Nombre de la etiqueta Y = Número de unidades vendidas
    - Añadir un marcador de círculo.
    - El ancho de la línea debe ser 3
'''
import matplotlib.pyplot as plt # Importación del módulo Matplotlib, submódulo Pyplot
import pandas as pd # Importación del módulo Pandas

# Lectura de dataframe desde CSV
df = pd.read_csv('data/company_sales_data-221102-123259.csv')

# Conversión de datos del dataframe de las columnas solicitadas
ejex_mes = df['month_number'].tolist()
ejey_total= df['total_profit'].tolist()

# Impresión de datos -------------------------
# datos, incluyendo la leyenda
plt.plot(ejex_mes, ejey_total, linestyle = 'dashed', color = 'r', label = 'Datos ganancias ultimo año',
         linewidth='3', marker='o', markerfacecolor='k')
plt.legend(loc='lower right') # colocación de la leyenda

#labels y título
plt.xlabel('Mes del año')
plt.ylabel('Beneficio total')

plt.title('---- Beneficios totales mensuales ---- ') # título

plt.xticks(ejex_mes) # se colocan los meses en el eje X
plt.yticks([100000, 200000, 300000, 400000, 500000]) # se colocan los totales en el eje Y

# mostrado de datos en pantalla
plt.show()