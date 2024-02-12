nombreConductores = []
kilometros = []
total_kms = []
sumatotal = 0

for i in range(3):
    nombre = input(f"\nIngresa el nombre del conductor {i+1}: ")
    nombreConductores.append(nombre)
    
    kilometros = []
    sumatotal = 0

    for x in range(7):
        kilo = float(input(f"Ingresa la cantidad de kilometros qu realiza en el día {x+1}: "))
        kilometros.append(kilo)
    
    for z in range(len(kilometros)):
        sumatotal += kilometros[z]

    total_kms.append(sumatotal)
   

print("\nLista de conductores y kilometros realizados: \n")
for x in range(len(nombreConductores)):
    print(f"{nombreConductores[x]}: {total_kms[x]} kilometros")