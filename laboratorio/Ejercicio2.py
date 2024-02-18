alvaro = int(input("Alvaro arroja el dado: "))
barbara = int(input("Barbara arroja el dado: "))

while (alvaro < 1 or alvaro > 6):
    print("El numero del dado no es correcto")
    alvaro = int(input("Alvaro arroja el dado: "))

while (barbara< 1 or barbara > 6):
    print("El numero del dado no es correcto")
    barbara= int(input("Barbara arroja el dado: "))
    
    
if (alvaro > barbara):
    print(f"Alvaro Ganó con un puntaje de {alvaro}")
elif (alvaro < barbara):
    print(f"Barbara Ganó con un puntaje de {barbara}")
else:
    print(f"Empate!!! con un puntaje de {alvaro} y {barbara}")