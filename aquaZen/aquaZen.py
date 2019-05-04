#Simulemos el acuario!

#Librerías
import random

#Establecimiento del acuario


#Valores de inicio

day = 0
parameter1 = 0 
members = 3


#El día a día

for i in range(100):
    day = day + 1
    parameter1 += random.choice(.1, .2, .4)

    if parameter1 > .20:
        print("¡Necesitas hacer cambio de agua!")

    if parameter1 > .24:
        members -= 1
        print("Axólotl ha muerto.")

#Intervención en el parámetro. 

def cambio_de_agua():
    parameter1 = parameter1 - .15
    print("¡Cambiaste el agua!")


# Acuario establecido

if day > 16:
   parameter1 = 0.0
   print("El acuario se ha establecido")


# El acuario balanceado


#valores de inicio

day = 16
parameter1 = 2
parameter2 = 5
parameter3 = 5
parameter6 = 7

#acciones de control de parámetros
#interesante ver cómo interactúan

#alertas

#muertes



