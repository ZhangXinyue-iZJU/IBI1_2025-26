# import necessary libraries
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm

# 1. Define parameters
beta = 0.3      # Infection probability
gamma = 0.05    # Recovery probability
time_steps = 100

# 2. Initialize population grid (100x100)
# 0: Susceptible, 1: Infected, 2: Recovered
population = np.zeros((100, 100), dtype=int)

# Random initial outbreak point
outbreak = np.random.choice(range(100), 2)
population[outbreak[0], outbreak[1]] = 1

# 3. Plot initial state (time 0)
plt.figure(figsize=(4, 4), dpi=150)
plt.imshow(population, cmap='viridis', interpolation='nearest', vmin=0, vmax=2)
plt.title('Spatial SIR: Time 0')
plt.colorbar(ticks=[0, 1, 2], label='State (0:S, 1:I, 2:R)')
plt.savefig('spatial_SIR_time0.png', dpi=150, bbox_inches='tight')
plt.close()

# 4. Time loop
for t in range(1, time_steps + 1):
    # Create a copy of the population to avoid overwriting during updates
    new_population = population.copy()
    
    # Find coordinates of all infected individuals (state 1)
    infected_coords = np.where(population == 1)
    infected_list = list(zip(infected_coords[0], infected_coords[1]))
    
    # Step 1: Recovery (Infected -> Recovered)
    for (i, j) in infected_list:
        if np.random.rand() < gamma:
            new_population[i, j] = 2  # Recovered
    
    # Step 2: Infection spread to 8 neighbors
    for (i, j) in infected_list:
        # 8 neighbor coordinates
        neighbors = [
            (i-1, j-1), (i-1, j), (i-1, j+1),
            (i, j-1),          (i, j+1),
            (i+1, j-1), (i+1, j), (i+1, j+1)
        ]
        
        # Iterate over each neighbor
        for (ni, nj) in neighbors:
            # Check if neighbor is within grid bounds and susceptible
            if 0 <= ni < 100 and 0 <= nj < 100:
                if population[ni, nj] == 0:  # Only susceptible can be infected
                    if np.random.rand() < beta:
                        new_population[ni, nj] = 1  # New infection
    
    # Update population for next step
    population = new_population
    
    # Plot key time points (0, 10, 50, 100)
    if t in [10, 50, 100]:
        plt.figure(figsize=(4, 4), dpi=150)
        plt.imshow(population, cmap='viridis', interpolation='nearest', vmin=0, vmax=2)
        plt.title(f'Spatial SIR: Time {t}')
        plt.colorbar(ticks=[0, 1, 2], label='State (0:S, 1:I, 2:R)')
        plt.savefig(f'spatial_SIR_time{t}.png', dpi=150, bbox_inches='tight')
        plt.close()