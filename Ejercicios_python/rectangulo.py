ancho = int(input("Ingresa el ancho del rectangulo: "))
altura = int(input("Ingresa la altura del rectangulo: "))
caract = input("Ingresa el caracter a utilizar: ")

def dibujar(ancho,altura,letra):
    for i in range(ancho):
        for j in range(altura):
            print(letra,end= " ")
        print()

dibujar(ancho,altura,caract)
