#Creando una lista con LIST
lista = list (["hola", "esto", "es", "una", "lista", 1123])    

#Devuelve la cantidad de elementos de una lista
resultado = len(lista)
print(lista, "\n","La lista tiene" ,resultado, "elementos")


print("\n")


#Agregando elementos a la lista con APPEND
#Se agregará al final de la lista
lista.append("Fuí agregado")
print(lista)


print("\n")


#Agregando elemento a lista con INSERT
#Primero se da la posición a cambiar, luego el valor
lista.insert(3, "Cambiado en la cuarta posición")
print (lista)


print("\n")


#Agregando con EXTEND
#Se agregan VARIOS elementos a la lista
#Es necesario agregarlos dentro de llaves como una lista([elementos,1,2,3,4...])
lista.extend(["Jajaja", 12, False])
print(lista)


print("\n")


#Eliminando elemento de la lista por su posición con POP
lista.pop(2)#-1 para eliminar el último, -2 para el penúltimo ETC...
print(lista)


print("\n")


#Removiendo elemento por su valor con REMOVE
lista.remove("Jajaja")
print(lista)


print("\n")


#Organizando la lista de forma ascendente con SORT
#Si se añade "reverse = True" se mostrarán al revés
lista.sort(reverse=True)
print(lista)


























#Eliminando toda la lista con CLEAR
#lista.clear()