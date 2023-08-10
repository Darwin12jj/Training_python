#Cada caracter tiene una posición ordenada dentro de una cadena
#"H O L A"
# 0 1 2 3

mi_texto = "Esto es una prueba"

#Entre llaves se conoce el caracter de dicha posición
#Con números negativos cuenta de derecha a izquierda
resultado0 = mi_texto[2]
#Usando Index() lanza la posición en la que se encuentra el caracter
#Si no encuentra lo buscado lanza un error
resultado1 = mi_texto.index("p")
#Agregando un numero al lado de lo buscado comenzará a buscar desde dicha posición.
resultado2 = mi_texto.index("o",2)
#Con un tercer parámetro se indica HASTA DONDE se hará la búsqueda
resultado3 = mi_texto.index("p",3,16)

#No es necesario escribir index[]. Con las llaves [] basta.
#Con paréntesis si es necesario escribir .index() por completo.
palabra = "ordenador"
print(palabra[5])
print(palabra.rindex("d"))

#RINDEX() encuentra la última ocurrencia del valor dentro de la cadena.
resultado4 = palabra.rindex("o")
print(resultado4)
