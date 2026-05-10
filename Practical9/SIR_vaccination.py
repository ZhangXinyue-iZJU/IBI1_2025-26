# import necessary libraries
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm  # 可选，用于颜色映射

# 1. Define model parameters
N = 10000
beta = 0.3
gamma = 0.05
time_steps = 1000

# 2. Vaccination rates to test (0% to 100% in 10% increments)
vaccination_rates = [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]

# 3. Prepare plot
plt.figure(figsize=(8, 5), dpi=150)
colors = cm.viridis(np.linspace(0, 1, len(vaccination_rates)))  # 可选颜色映射

# 4. Simulate for each vaccination rate
for idx, v_rate in enumerate(vaccination_rates):
    # Initial conditions with vaccination
    V = int(N * v_rate)  # Vaccinated individuals (immune)
    S = N - 1 - V       # Susceptible individuals (total - vaccinated - 1 initial infected)
    I = 1               # Initial infected
    R = 0               # Recovered (excluding vaccinated)
    
    # Store infected count over time
    I_list = [I]
    
    for t in range(time_steps):
        infection_prob = beta * (I / N)
        new_infections = np.random.choice([0, 1], size=S, p=[1 - infection_prob, infection_prob]).sum()
        new_recoveries = np.random.choice([0, 1], size=I, p=[1 - gamma, gamma]).sum()
        
        S -= new_infections
        I += new_infections - new_recoveries
        R += new_recoveries
        
        I_list.append(I)
    
    # Plot the infected curve for this vaccination rate
    plt.plot(I_list, label=f'{int(v_rate*100)}%', color=colors[idx])

# 5. Customize plot
plt.xlabel('time')
plt.ylabel('number of infected people')
plt.title('SIR model with different vaccination rates')
plt.legend(title='Vaccination Rate', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()

plt.savefig('SIR_vaccination.png', dpi=150, bbox_inches='tight')
plt.show()