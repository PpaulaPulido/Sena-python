print("Rango de años \n")
inicio = int(input("Ingrese el año de inicio del rango: "))
final = int(input("Ingrese el año final del rango: "))

def bisiesto(inicio,final):
    contadorBisiesto = 0
    contadorAgnos = -1
    contadorNoBisiesto = 0
    for i in range(inicio,final+1):
        print(i)
        if i%4 == 0:
            if i%100 == 0:
                contadorNoBisiesto += 1
            else:
                contadorBisiesto += 1
        else:
            contadorNoBisiesto += 1

        contadorAgnos +=1
    
    print(f"Cantidad de años del {inicio} hasta el {final}: {contadorAgnos}")
    print(f"Cantidad de años bisiestos: {contadorBisiesto}")
    print(f"Cantidad de años no bisiestos: {contadorNoBisiesto}")

bisiesto(inicio,final)