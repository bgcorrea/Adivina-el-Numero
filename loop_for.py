lista = ['a', 'b', 'c']

for letra in lista:
    numero_de_letra = lista.index(letra) + 1
    print(numero_de_letra)
    print(f"en la lista existe la letra {letra}")


lista = ['Pablo', 'Laura', 'Fede', 'Luis', 'Julia']
for nombre in lista:
    if nombre.startswith('L'):
        print(nombre)
    else:
        print("Nombre que no comienza con L")

numeros = [1, 2, 3, 4, 5]
mi_valor = 0

for numero in numeros:
    mi_valor = mi_valor + numero

print(mi_valor)

palabra = 'python'

for letra in palabra:
    print(letra)