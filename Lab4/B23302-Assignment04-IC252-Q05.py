################################################################################################################
# Question 5: Joint Distribution and independence
################################################################################################################
# (a) Generate two independent random variables, X and Y , with uniform distributions over the inter-
# vals [0,1] and [1,2], respectively and Calculate their joint probability distribution.
################################################################################################################

import numpy as np
import matplotlib.pyplot as plt

n_trials = 10000
# Generate random variables X and Y
X = np.random.uniform(0, 1, size=n_trials)
Y = np.random.uniform(1, 2, size=n_trials)

X_new = X.reshape(n_trials,1)
Y_new = Y.reshape(1,n_trials)


# finding joint probabilities by dot product
# joint_prob = np.histogram2d(X, Y, bins=[10, 10], range=[[0, 1], [1, 2]])[0] / n_trials
# print(joint_prob)
joint_probab = np.dot(X_new,Y_new)
joint_probab = np.round(joint_probab,decimals = 3)
print("Joint probability of", n_trials, "of random variables 'X' and 'Y':")
print(joint_probab)

################################################################################################################
# (b) Verify independence by checking if P(X = x ∩ Y = y) = P(X = x)P(Y = y) for all x and y.
################################################################################################################

# finding marginal pdf
marginal_X = np.histogram(X, bins=10, range=[0,1])[0] / 10000
marginal_Y = np.histogram(Y, bins=10, range=[1,2])[0] / 10000

# checking as independent which is absurd as given already independent
probab_indep = np.outer(X,Y)
probab_indep = np.round(probab_indep,decimals = 3)
is_indep = np.allclose(joint_probab, probab_indep)
print("Indepedent.(T/F):",is_indep)

################################################################################################################
# (c) Based on the joint distribution, calculate P(X > 0.5|Y = 1.5) (conditional probability).
################################################################################################################

# to find index for all y =1.5
Y_index = int((1.5 - 1) / (2 - 1) * joint_probab.shape[1])

# summing all such for y = 1.5
css_Y_15 = joint_probab[:, Y_index].sum()

# finding same for x > 0.5
css_X_05_Y_15 = joint_probab[int(0.5 * joint_probab.shape[0]):, Y_index].sum()

# adding condition now
cond_probab = css_X_05_Y_15 / css_Y_15

# printing the output
print("Conditional Probability P(X > 0.5 | Y = 1.5):", cond_probab)


################################################################################################################
# (d) Plot the conditional probability distribution of X given Y = 1.5.
################################################################################################################

# defining x_values
x_values = np.linspace(0, 2, 100)

# defining conditional to be plot
cdn_probs = np.full_like(x_values, cond_probab)

plt.plot(x_values, cdn_probs, label='P(X > 0.5 | Y = 1.5)')
plt.xlabel('X')
plt.ylabel('Conditional Probability')
plt.title('Conditional Probability P(X > 0.5 | Y = 1.5)')
plt.grid(True)
plt.legend()
plt.show()

################################################################################################################
# (e) Define a new random variable Z = X +Y and utilize the change of variable formula to determine
# the probability density function (pdf) of Z.
################################################################################################################

#####################################################################
# By  convolution theorem we have,                                  
#         {  z−1   for 1 ≤ z ≤ 2                      
# f(z) =  {  3−z   for 2 ≤ z ≤ 3                      
#         {  0     elsewhere                          
#####################################################################

# defining new random variable
Z = X + Y

# defining range for Z
range_Z = [1, 3]

# defining pdf for X
def pdf_X(x):
    if (0 <= x <= 1):
        return 1
    else:
        return 0
  
# defining pdf for Y
def pdf_Y(y):
    if (1 <= y <= 2):
        return 1
    else:
        return 0
 
# pdf of Z by convolution on X and Y
def pdf_Z(z,num):
    res = 0
    for x in np.linspace(0, 1, num):
        # stating the convolution thm for the Z
        if range_Z[0] <= z - x <= range_Z[1]:
            res += pdf_X(x) * pdf_Y(z - x)
    return res/num


num = 1000

# generating values regarding Z
z_values = np.linspace(range_Z[0], range_Z[1], num)

# finding pdf of Z for different points
pdf_values = [pdf_Z(z,num) for z in z_values]

# pdf_Z = np.convolve(pdf_X(Z_values), pdf_Y(Z_values), mode='full')   

# Plotting the pdf of Z
plt.plot(z_values, pdf_values, label='pdf of Z = X + Y')
plt.xlabel('Z')
plt.ylabel('Probability Density')
plt.title('PDF of Z = X + Y')
plt.grid(True,alpha = 0.3)
plt.legend()
plt.show()

# plt.hist(Z, bins=30, density=True, alpha=0.7, label='Empirical PDF')
# plt.xlabel('Z')
# plt.ylabel('Probability Density')
# plt.title('Empirical PDF of Z')
# plt.show()

################################################################################################################
# (f) Validate the result by generating random samples of Z and comparing the empirical distribution
# with the theoretical pdf.
################################################################################################################

# Random samples of z for random x & y
def rdm_saps(n_trials):
    X_saps = np.random.uniform(0, 1, n_trials)
    Y_saps = np.random.uniform(1, 2, n_trials)
    Z_saps = X_saps + Y_saps
    return Z_saps

sam_Z = rdm_saps(n_trials)

# defining z_vals where to calculate
Val_Z = np.linspace(range_Z[0], range_Z[1], num=1000)

# adjusting size so that compatible for plotting
Val_Z = np.linspace(range_Z[0], range_Z[1], num=len(pdf_values))

# plotting the same
plt.hist(sam_Z, bins=50, density=True, alpha=0.5, color='green', label='Sampled PDF of Z')
plt.plot(Val_Z, pdf_values, label='Theoretical PDF of Z')
plt.xlabel('Z')
plt.ylabel('Probability Density')
plt.title('Sampled vs. Theoretical PDF of Z')
plt.grid(True,alpha = 0.7)
plt.legend()
plt.show()