import numpy as np  #  Importe la bibliothèque NumPy sous l'abréviation np pour gérer les tableaux et les comparaisons numériques
import matplotlib.pyplot as plt # Importe La bibliothéque Matplotlib pour la création et l'affichage des graphiques
R = 8.314                                                    
a = 0.1358                                                   
b = 0.0000364                                                
T = 320.0                                                    
def p_ideal(T_val, v_val):   # Définit la fonction calculant la pression d'un gaz parfait : P = R*T / v
    return (R * T_val) / v_val
def p_vdw(T_val, v_val): # Définit la fonction calculant la pression d'un gaz de Van der Waals : P = R*T/(v-b) - a/v²
    return (R * T_val) / (v_val - b) - a / (v_val**2)
volumes = np.linspace(5e-4, 5e-3, 250)# Génère un tableau de 250 valeurs de volume molaire réparties régulièrement entre 0.0005 et 0.005 m³/mol
plt.plot(volumes, p_ideal(T, volumes) / 1e5, label="Gaz parfait") # plt.plot(...) : C'est la fonction de la bibliothèque Matplotlib qui permet de dessiner un graphique en 2D .volumes: Représente les valeurs de l'axe des abscisses .p_ideal(T, volumes) / 1e5 : Représente les valeurs de l'axe des ordonnées (Y):Elle appelle la fonction p_ideal pour calculer la pression du gaz parfait à la température T pour chaque volume.Elle divise le résultat par 10^5 (1e5) pour convertir la pression de Pascals (Pa) en bars (
plt.plot(volumes, p_vdw(T, volumes) / 1e5, label="Van der Waals") # plt.plot(...) : la meme chose mais elle apelle la fonction de van der walls
plt.xlabel("Volume molaire (m3/mol)") # plt.xlabel(...) : C'est la fonction de Matplotlib qui permet de nommer l'axe des abscisses."Volume molaire (m3/mol)" : C'est le texte qui s'affichera directement sous l'axe X, indiquant la grandeur représentée (le volume molaire) ainsi que son unité de mesure (m^3/mol).
plt.ylabel("Pression (bar)") # Ajoute un nom/étiquette sur l'axe des ordonnées (Y)
plt.title("Isotherme a T = 320 K") # Définit le titre principal du graphique
plt.grid(True)  # Affiche une grille en arrière-plan pour faciliter la lecture des valeurs
plt.legend()  # Affiche la légende identifiant chaque courbe selon les étiquettes ("label")
plt.tight_layout()# Ajuste automatiquement les marges de la figure pour éviter les chevauchements
plt.show()  # Ouvre la fenêtre d'affichage du graphique