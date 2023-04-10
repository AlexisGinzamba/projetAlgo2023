# -*- coding: utf-8 -*-
"""
Created on Wed Apr  5 12:16:11 2023

@author: ALEX
"""

import numpy as np
import matplotlib.pyplot as plt
from math import*

x = [0.01]
v = [0]
t = [0]

h = 1e-3

# nous allons resoudre l'equation par la methode de difference fins

""""

# oscillation librer 


for i in range(0,10000):
    x.append(x[i]+h*v[i])
    v.append((1-h)*v[i]-100*h*x[i-1]+h*cos(10*i*h))
    t.append(i*h)

# nous l'avos mis en commentaire car deja plotés

"""




# oscillation force

for i in range(0,10000):
    x.append(x[i]+h*v[i])
    v.append((1-h)*v[i]-100*h*x[i-1]+h*cos(10*i*h))
    t.append(i*h)

a = np.array(x)
c = np.array(v)
tps = np.array(t)

Ep = 10*9.81*a

Ec = 0.5*10*(c**2)

Et = Ec + Ep


plt.plot(tps,Ep, color = 'blue' )
plt.label(Ep,'Energie potentiel')
plt.plot(tps,Ec, color = 'red' )
plt.label(Ec,'Energie cinetique') 
plt.plot(tps, Et, label = 'Energie mecanique total', color = 'green')
plt.label(Et,'Energie total')
plt.show()
   

