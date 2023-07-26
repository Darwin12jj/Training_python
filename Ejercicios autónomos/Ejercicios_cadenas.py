#Escribir un programa que pregunte el nombre del usuario en la consola y un número entero e imprima por pantalla en líneas distintas el nombre del usuario tantas veces como el número introducido.
pregunta_cant = input("Ingrese su nombre de usuario: ")
veces_rep = int(input("Digite las veces que se repetirá el nombre: "))

print ((pregunta_cant + "\n") * veces_rep)


#Escribir un programa que pregunte el nombre completo del usuario en la consola y después muestre por pantalla el nombre completo del usuario tres veces, una con todas las letras minúsculas, otra con todas las letras mayúsculas y otra solo con la primera letra del nombre y de los apellidos en mayúscula. El usuario puede introducir su nombre combinando mayúsculas y minúsculas como quiera.
question_user = input("Ingrese su nombre: ")

print(question_user.lower())
print(question_user.upper())
print(question_user.title())


#Los teléfonos de una empresa tienen el siguiente formato prefijo-número-extension donde el prefijo es el código del país +34, y la extensión tiene dos dígitos (por ejemplo +34-913724710-56). Escribir un programa que pregunte por un número de teléfono con este formato y muestre por pantalla el número de teléfono sin el prefijo y la extensión.
numero = (input("La extensión es +34, ingrese el número: "))
comprobar_num = "+34"

if not numero.startswith(comprobar_num):
    numero = "+34-" + numero
    
prefijo_numero_extension = (input("Ingrese la extensión: "))
nuevo_num = numero.replace("+34-", "")

print("El número con el prefijo y la extensión es: \n", numero + "-" + prefijo_numero_extension)
print("El número sin el prefijo y con la extensión es: \n", nuevo_num + "-" + prefijo_numero_extension)


#Escribir un programa que pida al usuario que introduzca una frase en la consola y muestre por pantalla la frase invertida.
a_invertir = input("Ingrese un texto a invertir: ")
rebanada_inversa = a_invertir[::-1]

print(rebanada_inversa)

#Escribir un programa que pida al usuario que introduzca una frase en la consola y una vocal, y después muestre por pantalla la misma frase pero con la vocal introducida en mayúscula.
frase_ejercicio = input("Ingrese una frase: ")
vocal_mayuscula = input("Ingrese una vocal a poner en mayúscula: ")

print(frase_ejercicio.replace(vocal_mayuscula, vocal_mayuscula.upper()))

#Escribir un programa que pregunte el correo electrónico del usuario en la consola y muestre por pantalla otro correo electrónico con el mismo nombre (la parte delante de la arroba @) pero con dominio ceu.es.
correo = input("Ingrese su correo: ")
print(correo[:correo.find("@")] + "@ceu.es")

#Escribir un programa que pregunte por consola el precio de un producto en euros con dos decimales y muestre por pantalla el número de euros y el número de céntimos del precio introducido.
precio= input("ingrese el precio en euros con céntimos: ")
centimos = precio.split(".")[1]

print(f"Los euros fueron: ${precio}\nLos céntimos fueron: ¢{centimos}")

