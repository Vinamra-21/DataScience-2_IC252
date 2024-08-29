import numpy as np
import matplotlib.pyplot as plt

##################################################################################################################
# Question 2: A course instructor has brought a lie detector to check how many of his students lie. Let
# X = number of times the lie detector buzzes for a student. He randomly chooses 50 students for the
# test and the following information was obtained: X = 0 for 2 students, X = 1 for 11 students, X = 2
# for 23 students, X = 3 for 9 students, X = 4 for 4 students, X = 5 for 1 student.
##################################################################################################################

##################################################################################################################
# (a) Plot the PDF and CDF.
##################################################################################################################

n = 50
p = [2, 11, 23, 9, 4, 1]  # Frequencies for each X value
x_values = np.arange(0, 6)
probab = np.array(p) / n
cdf = np.cumsum(probab)

plt.figure(figsize=(8,4))
# PDF
plt.subplot(1, 2, 1)
plt.grid(True)
plt.bar(x_values, probab)
plt.title('Probability Mass Function (PMF)')
plt.xlabel('Value of Random variable(X)')
plt.ylabel('Probability')

# CDF
plt.subplot(1, 2, 2)
for i in range(len(x_values)-1):
    plt.plot([x_values[i], x_values[i+1]], [cdf[i], cdf[i]], color='black')
    plt.plot(x_values[i], cdf[i], marker='o', color='black')  
    plt.plot(x_values[i+1], cdf[i], 'o', color='black', fillstyle='none') 
    plt.plot(x_values[i+1], cdf[i], 'o', color='white') 
plt.title('Cumulative Distribution Function (CDF)')
plt.xlabel('Value of Random variable (X)')
plt.ylabel('Cumulative Probability')
plt.grid(True)
plt.ylim(0, 1.5)
plt.tight_layout()
plt.show()

##################################################################################################################
# (b) Simulate such an experiment in python (for n = 50, 500 and 5000 times) and calculate the average number of lies a 
#student tells and the standard deviation. Compare it with the theoretical values.(Calculate theoretical values using python)
##################################################################################################################

ns = [50, 500, 5000]

theo_mean = np.sum(x_values * probab)
theo_stddev = np.sqrt(np.sum(((x_values - theo_mean) ** 2) * probab))
for n in ns:
    X_generate = np.random.choice(x_values, n,p=probab)
    mean_X = np.mean(X_generate)
    #temp=0
    #for i in simulated_X:
    #   temp+=i
    # average_X=temp/n
    std_dev = np.std(X_generate)
    # variance = (sum((x - mean_X) ** 2 for x in X_generate) / n)
    # stddev=varience**0.5
    print(f"For n={n}:")
    print(f"Simulated average: {mean_X}")
    print(f"Simulated standard deviation: {std_dev}")
    print(f"Theoretical mean: {theo_mean}")
    print(f"Theoretical standard deviation: {theo_stddev}")
    print()

##################################################################################################################
#(c) Pick one value of n, repeat n experiments 1000 times (try playing with this value). Plot a histogram of these
# mean values. What is the mean and variance of the sample means? Does the histogram seem to follow a type of 
# distribution? (CLT foreshadowing). Can you comment on the following statement -“The sample mean is a Random Variable.”
##################################################################################################################

n = 50  # chosen value of n
num_exp = 1000
sample_means = []

for _ in range(num_exp):
    X_generate = np.random.choice(x_values, n, p=probab)
    sample_means.append(np.mean(X_generate)) 

# Plot histogram of sample means
plt.hist(sample_means, bins=40, alpha=0.7)
plt.title('Histogram of Sample Means')
plt.xlabel('Sample Mean')
plt.ylabel('Density')
plt.grid(True)
plt.show()

# Calculate mean and variance of sample means
print(f"Mean of sample means: {np.mean(sample_means)}")
print(f"Variance of sample means: {np.var(sample_means)}")



#In simpler terms, CTL implies that as you take more and more samples from a population and calculate their 
#means, the distribution of those sample means will tend to follow a normal distribution, regardless of the 
#shape of the original population distribution, under certain conditions. This is a key concept in statistics, 
#as it allows us to make inferences about population parameters based on sample statistics, particularly when 
#dealing with large samples.


#Follows CTL

#“The sample mean is a Random Variable.”