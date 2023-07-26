
# Escribir un programa que muestre por pantalla la cadena ¡Hola Mundo!.
print ("Hola mundo!")

#Escribir un programa que almacene la cadena ¡Hola Mundo! en una variable y luego muestre por pantalla el contenido de la variable.
variable = "Hola mundo"
print(f"la variable es", variable)

#Escribir un programa que pregunte el nombre del usuario en la consola y después de que el usuario lo introduzca muestre por pantalla la cadena ¡Hola <nombre>!, donde <nombre> es el nombre que el usuario haya introducido.

nombre = input("ingrese su nombre: ")
print ("Hola,", nombre)

#Escribir un programa que muestre por pantalla el resultado de la siguiente operación aritmética 
operacion = (((3+2)/(2*5)) ** 2)
print ("El resultado de la operación es:", operacion)

#Escribir un programa que pregunte al usuario por el número de horas trabajadas y el coste por hora. Después debe mostrar por pantalla la paga que le corresponde.
horas_trabajadas = int(input("Indique las horas que trabajó: "))
costo_por_hora = int(input("Indique el costo por hora: "))
paga = horas_trabajadas * costo_por_hora

print ("Hola,", nombre, "Su paga es:", paga, "Dolarucos")

#Escribir un programa que pida al usuario su peso (en kg) y estatura (en metros), calcule el índice de masa corporal y lo almacene en una variable, y muestre por pantalla la frase Tu índice de masa corporal es <imc> donde <imc> es el índice de masa corporal calculado redondeado con dos decimales.
question_kg = (input("Ingrese su peso en kilogramos: "))
question_mt = (input("Ingrese su altura en metros: "))
result_mass = round(float(question_kg) / float(question_mt)**2,2)
print (nombre ,"El indice de su masa corporal redondeado es:", str(result_mass))

#Escribir un programa que pida al usuario dos números enteros y muestre por pantalla la <n> entre <m> da un cociente <c> y un resto <r> donde <n> y <m> son los números introducidos por el usuario, y <c> y <r> son el cociente y el resto de la división entera respectivamente.

pregunta1 = int(input("Ingrese un número: "))
pregunta2 = int(input("Ingrese un segundo número: "))

c = float(pregunta1 / pregunta2)
r = float(pregunta1 % pregunta2)

print ("El cociente de los números es :", c)
print ("El resto de los números es :", r)

#Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y el número de años, y muestre por pantalla el capital obtenido en la inversión.

inversion = int(input("Ingrese una cantidad a invertir"))
int_anual = int(input("Ingrese el interés anual"))
años = int(input("Ingrese el numero de años"))

cap_obtenido = round(inversion * (int_anual /100 + 1)** años, 2)
print(cap_obtenido)

#Una juguetería tiene mucho éxito en dos de sus productos: payasos y muñecas. Suele hacer venta por correo y la empresa de logística les cobra por peso de cada paquete así que deben calcular el peso de los payasos y muñecas que saldrán en cada paquete a demanda. Cada payaso pesa 112 g y cada muñeca 75 g. Escribir un programa que lea el número de payasos y muñecas vendidos en el último pedido y calcule el peso total del paquete que será enviado.

cant_payasos = int(input("Ingrese el número de payasos vendidos en el último pedido:"))
cant_muñecas = int(input("Ingrese el número de muñecas vendidos en el último pedido:"))

peso_pay = cant_payasos * 112
peso_muñ = cant_muñecas * 75

peso_total = peso_pay + peso_muñ
print(nombre, "el total en peso de su pedido es de:", str(peso_total), "Gramos")

#Imagina que acabas de abrir una nueva cuenta de ahorros que te ofrece el 4% de interés al año. Estos ahorros debido a intereses, que no se cobran hasta finales de año, se te añaden al balance final de tu cuenta de ahorros. Escribir un programa que comience leyendo la cantidad de dinero depositada en la cuenta de ahorros, introducida por el usuario. Después el programa debe calcular y mostrar por pantalla la cantidad de ahorros tras el primer, segundo y tercer años. Redondear cada cantidad a dos decimales.

intereses = 0.04
depositado= float(input("Ingrese la cantidad depositada:"))

primer_mes = depositado * (1 + intereses)
print ("El primer año se depositaron: ", round(primer_mes, 2))

segundo_mes = primer_mes * (1 + intereses)
print ("El segundo año se depositaron: ", round(segundo_mes, 2))

tercer_mes = segundo_mes * (1 + intereses)
print ("El segundo año se depositaron: ", round(tercer_mes, 2))

#Una panadería vende barras de pan a 3.49€ cada una. El pan que no es el día tiene un descuento del 60%. Escribir un programa que comience leyendo el número de barras vendidas que no son del día. Después el programa debe mostrar el precio habitual de una barra de pan, el descuento que se le hace por no ser fresca y el coste final total.

pregunta_pan = int(input("Ingrese las barras vendidas que no son del día: "))
barra_pan = 3.49
descuento_pan = 0.6 
costo_final_pan =  pregunta_pan * barra_pan * (1 - descuento_pan)
print("La barra de pan habitualmente cuesta", str(barra_pan),"€")
print("Se realizará descuento por no estar fresca, será un descuento del:", str(descuento_pan * 100), "%")
print("El costo final será: ", str(round(costo_final_pan, 2)), "€")