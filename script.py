from random import randint

nombre = input("Indícame tu nombre: ")
numero_maquina = randint(1, 100)
intentos = 0

while intentos < 8:
    numero_jugador = int(input("Indícame tu numero: "))
    if numero_jugador < 1 or numero_jugador > 100:
        print("Ingrese un número válido")
        continue
    
    intentos += 1

    if numero_jugador > numero_maquina:
        print(f"El numero indicado por {nombre} es más alto que el número de la máquina")
    elif numero_jugador < numero_maquina:
        print(f"El numero indicado por {nombre} es más bajo que el número de la máquina")
    elif numero_jugador == numero_maquina:
        print(f"El numero indicado por {nombre} es igual que el número de la máquina. Has ganado! y lo has conseguido con {intentos} intentos")
        break
    print(f"Te quedan {8 - intentos} intentos")
    
if numero_jugador != numero_maquina:
    print(f"Fallaste esta vez {nombre}. El número correcto era {numero_maquina}")
        
