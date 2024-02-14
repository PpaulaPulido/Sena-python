persona = {
    "Nombre": "paula",
    "apellido":"pulido",
    "estatura":1.51,
    "edad":22,
    "email":"pulidoibarra15@gmail.com",
    "ciudadNac": "Bogotá",
    "genero":["femenino","masculino","otro"]
}
print(persona)
print("El nombre de la persona es: ",{persona["Nombre"]})

#Agregar telefono
persona["telefono"] = 3114404010
print(persona)

#mofiicar elemento
persona["telefono"] = 3110650965
print(persona)

#modificar la clave
persona["celular"] = persona.pop("telefono")
print(persona)

#eliminar un elemento
del persona["celular"]
print(persona)

#iterar los items de las claves y valores
for clave,valor in persona.items():
    print(clave , ":",valor)
    
