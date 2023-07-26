#Crando diccionarios con dict
diccionario = dict(nombre = "Darwin", apellido = "Jimenez")

#Las listas no pueden ser claves por que son mutables. Se usa frozenset para meter conjuntos
diccionario = {("Dalto","Rancio"), "xd"}

#Creando diccionario con fromkeys() para obtener diccionario con valor NONE
#Es necesario colocarla como si fuese lista
diccionario = dict.fromkeys(["Nombre", "Apellido"])

#Creando diccionario con fromkeys() con dos parámetros
diccionario = dict.fromkeys(["Nombre", "Apellido"], "")
print (diccionario)




#diccionario = dict(nombre = input("ingrese su nombre: "), apellido = input("Ingrese su apellido: "))
#print(diccionario)