numeros = [1,2,3,4,5]
#encontrando el numero mayor de una lista 
numeros_mas_alto = max(numeros)

#encontrando el numero Menor de una lista 
numeros_mas_bajo = min(numeros)

#Redondeando a 6 decimales
redondeando= round(1.25325,5)

#Retorna FALSE -> 0, vacio, false, none \ Retorna TRUE -> distinto a 0, True, cadena, datos no vacíos
resultado=bool(2)

#All retorna True si TODOS los valores son verdaderos
resultado_all = all([2,"True",[12213,12312,34]])

#Suma todos los valores de un iterable
suma_total = sum(numeros)
print(suma_total)