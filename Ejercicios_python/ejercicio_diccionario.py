nombresEs = []
notasEs = []
promedioN = []
estudiantes = {}

cantidadA = int(input("Ingresa la cantidad de alumnos que desea ingresar: ")) 

for i in range(cantidadA):

    nombre = input(f"Ingresa el nombre del alumno {i+1}: ")

    for i in nombresEs:
        if i == nombre:
            print("error")


    nombresEs.append((nombre))

    i = 0
    nota = 1
    notasEs = []

    #Solicitar notas
    while nota > 0:
        nota = int(input(f"Ingresa la nota {i+1}: "))
        i += 1
        notasEs.append((nota))
    
    #Calcular promedio
    notasEs.pop()
    sumaPromedio = 0
    prom = 0

    for i in range(len(notasEs)):
        valor = notasEs[i]
        sumaPromedio += valor

    prom = sumaPromedio/(len(notasEs))
    promedioN.append((prom))

    estudiantes["NombresEstudiantes"] = nombresEs
    estudiantes["Notas"] = notasEs
    estudiantes["Promedios"] = promedioN
    print(estudiantes)
    


        
