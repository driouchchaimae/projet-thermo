import sympy as sp #importe la bibliothéque(sympy) sous l'abréviation sp qui est spécialisée dans le calcul formel 

# Crée des variables mathématiques symboliques (T, v, R, a, b) et indique à SymPy qu'elles sont strictement positives (positive=True)
Ts, vs, Rs, aa, bb = sp.symbols("T v R a b", positive=True)

# Définir l'équation de pression du gaz de Van der Waals
P = Rs * Ts / (vs - bb) - aa / vs**2


dP_dT = sp.diff(P, Ts)#la fonction sp.diff calcule  automatiquement la dérivée de la pression P par rapport à la température 
dP_dv = sp.diff(P, vs)# la fonction sp.diff calcule  automatiquement la dérivée de la pression P par rapport au volume 


print("dP/dT =", sp.simplify(dP_dT))# la fonction sp.simplify simplifie l'écrituremathématique de la dérivée par rapport à la tepérature 
print("dP/dv =", sp.simplify(dP_dv))# la même chose pour la dérivée de la pression par rapport au volume 



# 2. VÉRIFICATION PAR DIFFÉRENCES FINIES


# Définir une fonction Python pour la pression de Van der Waals
def p_vdw(T_val, v_val, R_val, a_val, b_val):
    return (R_val * T_val) / (v_val - b_val) - a_val / (v_val**2)

# Définir des valeurs numériques pour les variables
R = 8.314    # J/(mol·K)
T = 300.0    # K
v = 0.025    # m³/mol
a = 0.1358   # Pa·m⁶/mol² (ex. pour l'air)
b = 0.0000364 # m³/mol

# Choisir un pas h
h = 0.01

# Calculer la dérivée numérique par rapport à T
dP_dT_num = (p_vdw(T + h, v, R, a, b) - p_vdw(T - h, v, R, a, b)) / (2 * h)

# Calculer la dérivée exacte théorique
dP_dT_exact = R / (v - b)

# Calculer l'erreur relative
erreur = abs(dP_dT_num - dP_dT_exact) / abs(dP_dT_exact)

# Afficher les résultats
print("Dérivée numérique :", dP_dT_num)
print("Dérivée exacte    :", dP_dT_exact)
print("Erreur relative   :", erreur)