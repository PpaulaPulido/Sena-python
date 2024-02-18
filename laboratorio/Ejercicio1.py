opcion = 1

while opcion > 0:
    
    print("\nMenu Principal\n")
    print("1.Juego del dado \n2.Grupos A y B \n3.Sala de juegos \n4.Contraseña \n5.Factura IVA \n6.Menu Listas \n7.Diccionario frutas \n8.Diccionario cesta de compras \n9.Diccionario Alumnos-Promedios \n10.Salir \n")
    
    opcion = int(input("Ingrese una opción del menú: "))

    if opcion == 1:
        print("\n Seleccionaste el juego del dado \n")
        import Ejercicio2

    elif opcion == 2:
        print("\n Seleccionaste clasificación de grupos A y B \n")
        import Ejercicio3

    elif opcion == 3:
        print("\n Seleccionaste la sala de juegos \n")
        import Ejercicio4

    elif opcion == 4:
        print("\n Seleccionaste validar contraseña \n")
        import Ejercicio5

    elif opcion == 5:
        print("\n Seleccionaste factura sin IVA \n")
        import Ejercicio6

    elif opcion == 6:
        print("\n Seleccionaste Menu de listas \n")
        import Ejercicio7

    elif opcion == 7:
        print("\n Seleccionaste Diccionario de frutas \n")
        import Ejercicio8

    elif opcion == 8:
        print("\n Seleccionaste diccionario de cesta de compras \n")
        import Ejercicio9

    elif opcion == 9:
        print("\n Seleccionaste Diccionario de alumnos y promedios \n")
    
    elif opcion == 10:
        print("\n Saliendo....")
        break
    else:
        print("\n Opcion invalida")