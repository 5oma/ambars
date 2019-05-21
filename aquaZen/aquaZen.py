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



#parámetros

"""The critical water quality parameters that directly affect the axolotl's health include water temperature, ammonia (NH3), nitrite (NO2-), nitrate (NO3-), pH, carbonate hardness (KH, also known as alkalinity), general hardness (GH, also known as permanent hardness) and dissolved oxygen (DO). Additionally, some parameters have diurnal fluctuations. Imbalances in any one of these parameters may have an impact on others and these inter-relationships will be explained. But before the specifics of each water quality parameter is discussed, they must understand the nitrogen cycle."""


"""Several factors affect the performance of the biofilter and they include:

 Temperature (works between 12–58°C, most efficient between 28–36°C)

 The pH of the water (reactions occurring faster between a pH of 8–9, but is impeded at pH < 5)"""

 #Temperatura
 afecta = ["tasa metabólica", "monto de alimento", "crecimiento", "reproducción", "procesos fisiológicos", "función de enzimas", "sistema inmunológico", "actividad general"] 

rango de temperatura =  temperatura > 15 and temperatura < 20  

if temperatura > 24: 
    # axolotl innapetance
# hongo en la piel
    # flotamiento

#tratamiento
#enfriamento

def enfriar(axolotl):

#más antibiótico por si ocurre una infección bacterial

""" """

# pH
# El ph es una medida de la acidez del agua. 

if ph > 7 :
    "El agua es alcalina"
if ph < 7 :
    "El agua es acídica"

# Suciedad, o mucha materia orgánica baja el ph. 
# A 4.5 también se paran las funciones de la comunidad microbiana. 
# El cambio del parámetro debe ser gradual.

""" """

# amoníaco (NH3)
# los siguientes parámetros en
# https://www.vin.com/apputil/content/defaultadv1.aspx?id=7259211&pid=14365&print=1

















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
