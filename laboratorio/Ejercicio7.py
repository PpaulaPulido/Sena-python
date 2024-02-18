lista = [1,2,3,4,5]

print("La lista actualmente es ", lista)

print("\n1.Añadir numero \n2.Añadir numero en posición \n3.Longitud de la lista \n4.Eliminar el ultimo numero \n5.Eliminar numero en posicion \n6.Contar número \n7.Posiciones de un numero  \n8.Mostrar números \n9.Salir\n")

opcion = 0


while True:
    
    opcion = int(input("Escoge una opcion: "))
    if  opcion == 1:
    
        print("Escogiste la opcion 1 \n")
        num = int(input("Ingresa un número para agregar: "))
        lista.append(num)
        print(f"Tu lista es: {lista} \n")
    
    elif opcion == 2:
        print("Escogiste la opcion 2 \n")
        num = int(input("Ingresa un número para agregar: "))
        posicion = int(input("Ingresa la posicion: "))
        
        if posicion >= 1 and posicion <= len(lista):
            lista.insert(posicion,num)
            print(f"Tu lista es: {lista} \n")
        else:
            print("La posicion que ingresaste es invalida \n")
            
    elif opcion == 3:
        
        print("Escogiste la opcion 3 \n")
        longitud = len(lista)
        print(f"La lista {lista} tiene una longitud de {longitud}")

    elif opcion == 4:
        
        print("Escogiste la opcion 4 \n")
        lista.pop()
        print(f"tu nueva lista es: {lista}")

    elif opcion == 5:
        
        print("Escogiste la opcion 5 \n")
        posicion = int(input("Ingresa la posicion a eliminar: "))
        
        if posicion >= 1 and posicion <= len(lista):
            lista.pop(posicion)
            print(f"Tu lista es: {lista} \n")
        else:
            print("La posicion que ingresaste es invalida \n")

    elif opcion == 6:
        
        print("Escogiste la opcion 6 \n")
        buscar = int(input("Ingresa el número a contar: "))
        contar = lista.count(buscar)
        print("Nuestra lista es ", lista)
        print(f"El numero {buscar} aparece {contar} veces en la lista")

    elif opcion == 7:
        
        print("Escogiste la opcion 7 \n")
        buscar = int(input("Ingresa el número a buscar: "))
        posicion = lista.index(buscar,1)
        print(f"el numero {buscar} esta en la posicion {posicion}")

    elif opcion == 8:
        
        print("Escogiste la opcion 8 \n")
        print("La lista es ",lista)

    elif opcion == 9:
        print("Escogiste la opcion 9 \n")
        print("Saliendo....")
        break
        
    else:
        print("Opcion invalida \n")   
    