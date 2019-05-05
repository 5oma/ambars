"""¡Simulemos el acuario!

"""

#Librerías
import random

"""Establecimiento del acuario

Al iniciar nuestro acuario
con agua nueva y ocupantes, 
el filtro nuevo (sin comunidad
microbiana asentada) es fácilmente
rebasado. 

La conversión de nitrogenados a
compuestos nitrogenados inofensivos no 
es suficiente, y los nitrogenados 
se convierten en amoniáco por oxidación, 
el cual es tóxico en pequeñas
concentraciones. 
 
"""

# Valores de inicio

day = 0
parameter1 = 0 
members = 3


# Día a día

for i in range(100):
    day = day + 1
    parameter1 += random.choice(.1, .2, .4)

    if parameter1 > .20:
        print("¡Necesitas hacer cambio de agua!")

    if parameter1 > .24:
        members -= 1
        print("Axólotl ha muerto.")

# Intervención en el parámetro. 

def cambio_de_agua():
    parameter1 = parameter1 - .15
    print("¡Cambiaste el agua!")


# Acuario establecido

if day > 16:
   parameter1 = 0.0
   print("El acuario se ha establecido")





""" El acuario balanceado

Una vez solucionado el establecimiento de
un acuario, comenzamos a realizar tareas
de mantenimiento con menores cambios de
agua. 

Algunos parámetros importantes en el
mantenimiento.  

PH



"""

#rangos para parámetros

if parameter1 > x and parameter1 < y:
    print("Parámetro dentro de su rango")
elif parameter1 > m and parameter1 < j;
    print("Parámetro en zona de peligro")
else: 
    print("Parámetro fuera de control")

 

#valores de inicio

day = 16
parameter1 = 2
parameter2 = 5
parameter3 = 5
parameter4 = 7



#acciones en el acuario que desembocan en
#picos de amoniáco

#Introducción de especia




#de control de parámetros






# día a día

# cambios o limpias de filtro

# salida de control

# interesante colocar algunas interacciones

#alertas

#muertes
