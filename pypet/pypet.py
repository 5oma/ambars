# -*- coding: utf-8 -*-

import random

axolotl = {
    "photo": "W(o_.._o)W", 
    "name": "Axólotl, el mágico anfibio mexicano.",
    "weight": 1.1,
    "age" : 2,
    "hungry": True,
    "phrases": ["Soy el ser de las profundidades.", "La naturaleza es el camino de regreso a casa.", "Sólo toma el camino más natural a tu alcance.", "Flow system", "Hack, amigo, hack!"] 
}


print(axolotl["photo"])

def startup_pypet():
    print("Hola! Recuerda cuidar tu axolotl virtual.")
 

def pypet_stats():
    print("Hola, mi nombre es " + axolotl["name"])
    print("Peso: " + str(axolotl["weight"]))

if axolotl["hungry"]: 
    print("Tu axolote tiene hambre.")
else: 
    print("Estoy lleno. ¡Gracias!")


terminate = False

while not terminate:
    print("ZZZZZZZZZZZZZZZZZZZZZZZZZZZZZ")

    user_input = raw_input("> ")

    if user_input == "quitar":
         terminate = True

    elif user_input == "estadísticas":
        pypet_stats()
    
    elif user_input == "alimentar":
	axolotl["weight"] = axolotl["weight"] + 0.1
        hungry = False
        print("¡Yum! ¡Qué rico!") 

    elif user_input == "textear":
	print random.choice(axolotl["phrases"])
 
    else:
         print("Lo siento, hubo un error.")

print "¡Hasta pronto!"
print axolotl["photo"]

