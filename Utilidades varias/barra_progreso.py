'''
Se utiliza para realizar una estimación del tiempo restante y el tiempo que ha transcurrido en una carga,
en una instalación...
TQDM proviene de la palabra árabe taqadum (تقدّم), que significa progreso, aproximación...

    1º.- Instalar en el CMD: pip install tqdm
    2º.- Trabajar con las nuevas barras de progreso

Más info: https://pypi.org/project/tqdm/
'''
# Barra de progreso simple
from tqdm import tqdm # importación de módulo para trabajar con barras de progreso. Más info: https://tqdm.github.io/

for i in tqdm(range(int(9000000))):
    pass # este código simplement ejecuta un "paso a la siguiente orden"

# Barra de progreso con texto
from tqdm import tqdm
from time import sleep # módulo utilizado para poder hacer delay (retardo)

for i in tqdm(range(0, 100), desc="Cargando ultravirus..."):
    sleep(.1) # delay en segundos

# Barra de progreso con número de iteraciones totales esperadas
from tqdm import tqdm
from time import sleep

for i in tqdm(range(0, 100), total=500, desc="Cargando ultravirus..."): # total= significa el número de iteraciones esperadas
    sleep(.1)

# Barra de progreso para desactivación de barra
from tqdm import tqdm
from time import sleep

for i in tqdm(range(0, 100), disable=True, desc="Cargando sistema operativo..."): # disable: desactivación de barra
    sleep(.1)

# Barra de progreso con ancho de salida
from tqdm import tqdm
from time import sleep

for i in tqdm(range(0, 100), ncols=220, desc="Cargando sistema operativo..."): # ncols: número de columnas para mostrar en pantalla
    sleep(.1)

# Barra de progreso con actualización mínima de la pantalla de progreso
from tqdm import tqdm
from time import sleep

for i in tqdm(range(0, 100), mininterval=3, desc="Cargando sistema operativo..."): # mininterval: para mostrado con demora
    sleep(.1)

# Barra de progreso con ASCII: según va completando, se va quitando el número y se convierte en carácter # (por ejemplo)
from tqdm import tqdm
from time import sleep

for i in tqdm(range(0, 100), ascii="123456789#"):
    sleep(.1)

# Barra de progreso con unit (it: la unidad de tiempo de una iteracción)
from tqdm import tqdm
from time import sleep

for i in tqdm(range(0, 100), unit="GB", desc="Cargando sistema operativo"):
    sleep(.1)