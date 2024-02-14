edad = int(input('Por favor ingresar su edad: '))

if edad < 4:
    Ingreso = 0
elif edad <= 18:
    Ingreso = 5000
else:
    Ingreso = 10000


print(f"El precio e la entrada es {Ingreso} pesos")    