import numpy as np


true_baselines  = {"p-INSR": 0.02, "p-IRS1": 0.05, "PIK3CA": 0.10, "p-AKT1": 0.01}
true_peaks      = {"p-INSR": 0.85, "p-IRS1": 0.78, "PIK3CA": 0.65, "p-AKT1": 0.88}


noise_level = 0.10
proteins = ["p-INSR", "p-IRS1", "PIK3CA", "p-AKT1"]


for p in proteins:
    
    noisy_pre  = max(0.001, np.random.normal(true_baselines[p], noise_level * true_baselines[p]))
    noisy_post = max(0.001, np.random.normal(true_peaks[p], noise_level * true_peaks[p]))
    
    
    fold_change = noisy_post / noisy_pre
    
    
    historical_control_sd = true_baselines[p] * noise_level
    z_score = (noisy_post - true_baselines[p]) / historical_control_sd
    
    
    combined_score = fold_change * z_score
    max_theoretical_score = (true_peaks[p] / true_baselines[p]) * ((true_peaks[p] - true_baselines[p]) / historical_control_sd)
    normalized_pas = np.clip(combined_score / max_theoretical_score, 0.00, 1.00)
    
    print(f"{p} PAS: {normalized_pas:.4f}")
