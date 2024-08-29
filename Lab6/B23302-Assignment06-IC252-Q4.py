# 4. Repeat the same procedure as asked in Q3 by sampling from Exponential distribution, where the parameter λ is given as
#    input by the user
###########################################################################################################################################

# import libraries
import numpy as np
import matplotlib.pyplot as plt

colors = ["orange", "lightgreen", "skyblue", "lightgrey", "cyan"]
edge_colors= ["red", "green", "blue", "black", "purple"]

# User input for lamda amd samp_size
lamda = float(input("Enter the lambda of the exponential distribution: "))
samp_size = int(input("Enter the size of each sample: "))
number_samp = 5 
prt_saps = 10000

# generating the random exponential samples
def gen_saps(lamda, sap_sz, nm_saps):
    saps = np.random.exponential(scale = 1/lamda, size=(nm_saps, sap_sz))
    return saps


# Generating the exponential distribution
samples = gen_saps(lamda, samp_size, number_samp)

# Plotting the same
plt.figure(figsize=(10, 6))
plt.hist(np.random.exponential(scale=1/lamda, size = prt_saps), bins = 51 , alpha=0.7, label='Parent Distribution', color='yellow', edgecolor='brown')
for i in range(3):
    plt.hist(samples[i], bins=51, alpha=0.7, label=f'Sample {i+1}', color = colors[i],ec =edge_colors[i])

plt.title('Random Samples of Exponential Distribution')
plt.xlabel('Values')
plt.ylabel('Frequency')
plt.legend()
plt.grid(False)
plt.show()

# Function to calculate means & vars
def cal_stats(samples):
    samp_means = np.mean(samples, axis=1)
    samp_vars = np.var(samples, axis=1)
    return samp_means, samp_vars

# fxn call of same
samp_means, samp_vars = cal_stats(samples)

#   mean and var of the parent
parent_mean = 1 / lamda
parent_var = 1 / (lamda**2)

# Printing the same
print("Mean and Var. of Random Samples:")
for i, (mean, var) in enumerate(zip(samp_means, samp_vars)):
    print(f"Sample {i+1}: Mean = {mean}, Var. = {var}")

# Printing for the parent
print(f"\nMean and Variance of Parent:\n Mean = {parent_mean} \n Var. = {parent_var}")

max_obs_len = 500


# Initializing the required
samp_sizes = list(range(1, max_obs_len + 1))
dif_means = []
dif_vars = []

# Generating the random samples
for sap_size in samp_sizes:
    samples = gen_saps(lamda, sap_size, number_samp)
    samp_means, samp_vars = cal_stats(samples)
    dif_means.append(np.mean(samp_means))
    dif_vars.append(np.mean(samp_vars))

# Plotting mean and var. with sample size
plt.figure(figsize=(10, 6))
plt.plot(samp_sizes, dif_means, label='Sample Mean', marker='*')
plt.plot(samp_sizes, dif_vars, label='Sample Var.', marker='*')
plt.axhline(y=parent_mean, color='r', linestyle='--', label='True Mean')
plt.axhline(y=parent_var, color='g', linestyle='--', label='True Var.')
plt.xlabel('Sample Size')
plt.ylabel('Value')
plt.title('Mean and Var. vs. Sample Size')
plt.legend()
plt.grid(True)
plt.show()
