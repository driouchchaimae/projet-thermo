a = 0.364
v1 = 1.0e-3
v2 = 2.0e-3                                    
delta_U_vdw = a*(1/v1 - 1/v2)  # Calcule la variation d'énergie interne (Delta U) pour un gaz de Van der Waals entre les volumes v1 et v2
delta_U_ideal = 0.0  # Variation d'énergie interne pour un gaz parfait (nulle car l'énergie interne d'un gaz parfait ne dépend que de la température)
print("Delta U Van der Waals (J/mol) :", delta_U_vdw) # Affiche le résultat du calcul de Delta U pour le gaz de Van der Waals dans la console