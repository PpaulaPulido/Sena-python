texto = "Buenos dias definiendo un parametro en una funcion"
def mensaje(texto):
    print(texto)

mensaje(texto)

def datos():
    N1 = int(input("Ingresa el primer numero: "))
    N2 = int(input("Ingresa el segundo numero: "))
    calcular(N1,N2)
    positivo(N1,N2)

def calcular(N1,N2):
    
    if N1 > N2:
        print("El primer numero es mayor")
    elif N1 < N2:
        print("El segundo numero es mayor")
    else:
        print("Son numeros iguales")


def positivo(p1,p2):
    if p1 > 0 and p2 > 0:
        print("Son numeros positivos")
    elif p1 < 0 and p2 <0:
        print("Son numeros negativos")
    else:
        print("Al menos uno de los dos no es positivo")

datos()