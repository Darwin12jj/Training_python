#Escribir un programa que pregunte al usuario la fecha de su nacimiento en formato dd/mm/aaaa y muestra por pantalla, el día, el mes y el año. Adaptar el programa anterior para que también funcione cuando el día o el mes se introduzcan con un solo carácter.

numero_mult = int(input("Ingrese un número por el que multiplicará: "))

numeros = [1,2,3,4,5,6,7,8,9,10]
for numero in numeros:
    resultado = numero * numero_mult
    print(f"{numero_mult} X {numero} = ",resultado)