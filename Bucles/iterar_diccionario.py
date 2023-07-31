diccionario = {
    "nombre" : "Peter",
    "Apellido" : "El gato",
    "edad" : 2
}

#Recorriendo dccionario para obtener las claves
for key in diccionario.items(): 
    key 
    print(f"La clave es:{key}")

#Recorriendo dccionario para obtener las claves y el valor 
for datos in diccionario.items(): 
    key = datos[0]
    value = datos[1]
    print(f"La clave es:{key}, y el valor es:{value}\n")