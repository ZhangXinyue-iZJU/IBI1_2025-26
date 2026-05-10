# import necessary libraries
import numpy as np
import matplotlib.pyplot as plt

# 1. Define model parameters
N = 10000
beta = 0.3
gamma = 0.05

# 2. Initial conditions
S = N - 1
I = 1
R = 0

# 3. Lists to store time series data
S_list = [S]
I_list = [I]
R_list = [R]

# 4. Time loop (1000 steps)
for t in range(1000):
    # Calculate infection probability
    infection_prob = beta * (I / N)
    
    # New infections: susceptible individuals getting infected
    new_infections = np.random.choice([0, 1], size=S, p=[1 - infection_prob, infection_prob]).sum()
    
    # New recoveries: infected individuals recovering
    new_recoveries = np.random.choice([0, 1], size=I, p=[1 - gamma, gamma]).sum()
    
    # Update S, I, R
    S -= new_infections
    I += new_infections - new_recoveries
    R += new_recoveries
    
    # Append to lists
    S_list.append(S)
    I_list.append(I)
    R_list.append(R)

# 5. Plot the results
plt.figure(figsize=(6, 4), dpi=150)
plt.plot(S_list, label='susceptible', color='blue')
plt.plot(I_list, label='infected', color='orange')
plt.plot(R_list, label='recovered', color='green')

plt.xlabel('time')
plt.ylabel('number of people')
plt.title('SIR model')
plt.legend()

plt.savefig('SIR_model.png', dpi=150, bbox_inches='tight')
plt.show()