#Las listas no son inmutables. Por que se podrá modificar sus valores.
#La lista puede tener diferentes clases de valores
mi_lista = ["a","b","c"]
#Mostrando el tipo de clase
tipo = type(mi_lista)

#Conociendo la cantidad de elementos de la lista con LEN
elementos = len(mi_lista)

#Indexando una lista
indexando = mi_lista [1]

#Lo conocido para strings funciona con la lista
indexando1 = mi_lista[0:2]
print(indexando1)
