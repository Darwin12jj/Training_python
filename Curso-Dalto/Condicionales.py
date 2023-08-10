#-*- coding: utf-8 -*-

# IF // SI 
# El código se ejecuta en caso de que
# la condición se culpa de manera adecuada.

# ELSE // DE LO CONTRARIO
# Se ejecuta otro código en caso que no se repita.
 
edad = int(input("Ingrese su edad: "))
edad_ecu = int(18 - edad)

if edad >= 18: 
    print("Eres mayor de edad")
    
elif edad >= 16:
    print("Tienes", edad, "años, ya casi alcanza la edad necesaria, le faltan", edad_ecu, " años para la mayoría de edad")

    
else:
    print("Tienes", edad, "años, eres un bebé, aún te faltan", edad_ecu ,"años para la mayoría de edad")