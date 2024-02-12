def diccionario_colores(color):
    colores = {
        'black':(0, 0, 0),
        'white': (255, 255, 255),
        'green': (96, 218, 117),
        'blue': (96, 181, 218),
        'red': (239, 71, 71),
        'rose': (214, 74, 236),
        'grey':(103, 103, 103),
        'grey2': (233, 233, 233)
    }
    return colores

# definición de colores para columnas, textos...
def dcol_set(hoja, color):
    cr, cg, cb = diccionario_colores(color) # color_red = cr, color_green = cg, color_blue = cb
    hoja.set_draw_color(r = cr, g = cg, b = cb)

def bcol_set(hoja, color):
    cr, cg, cb = diccionario_colores(color)  # color_red = cr, color_green = cg, color_blue = cb
    hoja.set_fill_color(r = cr, g = cg, b = cb)

def tcol_set(hoja, color):
    cr, cg, cb = diccionario_colores(color)  # color_red = cr, color_green = cg, color_blue = cb
    hoja.set_text_color(r = cr, g = cg, b = cb)

def tfont_size(hoja, size):
    hoja.set_font_size(size)

def tfont(hoja, estilo, fuente='Arial'):
    hoja.set_font(fuente, style=estilo)
