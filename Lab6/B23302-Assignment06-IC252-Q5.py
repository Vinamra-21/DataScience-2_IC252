# 5. Let the marks of students in a class are normally distributed with mean 65 and standard deviation 15. Then,
# (a) Generate five random samples of size 50 and calculate their statistics. Also, plot the histogram of these samples and
#     the total population in a single graph.
# (b)  Again generate random samples of size 100, 150 and 250, and observe their statistics and histogram.
# (c)  Think of any other sampling strategy different form random sampling. Use it to generate samples of different sizes
#      from the population. Calculate their statistics and plot the histogram.
# (d)  Compare the statistics of the random sampling and the sampling from part c. Are they close to what is in the
#      population? Is there any bias one way or the other? Is the variance too high or too low?
# ######################################################################################################################################################

# import libraries
import numpy as np
import matplotlib.pyplot as plt

# Values
mean = 65
std_dev = 15
n_samp = 50
diff_samp = 5
samp_size = [100, 150, 250, 500]
popu_size = 1000  # Assuming

# generate samples 
samps = np.random.normal(mean, std_dev, size=(diff_samp, n_samp))

# Calculating mean and std for all
samp_mean = np.mean(samps, axis=1)
samp_std_dev = np.std(samps, axis=1)


colors = ["orange", "lightgreen", "skyblue", "lightgrey", "cyan"]
edge_colors = ["red", "green", "blue", "black", "purple"]

plt.figure(figsize=(10, 6))
plt.hist(np.random.normal(mean, std_dev, size=1000), bins=30, alpha=0.5, label='Parent Histogram', color="skyblue", edgecolor="black")
for i in range(diff_samp):
    plt.hist(samps[i], bins=30, alpha=0.5, label = f'Sample {i+1}', color = colors[i], ec = edge_colors[i])

plt.title('Histogram for all distribution')
plt.xlabel('Marks')
plt.ylabel('Frequency of Marks')
plt.legend()
plt.grid(False)
plt.show()

# print the stats
for i in range(diff_samp):
    print(f"Sample {i+1} Mean: {samp_mean[i]}, Std. Dev.: {samp_std_dev[i]}")


# generate samples and stats 
samp_data = {}
for sz in samp_size:
    samps = np.random.normal(mean, std_dev, size = (diff_samp, sz))
    samp_mean = np.mean(samps, axis=1)
    samp_std_dev = np.std(samps, axis=1)
    samp_data[sz] = {'samples': samps, 'means': samp_mean, 'stds': samp_std_dev}


# define the size and plot
plt.figure(figsize=(15, 10))
for i, sz in enumerate(samp_size):
    plt.subplot(2, 2, i+1)
    plt.hist(np.random.normal(mean, std_dev, size = 1000), bins=30, alpha=0.7, label='Population', color="yellow", edgecolor="black")
    for j in range(diff_samp):
        plt.hist(samp_data[sz]['samples'][j], bins=30, alpha=0.7, label=f'Sample {j+1}', color=colors[j], edgecolor=edge_colors[j])
    plt.title(f'Histogram of Random (Size {sz}) and Parent')
    plt.xlabel('Marks')
    plt.ylabel('Frequency')
    plt.legend()
    plt.grid(False)

plt.tight_layout()
plt.show()

# show the required stats
for sz in samp_size:
    print(f"\nSample Statistics for {sz} data points:")
    for i in range(diff_samp):
        print(f"Sample {i+1} Mean: {samp_data[sz]['means'][i]}, Std.Dev.: {samp_data[sz]['stds'][i]}")

# generate population data
ppn = np.random.normal(mean, std_dev, popu_size)

# Function for systematic sampling
def dif_wy(ppn, sap_sz):
    gap = len(ppn) // sap_sz
    idcs = np.arange(0, len(ppn), gap)
    tot_saps = []
    for i in range(diff_samp):
        saps = ppn[idcs[i]:idcs[i]+sap_sz]
        tot_saps.append(saps)
    return tot_saps

# generating the asked along with showing the same
plt.figure(figsize=(15, 6))

for i, size in enumerate(samp_size):

    # defining all quantities required
    samp_mean = np.zeros(diff_samp)
    samp_std_dev = np.zeros(diff_samp)
    total_samp = dif_wy(ppn, size)

    # iterating to assign the values for each
    for j in range(diff_samp):
        samp_mean[j] = np.mean(total_samp[j])
        samp_std_dev[j] = np.std(total_samp[j])
    
    # plotting the same in the range
    plt.subplot(1, len(samp_size), i+1)
    plt.hist(ppn, bins=30, alpha=0.7, label='Population', color="yellow", edgecolor="black")
    for j in range(diff_samp):
        plt.hist(total_samp[j], bins=30, alpha=0.5, label=f'Sample {j+1}', color=colors[j], edgecolor=edge_colors[j])
    plt.title(f'Different way Sampled (Size {size})')
    plt.xlabel('Marks')
    plt.ylabel('Frequency')
    plt.legend()
    plt.grid(False)

    # printing the stats
    print(f"\nStats for Different way of Sampling (Size {size}):")
    for j in range(diff_samp):
        print(f"Sample {j+1} Mean: {samp_mean[j]}, Std.Dev.: {samp_std_dev[j]}")

plt.tight_layout()
plt.show()


# defining for tot population
ppn_mean = np.mean(ppn)
ppn_std = np.std(ppn)

# for random sample stats
rdm_sap_means = [np.mean(sap) for sap in samps]
rdm_sap_stds = [np.std(sap) for sap in samps]

# different method sampling stats
dif_sap_means = [np.mean(sap) for sap in total_samp]
dif_sap_stds = [np.std(sap) for sap in total_samp]

# printing overall stats
print(" ")
print("Population Stats:")
print(f"Population Mean: {ppn_mean}, Population Std.Dev.: {ppn_std}")

# printing random samples stats
print("\nRandom Sampling Stats:")
for i in range(diff_samp):
    print(f"Sample {i+1} Mean: {rdm_sap_means[i]}, Std.Dev.: {rdm_sap_stds[i]}")

# printing different way stats
print("\nDifferent Sampling Stats:")
for i, size in enumerate(samp_size):
    print(f"Sample Size {size}:")
    for j in range(diff_samp):
        print(f"Sample {j+1} Mean: {dif_sap_means[j]}, Std.Dev.: {dif_sap_stds[j]}")
