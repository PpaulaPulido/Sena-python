nombre = []
notas = []
listamejor = []
eliminar = []
mb= 0
b = 0
ints = 0

for x in range(1,5):
    nom = input(f"Por favor ingresar el nombre del alumno {x}: ")
    nombre.append(nom)
    nota = float(input(f"Ingresar la nota del alumno {x}: "))
    notas.append(nota)

for x in range(len(nombre)):
    print(nombre[x])
    print(notas[x])

    if notas[x] >= 8:
        alumnoBueno = nombre[x]
        listamejor.append(alumnoBueno)
        print("Alumno muy bueno")
        mb +=1
    else:
        if notas[x] >= 4:
            print("Alumno bueno")
            b += 1
        else:
            print("Alumno no aprueba la materia")
            ints += 1

for z in len(notas):
    if notas[z] >= 4 and notas[z]<=7:
        eliminar.append[z]

for d in sorted(eliminar,reverse=True):
    notas.pop(d)
    nombre.pop(d)

print("Listado de la lista inicial: ",nombre)
print("\nCantidad de alumnos muy buenos son: ",mb)
print("Cantidad de alumnos buenos: ",b)
print("Cantidad de alumnos que no aprobaron: ",ints)
print(f"\nLista de los almunos muy buenos: {listamejor}")
print(f"Lista de alumnos con notas entre 4 y 7: {nombre}")
print("Lista de eliminados: ",eliminar)
