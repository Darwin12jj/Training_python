#Creando las listas
frutas = ["banana", "manzana", "papaya", "guayaba"]
for fruit in frutas :
    if fruit == "banana":
        continue 
    print(f"Me voy a comer una {fruit}")
else:
    print(f"\nNo me gusta la {frutas[0]}\n")
    
#Evitar que el bucle siga ejecutándose
for fruta in frutas:
    if fruta == "papaya":
        break
    print(f"Voy a comer una {fruta}")
print ("Bucle terminado.")

#Recorrer/iterar cadena de texto
cadena = "Hola soxix"
for letra in cadena: 
    print (letra)
    

#Bucle FOR en una sola línea de código
#SIN OPTIMIZAR
numeros = [2,4,5,6,7]
#numeros_duplicados = list()
#for numero in numeros: 
#    numeros_duplicados.append(numero*10)
#print(f"Los numeros multiplicados por 10 son: {numeros_duplicados}")

numeros_duplicados = [x*10 for x in numeros]
print(numeros_duplicados)