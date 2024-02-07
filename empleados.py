nEmpleados = int(input("Ingrese el número de empleados: "))
contadorSuperior = 0
contadorInferior = 0
importe = 0

for i in range(nEmpleados):
  sueldo = float(input(f"Ingrese el sueldo del empleado {i+1}: "))
  importe += sueldo
  if sueldo > 1300000 and sueldo < 3000000:
    contadorInferior += 1
  elif sueldo > 3000000 and sueldo < 10000000:
    contadorSuperior += 1

print(f"Empleados con sueldo superior a 3.000.000: {contadorSuperior}")
print(f"Empleados con sueldo inferior a 3.000.000: {contadorInferior}")
print(f"El importe total de sueldos es: {importe}")
