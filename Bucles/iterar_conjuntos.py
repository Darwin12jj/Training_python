#ITERAR conjunto

#FOR
animales = {"perro", "gato", "pez", "caballo", "colibri", "arroz"}
for animal in animales:
    print("En este momento es un: ", animal)
    
#Recorriendo conjunto y multiplicando cada valor  por 10
#TABLA DE MULTIPLICAR:
numero_mult = int(input("Ingrese un número por el que multiplicará: "))

numeros = {1,2,3,4,5,6,7,8,9,10}
for numero in numeros:
    resultado = numero * numero_mult
    print(f"2 X {numero} = ",resultado)
    
#Iterar dos conjuntos del mismo tamaño al mismo tiempo con ZIP
for numero, animal in zip (animales, numeros) :
    print (f"Recorriendo conjunto 1: {animal}")
    print (f"Recorriendo conjunto 2: {numero}")

#forma correcta de recorrer un conjunto con su índice enumerada  
for num in enumerate(numeros):
    indice = num[0]
    valor = num[1]
    print (f"El índice es: {indice} y el valor es: {valor}")
    
#Usando Else SIEMPRE se ejecuta al final
for numero in numeros: 
    print(f"Ejecutando el último bucle, el valor actual es: {numero}.")
else:
    print("El bucle termino.")
    
#Todo LO ANTERIOR FUNCIONA EXACTAMENTE IGUAL PARA TUPLAS