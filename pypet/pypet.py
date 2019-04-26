# -*- coding: utf-8 -*-

photo = "W(o_.._o)W"
name = "Axolotl, el mágico anfibio mexicano." 
age = 5
weight = 5.5
hungry = True

def startup_pypet():
    print("Hola! Recuerda cuidar tu axolotl virtual.")
 

def pypet_stats():
    print("Hola, mi nombre es " + name)
    print(name + " pesa " + str(weight) + " kilogramos ")

if hungry: 
    print("Tu axolote tiene hambre.")
else: 
    print("Estoy lleno. ¡Gracias!")

startup_pypet()
pypet_stats()

terminate = False

while not terminate:
    print("ZZZZZZZZZZZZZZZZZZZZZZZZZZZZZ")

    user_input = raw_input("> ")

    if user_input == "quitar":
         terminate = True

    elif user_input == "estadísticas":
        pypet_stats()
    
    elif user_input == "alimentar":
	weight = weight + 0.1
        hungry = False
        print("¡Yum! ¡Qué rico!") 
 
    else:
         print("Lo siento, hubo un error.")

print "¡Hasta pronto!"


