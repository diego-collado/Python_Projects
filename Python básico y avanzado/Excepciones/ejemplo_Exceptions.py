'''
Exception Handling: Manejo de errores
    - Para saber qué está pasando y dónde en el código --> TRACEBACK
    - Controlar el comportamiento de nuestro código
****- DEBERÍAMOS CONTROLAR CUALQUIERA DE LAS EXCEPCIONES QUE SE PRODUZCAN EN NUESTRO SOFTWARE -****

-> Tipo de Exceptions:
    - TypeError: ocurre al aplicar una operación/función a datos de tipos inapropiados
    - ZeroDivisionError: ocurre cuando se intenta dividir entre 0
    - OverflowError: ocurre cuando un cálculo excede el límite del tipo de dato
    - IndexError: ocurre cuando se intenta acceder a una secuencia (lista, tupla...) con un índice no existente
    - KeyError: ocurre cuando se intenta acceder a un diccionario con claves no existentes
    - FileNotFoundError: ocurre cuando se intenta acceder a un archivo que no existe en la ruta que se indica
    - ImportError: ocurre cuando falla algo en la importación de módulos o paquetes

-> Jerarquía de Exceptions:
    - TypeError.mro(): [TypeError, Exception, BaseException, object]
    - ZeroDivisionError.mro(): [ZeroDivisionError, ArithmeticError, Exception, BaseException, object]
    - IndexError.mro(): [IndexError, LookupError, Exception, BaseException, object]
    - FileNotFoundError.mro(): [FileNotFoundError, OSError, Exception, BaseException, object]

BaseException
├── BaseExceptionGroup
├── GeneratorExit
├── KeyboardInterrupt
├── SystemExit
└── Exception
    ├── ArithmeticError
    │    ├── FloatingPointError
    │    ├── OverflowError
    │    └── ZeroDivisionError
    ├── AssertionError
    ├── AttributeError
    ├── BufferError
    ├── EOFError
    ├── ExceptionGroup [BaseExceptionGroup]
    ├── ImportError
    │    └── ModuleNotFoundError
    ├── LookupError
    │    ├── IndexError
    │    └── KeyError
    ├── MemoryError
    ├── NameError
    │    └── UnboundLocalError
    ├── OSError
    │    ├── BlockingIOError
    │    ├── ChildProcessError
    │    ├── ConnectionError
    │    │    ├── BrokenPipeError
    │    │    ├── ConnectionAbortedError
    │    │    ├── ConnectionRefusedError
    │    │    └── ConnectionResetError
    │    ├── FileExistsError
    │    ├── FileNotFoundError
    │    ├── InterruptedError
    │    ├── IsADirectoryError
    │    ├── NotADirectoryError
    │    ├── PermissionError
    │    ├── ProcessLookupError
    │    └── TimeoutError
    ├── ReferenceError
    ├── RuntimeError
    │    ├── NotImplementedError
    │    └── RecursionError
    ├── StopAsyncIteration
    ├── StopIteration
    ├── SyntaxError
    │    └── IndentationError
    │         └── TabError
    ├── SystemError
    ├── TypeError
    ├── ValueError
    │    └── UnicodeError
    │         ├── UnicodeDecodeError
    │         ├── UnicodeEncodeError
    │         └── UnicodeTranslateError
    └── Warning
        ├── BytesWarning
        ├── DeprecationWarning
        ├── EncodingWarning
        ├── FutureWarning
        ├── ImportWarning
        ├── PendingDeprecationWarning
        ├── ResourceWarning
        ├── RuntimeWarning
        ├── SyntaxWarning
        ├── UnicodeWarning
        └── UserWarning
'''

'''
raise: cuando se lanza un excepción por parte de Python, se hace de modo autómatico... ¿Qué pasa si quiero
ser yo el que lance esa excepción independienmente del lenguaje o del editor? Raise se utiliza para lanzar
excepciones que no sean por defecto de Python.'''

# Caso típico de Exception
try:
    d = 2 + "Hola"
except Exception as exc:
    print(f"Hemos tenido un problema: {type(exc)}")

# Caso típico utilizando RAISE
x = -1

if x < 0:
    raise Exception ("Lo sentimos, no se permiten los valores negativos")

y = "Hola, olita"
if not type(y) is int:
    raise TypeError("Solamente se permiten valores enteros")

# Controlando más de una excepción
while True:
    try:
        valor1 = int(input("Introduce dividendo:"))
        valor2 = int(input("Introduce divisor:"))
        division = valor1 / valor2

        print("División: ", division)

    except ValueError:
        print("Debes introducir únicamente números...")
    except ZeroDivisionError:
        print("No se puede dividir entre 0, es imposible")

    respuesta= input("¿Quieres seguir sumando más veces [s/n]?")

    if respuesta == 'n':
        break