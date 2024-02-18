edadCliente = int(input("Por favor ingresa la edad del cliente: "))

if (edadCliente < 4):
    print("Entrada es gratis")
    
elif (edadCliente >= 4 and edadCliente <= 18 ):
    print("El costo de la entrada es de 30.000 ")
else:
    print("El costo de la entrada es de 50.000") 