'''
Creación de una hoja:

    - P: portrait - vertical
    - L: landscape - horizontal

    A4: 210x297mm
------------------------------
Instalación: pip install fpdf
Más info:
    · https://pypi.org/project/fpdf/
    · https://pyfpdf.readthedocs.io/en/latest/
'''

'''# PDF sencillo ----------------------------------------------------------------------------------
from fpdf import FPDF

pdf = FPDF(orientation='P', unit='mm', format='A4') # configuración de salida de PDF
pdf.add_page() # se añade la página al archivo resultante

pdf.output('ejemplo.pdf') # guardado del archivo PDF en el disco
'''

'''# PDF trazos & figuras --------------------------------------------------------------------------
from fpdf import FPDF

pdf = FPDF(orientation='P', unit='mm', format='A4')  # configuración de salida de PDF
pdf.add_page()  # se añade la página al archivo resultante

# jugando con las formas
pdf.rect(x=90, y=80, w=50, h=50)  # recta
pdf.line(50, 150, 190, 200)  # línea
pdf.dashed_line(15, 78, 80, 90, dash_length=10, space_length=6)  # línea entrecortada (dashed)
pdf.ellipse(x=10, y=15, w=100, h=80) # elipse

pdf.output('ejemplo_formas.pdf')  # guardado del archivo PDF en el disco'''

'''# PDF texto & imagen -------------------------------------------------------------------------------
from fpdf import FPDF

pdf = FPDF(orientation='P', unit='mm', format='A4') # configuración de salida de PDF
pdf.add_page() # se añade la página al archivo resultante

# texto
pdf.set_font('Arial', '', 20)

pdf.text(x=60, y=50, txt='Esto es un ejemplo (el primero)')
pdf.text(x=60, y=60, txt='Esto es un ejemplo (el segundo)')

# imagen (JPG, PNG)
url = 'https://www.motorpasion.com/'
pdf.image('logo.png', x=50, y=120, w=60, h=60, link=url)

pdf.output('ejemplo_text_img.pdf') # guardado del archivo PDF en el disco'''

'''# PDF Grid --------------------------------------------------------------------------------------------

# Bordes: 0 = no | 1 = Si | T = ↑ | B = ↓ |L = ← |R = →
# Alineación: C = centro |L = ← |R = →

from fpdf import FPDF

pdf = FPDF(orientation='P', unit='mm', format='A4') # configuración de salida de PDF
pdf.add_page() # se añade la página al archivo resultante

# texto
pdf.set_font('Arial', '', 20)

texto = ('Cras molestie, massa sit amet varius euismod, velit purus ornare tortor, ultrices tempor nunc metus '
         'fringilla lorem. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Suspendisse dui sapien, '
         'ornare vitae nisl vitae, fringilla ultricies arcu. Integer blandit faucibus magna, ut dignissim massa '
         'blandit in. Ut lectus lectus, ullamcorper nec consectetur et, luctus ut libero. Lorem ipsum dolor sit amet, '
         'consectetur adipiscing elit. Nullam eget volutpat orci. Mauris viverra, mauris nec porta maximus, '
         'ante ligula tincidunt nisl, at dapibus est tellus eget urna. Sed a enim placerat, ultricies nisi non, '
         'luctus est. Donec velit lectus, aliquet sed pulvinar quis, aliquam ac ex. Maecenas et blandit nisi. Nulla '
         'facilisi. In hac habitasse platea dictumst. Sed accumsan orci quis viverra finibus.')

# Margen 1
pdf.cell(w=50, h=15, txt='texto 1', border=1, align='C', fill=0)
pdf.cell(w=30, h=15, txt='texto 2', border=1, align='C', fill=0)
pdf.cell(w=20, h=15, txt='texto 2', border=1, align='C', fill=0)
pdf.multi_cell(w=0, h=15, txt='texto 2', border=1, align='C', fill=0)

# Margen 2
pdf.cell(w=50, h=15, txt='texto 1', border=1, align='C', fill=0)
pdf.cell(w=30, h=15, txt='texto 2', border=1, align='C', fill=0)
pdf.cell(w=50, h=15, txt='texto 2', border=1, align='C', fill=0)
pdf.multi_cell(w=0, h=15, txt='texto 2', border=1, align='C', fill=0)


# Margen 3
pdf.cell(w=50, h=15, txt='texto 1', border=1, align='C', fill=0)
pdf.cell(w=30, h=15, txt='texto 2', border=1, align='C', fill=0)
pdf.cell(w=20, h=15, txt='texto 2', border=1, align='C', fill=0)
pdf.multi_cell(w=0, h=15, txt='texto 2', border=1, align='C', fill=0)

# texto
pdf.multi_cell(w=0, h=10, txt=texto, border=1, align='L', fill=0)


pdf.output('ejemplo_grid.pdf') # guardado del archivo PDF en el disco'''

'''# PDF con tabla ----------------------------------------------------------------------------------
from fpdf import FPDF

pdf = FPDF(orientation='P', unit='mm', format='A4') # configuración de salida de PDF
pdf.add_page() # se añade la página al archivo resultante

# lista de datos
lista_datos =(
                (1, 'Diego 1', 'diego.collado@gmail.com', '2024-01-08'),
                (2, 'Diego 2', 'diego.collado@empresa.com', '2024-01-10'),
                (3, 'Diego', 'diego.collado@otracuenta.com', '2024-01-20'),
                (4, 'Diego', 'diego.collado@esomismo.com', '2024-01-28'),
                (5, 'Diego', 'diego.collado@masomenos.com', '2024-01-31')
             )*8

# texto
pdf.set_font('Arial', '', 15)
pdf.cell(w=0, h=15, txt='Reporte de emails', border=1, ln=1, align='C', fill=0) # título
pdf.cell(w=20, h=15, txt='ID', border=1, align='C', fill=0) # encabezado - 1
pdf.cell(w=40, h=15, txt='Nombre', border=1, align='C', fill=0) # encabezado - 2
pdf.cell(w=70, h=15, txt='e-mail', border=1, align='C', fill=0) # encabezado - 3
pdf.cell(w=0, h=15, txt='Fecha de alta', border=1, align='C', fill=0) # encabezado - 4

# lista de valores
for valor in lista_datos:
    for valor in lista_datos:
        pdf.cell(w=20, h=9, txt=str(valor[0]), border=1,
                 align='C', fill=0)

        pdf.cell(w=40, h=9, txt=valor[1], border=1,
                 align='C', fill=0)

        pdf.cell(w=70, h=9, txt=valor[2], border=1,
                 align='C', fill=0)

        pdf.multi_cell(w=0, h=9, txt=valor[3], border=1,
                       align='C', fill=0)

pdf.output('ejemplo.pdf') # guardado del archivo PDF en el disco'''

'''# PDF metadatos & márgenes y saltos -----------------------------------------------------------------
from fpdf import FPDF

pdf = FPDF(orientation='P', unit='mm', format='A4')  # configuración de salida de PDF
pdf.add_page()  # se añade la página al archivo resultante (1)

# texto
pdf.set_font('Arial', '', 15)
pdf.cell(w=0, h=15, txt='Hola mundo 1', border=1, align='C', ln=1, fill=0)
pdf.cell(w=0, h=15, txt='Hola mundo 2', border=1, align='C', ln=2, fill=0)

pdf.add_page()  # se añade la página al archivo resultante (2)
pdf.multi_cell(w = 0, h = 15, txt = 'Hola mundo', border = 1, align = 'C', fill = 0)
pdf.multi_cell(w = 0, h = 15, txt = 'Hola mundo', border = 1, align = 'C', fill = 0)
pdf.multi_cell(w = 0, h = 15, txt = 'Hola mundo', border = 1, align = 'C', fill = 0)

# Metadata
pdf.set_title(title='Página con metadata') # titulo
pdf.set_author(author='Diego Collado') # autor
pdf.set_creator('AdobePDF') # codificador
pdf.set_keywords(keywords='Hoja, PDF, pruebas, test') # palabras clave
pdf.set_subject(subject='Probando los metadatos en PDF')

pdf.output('ejemplo_metas.pdf')  # guardado del archivo PDF en el disco'''

'''# PDF texto & imagen -------------------------------------------------------------------------------
from fpdf import FPDF

class PDF(FPDF):
    def header(self): # método de clase para poder configurar el encabezado
        self.image('logo.png', x=10, y=10, w=15, h=15) # definición de logo
        self.set_font('Arial', 'B', 25) # definición del tipo de fuente, alto...
        self.cell(w=0, h=15, txt='Encabezado', border=1, ln=1, align='C', fill=0) # título
        self.ln(5) # line break

    def footer(self): # método de clase para poder configurar el pie
        self.set_y(-20) # posición a 1.50cm de la parte inferior de página
        self.set_font('Arial', 'I', 25)  # definición del tipo de fuente, alto...
        self.cell(w=0, h=10, txt='Página '  + str(self.page_no()) + '/{nb}', border=1, ln=1, align='C', fill=0)  # número de página

# MAIN
pdf = PDF() # instanciación
pdf.alias_nb_pages() # define el alias para un total de páginas

pdf.add_page() # se añade la página al archivo resultante
pdf.set_font('Arial', '', 12)

for i in range(80):
    pdf.cell(w=0, h=10, txt='Texto', border=1, ln=1, align='C', fill=0)

pdf.output('ejemplo_enc_pie.pdf') # guardado del archivo PDF en el disco'''

# PDF fuentes externas -------------------------------------------------------------------------------
# Fuentes disponibles en FPDF: Courier, Helvetica, Arial, Times, Symbol, ZapfDingbats
from fpdf import FPDF
from referencias_PDF import *

# Página
pdf = FPDF(orientation='P', unit='mm', format='A4') # configuración de salida de PDF
pdf.add_page() # se añade la página al archivo resultante

# Fuentes
pdf.set_font('Arial', '', 25)
pdf.add_font(family='Caviar Dreams', style='', fname='fuentes2/CaviarDreams.ttf', uni=True) # fuente normal
pdf.add_font(family='Caviar Dreams', style='B', fname='fuentes2/CaviarDreams_Bold.ttf', uni=True) # fuente negrita
pdf.add_font(family='Caviar Dreams', style='I', fname='fuentes2/CaviarDreams_Italic.ttf', uni=True) # fuente cursiva
pdf.add_font(family='Caviar Dreams', style='BI', fname='fuentes2/CaviarDreams_BoldItalic.ttf', uni=True) # fuente negrita y cursiva

tfont(pdf, '', 'Caviar Dreams')

# Textos
pdf.cell(w=0, h=15, txt='Probando con un texto cualquiera', border=1, ln=2, align='C', fill=0)
pdf.cell(w=0, h=15, txt='Times', border=1, ln=2, align='C', fill=0)

pdf.output('estilos.pdf')