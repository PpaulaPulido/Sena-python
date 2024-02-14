import random


secreto = random.randint(1,10)

numero = int(input("Adivina el numero entre 1 a 10: "))


while numero != secreto:
    if numero < secreto:
        print("El numero es mayor")
    else:
        print("El numero ee menor")
    
    numero = int(input("Intentalo de nuevo: "))

print(f"Felicidades adivinaste el numero {secreto}")
print("final")