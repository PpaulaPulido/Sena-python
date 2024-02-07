frase=input("Por favor ingrese una frase:  ")
letra = input ("Por favor ingrese la letra a buscar: ")
cl=0

for i in frase:
    if i ==letra:
        cl+=1

print ("La letra '%s' aparece %2i en la frase '%s', " %(letra, cl, frase))