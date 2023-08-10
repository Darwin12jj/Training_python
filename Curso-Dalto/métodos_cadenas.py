

resultado1 = "Lower convierte en minúscula".lower()
print(resultado1)
resultado2 = "Upper convierte en mayúscula".upper()
print(resultado2)
resultado3 = "capitalize convierte la primer letra en mayúscula".capitalize()
print(resultado3)

#Find
#Busca un valor especificado.
busqueda_find = resultado1.find("l")
print (busqueda_find)

#Index
#Buscamos una cadena en otra cadena. Si no hay coincidencias lanza una excepción.
busqueda_index = resultado2.index ("U")
print (busqueda_index)

#Isnumeric
#Permite ver que si es numerico manda True.
text_num = "123"
esnum = text_num.isnumeric()
print (esnum)

#Isalpha
#Si es alpha numerico devuelve True.
#Solo son válidos a-z no espacios.
es_alpha = "asdñ".isalpha()
print (es_alpha)

#Count
#Devuelve el numero de ocurrencias de una subcadena en la cadena dada
#En vez de encontrar una coincidencia nos dice cuantas veces se encuentra.
contar_coincidencia = "cadenaxddd".count("z")
print(contar_coincidencia)

#Len 
#Cuenta la cantidad de caracteres que tiene una cadena.
metodo_len = len("este texto debe tener cierta cantidad de letras")
print(metodo_len)

#Startswidth
#Verificamos si una cadena EMPIEZA con otra cadena dada, en caso de que si devuelve True.
empieza_con = "Texto de prueba".startswith("Texto")
print(empieza_con)

#Endswidth
#Verificamos si una cadena TERMINA con otra cadena dada.
termina_con = "Texto de prueba2".endswith("ba2")
print(termina_con)

#Replace 
#Reemplaza una pedazo por otro. Si no encuentra coincidencia devuelve el valor inicial.
reemplazar_valor = "texto a reemplazar".replace("texto", "balón")
print(reemplazar_valor)

#Split
#Separa cadenas con lo que le pasemos convirtiendolas en lista
cadena_separada = "Esta cadena se separá por espacios".split(" ")
print(cadena_separada)