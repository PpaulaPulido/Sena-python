nombresEs = []
notasEs = []
promedioN = []
estudiantes = {}

cantidadA = int(input("Ingresa la cantidad de alumnos que desea ingresar: ")) 

for i in range(cantidadA):

    nombre = input(f"Ingresa el nombre del alumno {i+1}: ")

    # Verificar si el nombre ya existe en la lista
    '''nombre_existe = False
    for nombre_existe in nombresEs:
        if nombre_existe == nombre:
            print("Error: Este nombre ya ha sido ingresado.")
            nombre_existe = True
            break'''
    
    if nombre in nombresEs:
        print("Error: Este nombre ya ha sido ingresado.")
        continue
   
            
    nombresEs.append((nombre))

    i = 0
    nota = 1
    notasEs = []

    #Solicitar notas
    while nota > 0:
        nota = float(input(f"Ingresa la nota {i+1}: "))
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
    estudiantes["Promedios"] = promedioN

if  len(estudiantes) == 0:
    print("\n El diccionario de estudiantes se encuentra vacio")
else:
    print("\n Nombres de estudiantes con sus promedios")
    for nombre, promedio in zip(estudiantes["NombresEstudiantes"],estudiantes["Promedios"]):
        print(f"Estudiante: {nombre} - Promedio: {promedio}")
    
    
    