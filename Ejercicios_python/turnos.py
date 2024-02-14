suma = 0
promedioMañana = 0
promedioTarde = 0
promedioNoche = 0

for i in range(6):
    print("Turno de la mañana")
    edad = int(input(f"Ingresa la edad del estudiante {i+1}: "))
    suma += edad

promedioMañana = suma/6
suma = 0

for i in range(7):
    print("Turno de la tarde")
    edad = int(input(f"Ingresa la edad del estudiante {i+1}: "))
    suma += edad

promedioTarde = suma/7
suma = 0

for i in range(12):
    print("Turno de la Noche")
    edad = int(input(f"Ingresa la edad del estudiante {i+1}: "))
    suma += edad

promedioNoche = suma/6


print(f"Promedio de la mañana es {promedioMañana}")
print(f"Promedio de la mañana es {promedioTarde}")
print(f"Promedio de la mañana es {promedioNoche}")

if promedioMañana > promedioTarde and promedioMañana > promedioNoche:
    print("Promedio Mañana tiene un promedio superior")
elif promedioTarde > promedioMañana and promedioTarde >promedioNoche:
    print("Promedio Tarde tiene un promedio superior")
elif promedioNoche > promedioMañana and promedioNoche >promedioTarde:
    print("Promedio Noche tiene un promedio superior")


