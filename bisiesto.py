año = int(input("Ingrese el año: "))

def bisiesto(año):
    if año%4 == 0:
        if año%100 == 0:
            print(f"El año {año} no es bisiesto")
        else:
            print(f"El año {año} bisiesto")
    else:
        print(f"El año {año} no es bisiesto")

bisiesto(año)