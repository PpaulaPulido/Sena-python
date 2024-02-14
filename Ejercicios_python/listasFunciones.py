enteros = []
def ingresar():
    
    for i in range(5):
        numero = int(input("Ingresa el numero: "))
        enteros.append(numero)
  
    
def imprimir(enteros):
    print("Los datos de la lista son: ")
    for i in enteros:
        print(i)



def sumar(enteros):
    acumulador = 0
    for x in enteros:
        acumulador += x
    print(f"La suma de los elementos es {acumulador}")


ingresar()
imprimir(enteros)
sumar(enteros)
