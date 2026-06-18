import numpy as np
from scipy.integrate import odeint


def isc_system(y, t):
    pINSR, pIRS1, PIK3CA, pAKT1 = y
    
   
    insulin = 1.0
    
   
    k1, k2, k3, k4 = 0.6, 0.5, 0.4, 0.3
    decay = 0.15
# Parameters chosen phenomenologically for idealized baseline cascade
    
    
    dpINSR  = (k1 * insulin * (1.0 - pINSR)) - (decay * pINSR)
    dpIRS1  = (k2 * pINSR * (1.0 - pIRS1)) - (decay * pIRS1)
    dPIK3CA = (k3 * pIRS1 * (1.0 - PIK3CA)) - (decay * PIK3CA)
    dpAKT1  = (k4 * PIK3CA * (1.0 - pAKT1)) - (decay * pAKT1)
    
    return [dpINSR, dpIRS1, dPIK3CA, dpAKT1]

time_points = np.linspace(0, 30, 300)
initial_state = [0.0, 0.0, 0.0, 0.0] 
trajectories = odeint(isc_system, initial_state, time_points)

total_time = 30.0
proteins = ["p-INSR", "p-IRS1", "PIK3CA", "p-AKT1"]

for i, name in enumerate(proteins):
    auc = np.trapz(trajectories[:, i], time_points)
    normalized_pas = auc / total_time
    print(f"{name} PAS: {normalized_pas:.4f}")
