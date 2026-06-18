import matplotlib.pyplot as plt

proteins = ['P-INSR', 'P-IRS1', 'PIK3CA', 'P-AKT1']
trials = ['Noise 1', 'Noise 2', 'Noise 3']

plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['font.size'] = 11
plt.rcParams['axes.linewidth'] = 1.2

for protein in proteins:
    print(f"\n--- Enter data for {protein} ---")
    avg = float(input(f"Enter {protein} Average PAS: "))
    m1 = float(input(f"Enter {protein} Noise 1 value: "))
    m2 = float(input(f"Enter {protein} Noise 2 value: "))
    m3 = float(input(f"Enter {protein} Noise 3 value: "))
    measurements = [m1, m2, m3]
    
    fig, ax = plt.subplots(figsize=(6, 4))
    
    ax.axhline(y=avg, color='#d62728', linestyle='-', linewidth=2, label=f'Average PAS ({avg})')
    ax.scatter(trials, measurements, color='#1f77b4', s=100, zorder=3, label='Individual Trials')
    
    for i, val in enumerate(measurements):
        ax.vlines(trials[i], ymin=0, ymax=val, colors='#1f77b4', linestyles='dashed', alpha=0.7)
        
    ax.set_title(f'{protein} Stochastic Fluctuation Profile', fontweight='bold', pad=12)
    ax.set_ylabel('Pathway Activation Score (PAS)')
    ax.set_xlabel('Simulation Run')
    
    max_val = max(max(measurements), avg)
    ax.set_ylim(0, max_val * 1.2)
    
    ax.grid(axis='y', linestyle=':', alpha=0.5)
    ax.legend(loc='lower left')
    
    plt.tight_layout()
    plt.savefig(f'{protein}_drop_line_plot.png', dpi=300)
    plt.close()
    
    print(f"Successfully generated and saved {protein}_drop_line_plot.png")
