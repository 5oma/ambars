# -*- coding: utf-8 -*-

import random

axolotl = {
    "photos": [" W(o_.._o)W "," ≽(◕ ᴗ ◕ )≼ ", " ≽(♥ ᴗ ♥ )≼ ", " ≽(^ ᗜ ^)≼ ", " ≽(O _ o)≼  ", " ≽ (◝ _ ◜)≼  "," ≽ (⊙ _ ⊙ )≼, ", " ≽( ᵕ ‿ ᵕ)≼  ", " ≽(° ∩ °)≼ ", " ≽(ට ~ ට)≼  ", " ≽(★ ᴗ ★ )≼  ", " ≽ (⌐ _ ⌐ )≼  ", " ≽(˘ ∩ ˘)≼  "],  
    "name": "Axólotl, el mágico anfibio mexicano.",
    "weight": 1.1,
    "age" : 2,
    "hungry": True,
    "feeding": " ≽(^ ᗜ ^)≼  ",
    "phrases": ["Soy el ser de las profundidades.", "La naturaleza es el camino de regreso a casa.", "Sólo toma el camino más natural a tu alcance.", "Flow system", "Hack, amigo, hack!"] 
}


print random.choice(axolotl["photos"])

def startup_pypet():
    print("Hola! Recuerda cuidar tu axolotl virtual.")

startup_pypet() 

def pypet_stats():
    print("Hola, mi nombre es " + axolotl["name"])
    print random.choice(axolotl["photos"])
    print("Peso: " + str(axolotl["weight"]))

if axolotl["hungry"]: 
    print("Tu axolote tiene hambre.")
else: 
    print("Estoy lleno. ¡Gracias!")


terminate = False

while not terminate:
    print("ooooooooooo")

    user_input = raw_input("> ")

    if user_input == "quitar":
         terminate = True

    elif user_input == "estadísticas":
        pypet_stats()
    
    elif user_input == "alimentar":
	axolotl["weight"] = axolotl["weight"] + 0.1
        hungry = False
        print("¡Yum! ¡Qué rico!")
        print(axolotl["feeding"]) 

    elif user_input == "textear":
	print random.choice(axolotl["phrases"])
        print random.choice(axolotl["photos"])
 
    else:
         print("Lo siento, hubo un error.")

print "¡Hasta pronto!"
print random.choice(axolotl["photos"])

