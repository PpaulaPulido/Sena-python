frutas  = {}
respuesta = "si"

while  respuesta == "si":
    agregar = input("Ingresa el nombre de la fruta: ")
    
    if agregar in frutas.keys():
        print("Esta fruta ya se encuentra en la lista.")
    else:
        precio = float(input(f"Ingresa el precio de la fruta: "))
        frutas[agregar] = precio
        print(frutas)
    
    respuesta = input("¿Desea agregar otra fruta?: ")
    
