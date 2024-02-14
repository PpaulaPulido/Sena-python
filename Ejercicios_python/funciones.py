def inicio():
    print("Menu principal")
    print("Seleccione la opcion correcta: ")
    print("1.Sumar \n2.Restar \n3.Multiplicacion \n4.Division \n5.Salir")

def main():
    while True:
        inicio()
        opcion = int(input("Seleccione la opcion: "))
        if opcion == 1:
            print("\nSeleccionaste la opcion de suma")
            Num1 = int(input("Ingresa el primer numero: "))
            Num2 = int(input("Ingresa el segundo numero: "))
            resultado = Num1 + Num2
            print(f"\nEl resultado de la suma es {resultado}\n")
        elif opcion == 2:
            print("\nSeleccionaste la opcion de Resta")
            Num1 = int(input("Ingresa el primer numero: "))
            Num2 = int(input("Ingresa el segundo numero: "))
            resultado = Num1 - Num2
            print(f"El resultado de la resta es {resultado}\n")
        elif opcion == 3:
            print("\nSeleccionaste la opcion de Multiplicacion")
            Num1 = int(input("Ingresa el primer numero: "))
            Num2 = int(input("Ingresa el segundo numero: "))
            resultado = Num1 * Num2
            print(f"El resultado de la multiplicacion es {resultado}\n")
        elif opcion == 4:
            print("\nSeleccionaste la opcion de Resta")
            Num1 = int(input("Ingresa el primer numero: "))
            Num2 = int(input("Ingresa el segundo numero: "))
            resultado = Num1 / Num2
            print(f"El resultado de la divison es {resultado}\n")
        elif opcion == 5:
            print("\nSaliste del programa\n")
            break
        else:
            print("Opcion invalida, intente de nuevo")
    
    
        
main()
