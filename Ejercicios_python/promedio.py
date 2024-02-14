num = int(input("¿Cuantos numeros desea promediar?: "))
contador = 0
suma = 0
promedio = 0

while contador < num:
  valor = int(input("Ingrese un nùmero: "))
  suma = suma + valor
  contador = contador + 1

promedio = suma/num

print(f"El promedio de los {num} nùmeros ingresados es: {promedio}")
