import numpy as np  # Importe la bibliothèque NumPy sous l'abréviation np pour gérer les tableaux et les comparaisons numériques

# Définition des constantes et des variables nécessaires
R = 8.314                                    
a = 0.1358                                  
b = 0.0000364                                 
T = 300.0                                    
v = 0.025                                    

def cp_moins_cv_vdw(T, v): # Définit la fonction qui calcule la différence Cp - Cv pour un gaz de Van der Waals
    dpdt = R/(v-b)  # Calcule la dérivée partielle de la pression par rapport à la température (∂P/∂T)
    dpdv = -R*T/(v-b)**2 + 2*a/v**3 # Calcule la dérivée partielle de la pression par rapport au volume (∂P/∂v)
    if np.any(np.isclose(dpdv, 0, atol=1e-12)): #  Cette fonction teste si la valeur de dpdv (la dérivée de la pression par rapport au volume) est extrêmement proche de 0
        raise ValueError("Derivee en volume proche de zero") # Déclenche une erreur si la dérivée est trop proche de zéro
    return -T*dpdt**2/dpdv  # Retourne le résultat de la relation thermodynamique Cp - Cv

print("Cp-Cv ideal :", R)  # Affiche la valeur de Cp - Cv pour un gaz parfait (qui est égale à R)
print("Cp-Cv VdW :", cp_moins_cv_vdw(T,v))  # Affiche la valeur de Cp - Cv calculée par la fonction pour le gaz de Van der Waals