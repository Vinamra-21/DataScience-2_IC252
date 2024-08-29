# 8. (a) Simulate a random number generator for the following distributions:
# i. Uniform distribution
# ii. Normal distribution
# iii. Truncated exponential distribution
# Generate a sample dataset of 1000 points for each case. Plot the histogram of the samples and the density function
# of the given distributions in a single subplot.
#####################################################################################################################

# importing libraries
import numpy as np
import matplotlib.pyplot as plt

def un_rd(a, b, size):     # simulate uniform random by inverse transformation
    u = np.random.rand(size)
    return a + u * (b - a)

    # a: Lower bound
    # b: Upper bound
    # size: n_samples

def nrm_rd(low , high , size):   # simulate normal by Box-Muller transformation
    u1 = np.random.rand(size)
    u2 = np.random.rand(size)
    z0 = np.sqrt(-2 * np.log(u1)) * np.cos(2 * np.pi * u2)
    z1 = np.sqrt(-2 * np.log(u1)) * np.sin(2 * np.pi * u2)
    return z1 # or return z0

    # u1,u2 are two set of random numbers
    # z0 and z1 are two set of normally distributed number
    # mean is mean for the to be created
    # std is standard deviation for the same

# same fxn but removed the not required values
# def nrm_rd(mean, std, size):
#     u1 = np.random.rand(size)
#     u2 = np.random.rand(size)
#     z0 = np.sqrt(-2 * np.log(u1)) * np.cos(2 * np.pi * u2)
#     return mean + z0 * std

def trn_exp(lambda_, a, b, size=1): # truncated exponential by inverse transformation
  u = np.random.rand(size)
  x = (np.log(1 - u * (1 - np.exp(-lambda_ * (b - a)))) / (-lambda_)) + (a)
  return x

  # getting the inverse of cdf for this
  # lambda_: Rate parameter
  # a: Lower bound
  # b: Upper bound
  # size: Number of random numbers 


# Parameters for truncated exponential distribution
lambda_ = 1
a = 0
b = 5
size = 10000


un_saps = un_rd(0, 1, size)
nrm_saps = nrm_rd(0, 1, size)
trn_exp_saps = trn_exp(lambda_, a, b, size)

# plot
plt.figure(figsize=(12, 6))

# Uniform Distribution
plt.subplot(1, 3, 1)
plt.hist(un_saps, bins=30, density=True, color='lightpink', alpha=0.7, ec = "pink")
plt.title('Uniform Distribution')
plt.xlabel('Value')
plt.ylabel('Density')

# Normal Distribution
plt.subplot(1, 3, 2)
plt.hist(nrm_saps, bins=30, density=True, color='lightgreen', alpha=0.7, ec = "green")
plt.title('Normal Distribution')
plt.xlabel('Value')
plt.ylabel('Density')

# Truncated Exponential Distribution
plt.subplot(1, 3, 3)
plt.hist(trn_exp_saps, bins=30, density=True, color='lightblue', alpha=0.7, ec = "blue")
plt.title('Truncated Exponential Distribution')
plt.xlabel('Value')
plt.ylabel('Density')

plt.tight_layout()
plt.show()

# (b) Let fX = 1/40 *(2x + 3), 0 < x < 5
# be a density function. Generate a random number simulator for this density function and sample 1000 random draws.
# Plot the graph of given density function and histogram plot of the drawn samples in a single figure.
###################################################################################################################

def fx(x):
    if 0 <= x <= 5:
        return ((2*x) + 3) / 40
    else:
        return 0

# Finding CDF for fx
def Fx(x):
    if 0 <= x <= 5:
        return (x**2 + 3*x) / 40
    elif x < 0:
        return 0
    else:
        return 1

# Finding inverse of CDF
def Fix(y):
    return np.sqrt(np.abs(40 * y - 3)) - 3/2

# Random numbers by inverse transformation
def sim(size=1):
    u = np.random.rand(size)  # uniform random numbers
    return Fix(u)

# generating numbers for different number of simulations
num_sim = sim(1000)

# histogram along with line plot
x_array = np.linspace(0, 5, 1000)
dist_array = [fx(x) for x in x_array]
plt.plot(x_array, dist_array, label='Line for function', color='green')
plt.hist(num_sim, bins=30, density=True, label='Histogram for function', color='orange', edgecolor='red', alpha=0.7)
plt.xlabel('Points')
plt.ylabel('Probability density')
plt.title('Plot for the function given')
plt.legend()
plt.show() 















