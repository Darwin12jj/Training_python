#upper() pasa a mayúsculas
#lower() pasa a minúsculas
#split() separa una cadena en partes formando una lista
#join() une elementos de una lista usando un separador
#find() permite encontrar un sub-string
#replace() reemplaza un substring

texto = "Esto es un texto"
#Método Upper()
#Se puede indicar un índice con [] para modificar dicho elemento
resultado = texto[2].upper()

#Método lower()
resultado1 = texto.lower()

#Método split()
#Indicado un parámetro se añadirá separción en dicha posición
resultado2 = texto.split("t")

#Método Join()
#Funciona con una lista
#Perimte enidar los elementos de una lista
a = "Aprender"
b = "Python"
c = "En"
d = "La"
e = "Casa"
f = "De"
g = "Su"
h = "Mamá"
i = " ".join([a,b,c,d,e,f,g,h])
print (i.capitalize())

#Método .find()
#Busca un determinado caracter dentro de mi string
#La diferencia entre find e index es que FIND si no encuentra e valor especificado únicamente lanza -1. no un error
resultado3 = texto.find("1")

#Método .replace()
#Necesita dos parámetros. Primero el texto a eliminar y segundo el texto por el que se remplazará
resultado4 = texto.replace("e", "x", )
print(resultado4)