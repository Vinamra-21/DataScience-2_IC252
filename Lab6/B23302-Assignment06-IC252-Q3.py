# 3. Generate atleast five different random samples of size n from Normal distribution(where the mean and standard deviation
#    are given as input by the user) and
#    (a) Plot any three random samples in a single plot and compare them with the parent distribution to visually assess their
#        similarities or differences.
#    (b) Calculate the mean and variance of the random samples and compare them with the statistics of the parent distribution.
#    (c) Observe how the characteristics of the random samples change as the sample size n increases. Check for any trends
#        or patterns observed in the plots and statistical summaries 
# #########################################################################################################################################################

# importing the required libreries
import numpy as np
import matplotlib.pyplot as plt


# values
mean = float(input("Enter the mean of the normal distribution: "))
std = float(input("Enter the standard deviation of the normal distribution: "))
samp_size = int(input("Enter the size of each sample (>1000): "))
n_samps = 5 
prt_saps = 10000
max_n_samp = 500

colors = ["orange", "lightgreen", "skyblue", "lightgrey", "cyan"]
edge_colors = ["red", "green", "blue", "black", "purple"]


# defining the random samples
def gen_sap(mean, std, samp_size, n_samps):
    saps = np.random.normal(mean, std, size=(n_samps, samp_size))
    return saps


# generating the same
saps = gen_sap(mean, std, samp_size, n_samps)

# Plotting the same
plt.figure(figsize=(10, 6))
plt.hist(np.random.normal(mean, std, size = prt_saps), bins = 51 , alpha=0.7, label='Parent Distribution', color='yellow', edgecolor='brown')
for i in range(3):
    plt.hist(saps[i], bins=30, alpha=0.5, label=f'Sample {i+1}',color = colors[i], ec = edge_colors[i]) 

plt.title('Comparison of Random Samples with Parent Distribution')
plt.xlabel('Values')
plt.ylabel('Frequency')
plt.legend()
plt.grid(False)
plt.show()

# Stats of the random defined
samp_mean = np.mean(saps, axis=1)
samp_var = np.var(saps, axis=1)

# Stats of the parent
parent_mean = mean
parent_var = std**2

# Printing for the random samples
print("Mean and Var. of Random Samples:")
for i in range(n_samps):
    print(f"Sample {i+1}: Mean = {samp_mean[i]}, Var. = {samp_var[i]}")

# Printing for the parent
print(f"\nMean and Var. of Parent Dist.:\n Mean = {parent_mean}\n Var. = {parent_var}")


# Function to find the stats
def cal_stats(saps):
    sap_means = np.mean(saps, axis=1)
    sap_stds = np.std(saps, axis=1)
    return sap_means, sap_stds


# Initialization for the required
sap_szs = list(range(1, max_n_samp + 1))
diff_means = []
diff_std_dev = []

# Generating the random values for all simulations
for samp_size in sap_szs:
    saps = gen_sap(mean, std, samp_size, n_samps)
    samp_mean, sap_stds = cal_stats(saps)
    diff_means.append(np.mean(samp_mean))
    diff_std_dev.append(np.mean(sap_stds))

# Plotting mean and std with sample sizes
plt.figure(figsize=(10, 6))
plt.plot(sap_szs, diff_means, label='Mean', marker='*')
plt.plot(sap_szs, diff_std_dev, label='Std. Dev.', marker='*')
plt.axhline(y = mean, color='r', linestyle='--', label='True Mean')
plt.axhline(y = std, color='g', linestyle='--', label='True Std. Dev.')
plt.xlabel('Sample Size')
plt.ylabel('Value')
plt.title('Mean and Std. Dev. vs Sample Size')
plt.legend()
plt.grid(False)
plt.show()

