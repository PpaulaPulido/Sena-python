
nombre = input("Ingresa tu nombre: ")
sexo = input("Ingresa tu sexo M/F: ")

if (sexo.lower() == "f") and (nombre < "m"):
    print("Grupo A")
elif (sexo.lower() == "m")and (nombre >= "n"):
    print("Grupo A")
elif (sexo.lower() == "f") and (nombre >= "m"):
    print("Grupo B")
elif (sexo.lower() == "m")and (nombre < "n"):
    print("Grupo B")
else:
    print("Error al claisificar")