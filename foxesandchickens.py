# -*- coding: utf-8 -*-

#iniciando población
chickens = [100]
foxes = [10]

#definiendo las tasas
chicken_birth_rate = 0.5
chicken_death_rate = 0.015
fox_birth_rate = 0.015
fox_death_rate = 0.5

#definiendo tiempo 
delta_time = 0.01
cycles = 4500

#ahora sí... el modelo
for t in range(0, cycles):
    updated_chickens = chickens[t] + delta_time * (chicken_birth_rate * chickens[t] - chicken_death_rate * foxes[t] * chickens[t])
    updated_foxes = foxes[t] + delta_time * (- fox_death_rate * foxes[t] + fox_birth_rate * foxes[t] * chickens[t])
    chickens.append(updated_chickens)
    foxes.append(updated_foxes)

#visualizando

import matplotlib.pyplot as plt
time_points = range(cycles + 1)
plt.plot(time_points, foxes)
plt.plot(time_points, foxes)
plt.plot(time_points, chickens)
plt.xlabel("time")
plt.show()
