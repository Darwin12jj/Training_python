#Los Strings son inmutables
nombre = "Darwin "
nombre2 = "K"
print(nombre * 10)

#Un string puede tener varias lineas de codigo escribiendo 3 pares de comillas dobles """ """
poema = """Mil pequeños peces
blancos como
si hirviera el color del agua"""

#Usando IN se puede saber si se encuentra un caracter o una palabra dentro de los strings
print("r" in poema)

#Usando NOT IN dará el mesaje contrario por la doble negación
print("r" not in poema)

#LEN permite saber el largo de un string en cuanto a letras, comas o números vacíos
poema2 = "Hola"
print(len(poema2))