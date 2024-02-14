tupla =  (2,4,6)
fecha = (2,'febrero',2024)

print(tupla)
print(fecha)

palabras = int(input('Cuantas palabras deseas agregar: '))

if palabras < 1:
    print("No es valido")
else:
    lista = []
    for i in range(palabras):
        palabra = input(f"Escribe la palabra {i+1}: ")
        lista += [palabra]
    
    print(f"La lista creada es: {lista}")
