nAlturas = int(input("Cuantas alturas desea ingresar: "))
suma = 0
promedio = 0

for i in range(nAlturas):
  altura = float(input(f"Ingrese la altura de la persona numero {i+1}: "))
  suma += altura

promedio = suma/nAlturas

print(f"El promedio de las alturas ingresadas es: {promedio}")