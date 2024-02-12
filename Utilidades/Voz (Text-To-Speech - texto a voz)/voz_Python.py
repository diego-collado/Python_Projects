'''
Conversión de texto a voz (TTS - Text To Speech)
gTTS: https://gtts.readthedocs.io/en/latest/index.html
Realmente es una libreria de Python que utiliza la API de Google: Google Translate's text-to-speech
Antes de nada, realizar: pip install gTTS
Para listar todos los idiomas que soporta: gtts-cli --all
'''

'''
# Texto a MP3
from gtts import gTTS # importación de librería gTTS

texto = "En un lugar de la Mancha, de cuyo nombre Juan ni se acuerda... "
lenguaje = "zh-TW" # determinación del lenguaje de "lectura"

audio = gTTS(text=texto, lang=lenguaje, slow=False)
audio.save('Mancha_M-TW.mp3')

print("Proceso terminado")'''

# Texto a MP3 en varios idiomas (mismo archivo)
from gtts import gTTS # cargar el módulo correspondiente

# Conversiones de texto a voz
spa = gTTS("Hola, chicuelos, estamos jugando con la voz y Python", lang='es') # texto 1: español
eng = gTTS("Hi, guys, we're playing with Python and voices", lang='en') # texto 2: inglés
fra = gTTS(text="Bonjour les enfants, nous jouons avec la voix et Python", lang='fr') # texto 3: francés

# grabación de las voces en un archivo
with open("varios_idiomas.mp3", 'wb') as archivo:
    spa.write_to_fp(archivo)
    eng.write_to_fp(archivo)
    fra.write_to_fp(archivo)