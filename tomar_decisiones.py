mascota = "perro"
if mascota == "gato":
    print("tienes un gato")
elif mascota == "perro":
    print("tienes un perro")
else:
    print("no sé que animal tienes")

edad = 16
calificacion = 9

if edad < 18:
    print("eres menor de edad")
    if calificacion >= 7:
        print("aprobado")
    else:
        print("No aprobado")
else:
    print("eres adulto")