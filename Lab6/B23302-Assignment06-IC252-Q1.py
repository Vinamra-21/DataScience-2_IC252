# 1. (a) Calculate the entropy of a fair coin. Now suppose that the coin is biased, i.e., probability of head is not equal to 0.5.
# Plot the entropy curve where x−axis represents the probability of head and y−axis is the corresponding entropy.
##################################################################################################################################

# import libraries
import numpy as np
import matplotlib.pyplot as plt

def epy(p):  #entropy
    if p == 0 or p == 1:
        return 0
    return -(p * np.log2(p) + (1 - p) * np.log2(1 - p))

    # p: probab head 

nrml_entropy = epy(0.5)  #unbiased case

p_vals = np.linspace(0, 1, 100)
entropy_vals = [epy(p) for p in p_vals]

# plotting the same
plt.plot(p_vals, entropy_vals, color = "red")
plt.xlabel('Probability of Heads')
plt.ylabel('Entropy')
plt.title('Entropy Biased Coin')
plt.axhline(y = nrml_entropy, color='green', linestyle='-.', label='Entropy Fair Coin')
plt.legend()
plt.grid(True)
plt.show()

# (b) Generate and plot two Gaussian distributions with different mean and variance. Calculate the KL divergence and
# cross-entropy between these two distributions. Repeat this experiment for different mean and variance, and observe
# the value of KL divergence and cross-entropy when these two distributions:
# i. overlap each other,
# ii. partially overlap,
# iii. do not overlap.
#####################################################################################################################

# define value
mean_a = 1
mean_b = 3
stddev_a = 2
stddev_b = 4

x_values = np.linspace(-5, 10, 100) 

def gaussian_pdf(x, mean, std_dev): #gaussian dist
    return np.exp(-((x - mean) ** 2) / (2 * std_dev ** 2)) / (std_dev * np.sqrt(2 * np.pi))

y1 = gaussian_pdf(x_values, mean_a, stddev_a)
y2 = gaussian_pdf(x_values, mean_b, stddev_b)

# plot
plt.plot(x_values, y1, label='Distribution 1')
plt.plot(x_values, y2, label='Distribution 2')
plt.xlabel('x')
plt.ylabel('Probability density')
plt.title('Gaussian distributions with different mean and variance')
plt.legend()
plt.show()


def k_l_diverge(a_mean, a_var, b_mean, b_var):  #kl divergence

    x = np.linspace(min(a_mean - 3 * np.sqrt(a_var), b_mean - 3 * np.sqrt(b_var)),
                    max(a_mean + 3 * np.sqrt(a_var), b_mean + 3 * np.sqrt(b_var)), 1000)
    
    # finding pdf for each distribution 
    pdf_a = gaussian_pdf(x, a_mean, a_var)
    pdf_b = gaussian_pdf(x, b_mean, b_var)
    
    # kl divergence
    k_l_div = np.sum(pdf_a * np.log(pdf_a / pdf_b))
    
    return k_l_div

def cross_entropy(a_mean, a_var, b_mean, b_var):
    # Defining range of x
    x = np.linspace(min(a_mean - 3 * np.sqrt(a_var), b_mean - 3 * np.sqrt(b_var)),
                    max(a_mean + 3 * np.sqrt(a_var), b_mean + 3 * np.sqrt(b_var)), 1000)
    
    # finding pdf for each distribution
    a_pdf = gaussian_pdf(x, a_mean, a_var)
    b_pdf = gaussian_pdf(x, b_mean, b_var)
    
    cross_entrpy_val = -np.sum(a_pdf * np.log(b_pdf))
    
    return cross_entrpy_val

print("kl-divergence for the two distributions:", k_l_diverge(mean_a,mean_b,stddev_a,stddev_b))
print("cross-entropy for the two distributions:" ,cross_entropy(mean_a,mean_b,stddev_a,stddev_b))

# 1: Overlapping distributions
mean1 = 0
var1 = 1
mean2 = 0
var2 = 1

y1 = gaussian_pdf(x_values, mean1, var1)
y2 = gaussian_pdf(x_values, mean2, var2)

# plot
plt.plot(x_values, y1, label='Distribution 1')
plt.plot(x_values, y2, label='Distribution 2')
plt.xlabel('x')
plt.ylabel('Probability density')
plt.title('Overlapping Distribution')
plt.legend()
plt.show()

kl_div1 = k_l_diverge(mean1, var1, mean2, var2)
cross_ent1 = cross_entropy(mean1, var1, mean2, var2)
print("\nExperiment 1 - Overlapping Distributions:")
print("KL Divergence:", kl_div1)
print("Cross-Entropy:", cross_ent1)

# 2: Partially overlapping distributions
mean1 = 1
var1 = 1
mean2 = 2
var2 = 1

y1 = gaussian_pdf(x_values, mean1, var1)
y2 = gaussian_pdf(x_values, mean2, var2)

# plot
plt.plot(x_values, y1, label='Distribution 1')
plt.plot(x_values, y2, label='Distribution 2')
plt.xlabel('x')
plt.ylabel('Probability density')
plt.title('Partially Overlapping Distribution')
plt.legend()
plt.show() 

kl_div2 = k_l_diverge(mean1, var1, mean2, var2)
cross_ent2 = cross_entropy(mean1, var1, mean2, var2)
print("\nExperiment 2 - Partially Overlapping Distributions:")
print("KL Divergence:", kl_div2)
print("Cross-Entropy:", cross_ent2)

# 3: Non-overlapping distributions
mean1 = 0
var1 = 1
mean2 = 7
var2 = 1

y1 = gaussian_pdf(x_values, mean1, var1)
y2 = gaussian_pdf(x_values, mean2, var2)

# plot
plt.plot(x_values, y1, label='Distribution 1')
plt.plot(x_values, y2, label='Distribution 2')
plt.xlabel('x')
plt.ylabel('Probability density')
plt.title('Non-Overlapping Distribution')
plt.legend()
plt.show()

kl_div3 = k_l_diverge(mean1, var1, mean2, var2)
cross_ent3 = cross_entropy(mean1, var1, mean2, var2)
print("\nExperiment 3 - Non-overlapping Distributions:")
print("KL Divergence:", kl_div3)
print("Cross-Entropy:", cross_ent3)

