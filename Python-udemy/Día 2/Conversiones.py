#Implícita
#Sin expresar una conversión

num1 = 20
num2 = 30.5

num3 = num1 + num2
#Al num1 hacer parte de una suma cambia el tipo de dato

#Explícita
num4 = 5.8
num_int = int(num4)

print(type(num_int))
print(num_int)
print(type(num2))


edad = input("dime tu edad: ")

print(type(edad))

edad = int(edad)

print(type(edad))

nueva_edad = 1 + edad

print("Tu nueva edad es: ", nueva_edad)