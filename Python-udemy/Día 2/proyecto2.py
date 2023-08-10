nombre = input("¿Cual es tu nombre?\n")
ventas = float(input("¿Cuantas ventas has hecho?\n"))

print(f"Ok {nombre}.\nEste mes ganaste {round(ventas * 13/100, 2)}$")