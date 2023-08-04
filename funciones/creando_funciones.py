#Creando una función simple
#def saludo ():
#    print("hola como andas") 
    
#saludo()

#Creando una funcion con parámetros
def saludar(nombre, genero):
    gnero = genero.lower()
    if(genero=="mujer"):
        genero = "Jóvena"
    else:
        genero= "jóven"
    print(f"Hola, {nombre}, {genero} como vas")
    
saludar()