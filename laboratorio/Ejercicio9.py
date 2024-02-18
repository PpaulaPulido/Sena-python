cestaCompra = {}
respuesta = "si"
suma = 0

while respuesta == "si":
    articulo = input("Ingrese el nombre del artículo: ")
    precio = float(input("Ingrese el precio del artículo: "))
    suma += precio
    
    cestaCompra[articulo] = precio
    
    respuesta = input("¿Desea agregar otro articulo?: ")
    respuesta.lower()

cestaCompra["Total"] = suma
print()
for key,value in cestaCompra.items():
  print(f"{key} : {value}")