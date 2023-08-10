#Permite extraer porciones de texto añadiéndolas a una nueva variable

texto = "ABCDEFGHIJKLMÑOPQURST"


fragmento = texto[2:6] #<-----------------------------------------
#                 |                                              |
#                 |                          Número en que termina
#      Número en que comienza


fragmento1 = texto[2:] #Si se deja el último valor vacío irá hasta el final de la cadena
fragmento2 = texto[:7] #Si se deja el primer valor vacío comienza en la posición 0 hasta la especificada
fragmento3 = texto[::2] #Si se añade un tercer valor saltará las posiciones indicadas
fragmento4 = texto[::-1] #Si se añade un elemento negativo en el tercer valor se escribirá la cadena al revés
print(fragmento4)