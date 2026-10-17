import numpy as np 
R = 8.314462618
a = 0.364
b = 4.267e-5
def p_ideal(T, v):
      return R*T/v
def p_vdw(T, v):    
      if np.any(np.asarray(v) <= b):
              raise ValueError("Le volume doit etre superieur a b")   
      return R*T/(v-b) - a/v**2
T = 320.0
v = 1.0e-3 
print("Gaz parfait (bar) :", p_ideal(T,v)/1e5) 
print("Van der Waals (bar) :", p_vdw(T,v)/1e5)