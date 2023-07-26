#Se crean con función SET
conjunto = set(["dato1"])


#["dato1.1","dato1,2"]
#Metiendo un conjunto dentro de otro conjunto
conjunto1 = frozenset(["dato1", "dato2"])
conjunto2 = {conjunto1, "dato 3"}
print (conjunto2)



#TEORIA DE CONJUNTO

#Hay conjunto y subconjunto
#El subconjunto nace de una parte de datos del conjunto

conjunto1 = {1, 3 ,5, 9}
conjunto2 = {1,3,9}
#verificando si es subconjunto
resultado = conjunto1.issubset(conjunto2)
resultado = conjunto2 <= conjunto1

#Verificando su es superconjunto
resultado = conjunto1.issuperset(conjunto2)
resultado = conjunto2 <= conjunto1 

#Verificar si hay un número en común dará falso
resultado = conjunto1.isdisjoint(conjunto2)
print (resultado)