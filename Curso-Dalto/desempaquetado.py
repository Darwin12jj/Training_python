#Desempaquetado de variables
#Logra asignar valores a variables de una manera particular.
#NO PERMITE DESEMPAQUETAR NÚMEROS

#Creación de datos
datos_tupla = ("darwin","Jimenez", 2003)
datos_lista = {"Nombre", "apellido", 203}

#Desempaquetado
nombre, apellido, año_nacimiento = datos_lista

#Resultado
print(nombre,"Nació en" ,año_nacimiento)