import random
from random import *

aleatorio = randint(1, 50)
print(aleatorio)

aleatorio = uniform(1, 5)
print(aleatorio)

aleatorio = random()
print(aleatorio)

colores = ["azul", "rojo", "verde"]
aleatorio = choice(colores)
print(aleatorio)

numeros = list(range(5, 50, 5))
shuffle(numeros)
print(numeros)