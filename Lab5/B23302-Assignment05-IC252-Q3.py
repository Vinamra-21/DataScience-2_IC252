# 3. A random walk, sometimes known as a drunkard’s walk, is a random process that describes a path that consists of a
# succession of random steps on some mathematical space. An elementary example of a random walk is the random walk
# on the integer number line Z starts at 0 and moves +1 or −1 at each step with equal probability.
# (a) Simulate an elementary(equiprobable) 1D random walk experiment 10000 times. Let the number of steps n =
# (100,1000,10000). Plot the probability distribution of the final locations on the number line.
##########################################################################################################################

#import libraries
import numpy as np
import matplotlib.pyplot as plt

def random_walk(n_step, n_simu):    #simulate random walk
    loc_final = []
    for _ in range(n_simu):
        pos = 0
        for _ in range(n_step):
            pos += np.random.choice([-1, 1])    #randomly select 1,-1
        loc_final.append(pos)
    return loc_final

n_steps = [100, 1000, 10000]
n_simu = 1000

#histogram
shade = ["orange", "lightgreen", "skyblue"]
edge_shade = ["red", "green", "blue"]
plt.figure(figsize=(12,6))
for i,step in enumerate(n_steps):
    final_locs = random_walk(step, n_simu)
    plt.hist(final_locs, bins=50, alpha=0.7, label=f'{step} steps',color=shade[i], edgecolor=edge_shade[i])

# graph properties
plt.xlabel('Final Locations')
plt.ylabel('Frequency')
plt.title('Probability Distribution of Final Locations for Unbiased Random Walk')
plt.legend()
plt.grid(True)
plt.show()

# (b) Let the probability of going right = 0.6 and the probability of going left = 0.4. Repeat part a for the same.
#########################################################################################################################################
def rdm_wk_bsd(n_step, n_simu, prob_lr): #biased walk simulation
    bsd_loc_final = []
    for _ in range(n_simu):
        bsd_pos = 0
        for _ in range(n_step):
            bsd_pos += np.random.choice([-1, 1], p=[1-prob_lr, prob_lr])# Randomly select -1 or 1
        bsd_loc_final.append(bsd_pos)
    return bsd_loc_final

prob_r = 0.6 #right probab ##left=1-right

#histogram
plt.figure(figsize=(12,6))
for i,step in enumerate(n_steps):
    final_locs = rdm_wk_bsd(step, n_simu,prob_r)
    plt.hist(final_locs, bins=50, alpha=0.5,  label=f'{step} steps (prob_right={prob_r})',color=shade[i], edgecolor=edge_shade[i])

plt.xlabel('Final Locations')
plt.ylabel('Frequency')
plt.title('Probability Distribution of Final Locations for Biased Random Walk')
plt.legend()
plt.grid(True)
plt.show()



















