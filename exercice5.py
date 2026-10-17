import sympy as sp  # Importe la bibliothèque SymPy pour le calcul symbolique
import numpy as np   # Importe la bibliothèque NumPy pour les calculs numériques
R = 8.314     
T = 300.0      
v = 0.025       
a = 0.1358      
b = 0.0000364   
# Définition des variables symboliques positives
Ts, vs, Rs, aa, bb = sp.symbols("T v R a b", positive=True) # sp.symbols Elle sert à créer des variables mathématiques symboliques (littérales) pour faire du calcul algébrique sur ordinateur, (positive true);indique que les variables sont strictement positives.
# Définition de l'équation de pression du gaz de Van der Waals
P = Rs * Ts / (vs - bb) - aa / vs**2               
# Calcul des dérivées partielles analytiques
dP_dT = sp.diff(P, Ts)  # Calcule la dérivée partielle de P par rapport à la température Ts
dP_dv = sp.diff(P, vs)  # Calcule la dérivée partielle de P par rapport au volume v
# la fonction sp.simplify() Calcule et simplifie l'expression de la dérivée du volume par rapport à T à P constant
dvdT_P = sp.simplify(-dP_dT / dP_dv)              
valeur = dvdT_P.subs({Ts: T, vs: v, Rs: R, aa: a, bb: b}) # Substitue les symboles par les variables numériques

# Affiche les résultats convertis en nombres à virgule flottante
print("(dv/dT)P :", float(valeur)) # Affiche la valeur numérique convertie en float pour (∂v/∂T)_P
print("(dS/dP)T :", -float(valeur)) # Affiche la valeur de (∂dS/∂P)_T en utilisant les relations de Maxwell (- (∂v/∂T)_P)