################################################################################################################ 
# Question 2: A factory produces lightbulbs of two types: incandescent and LED. The probability of an
# incandescent bulb being defective is 0.1, while for LED bulbs it’s 0.05. A box contains 2 incandescent
# and 3 LED bulbs. You pick two bulbs at random without replacement
################################################################################################################
################################################################################################################
# (a) Define the random variables. Find and plot the joint distribution.
################################################################################################################

################################################################################################################
# Understanding and assumption
#X: number of defective incandescent bulbs                                      
#Y: number of defective LED bulbs                    
#There are two incandescent bulbs and three LED bulbs in the box,so there are only three possible outcomes:                                                  
#         ->  Both chosen bulbs are incandescent and defective.                     
#         ->  One incandescent bulb is defective, and one LED bulb is defective.        
#         ->  Both chosen bulbs are LED bulbs and defective.                        
#                                                                                   
#  X\Y      0	      1         2	                                                
#  0	 0.86475	0.04125    0.00075                                              
#  1	 0.066	    0.003      0.0                                                  
#  2	 0.001	    0.0        0.0                                                                                                                     
#################################################################################################################
# importing the libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def_incad = 0.1
n_def_incad = 1 - def_incad
def_led = 0.05
n_def_led = 1 - def_led

# random variable
X = Y  = [0,1,2]

n_led = 3
n_incad = 2
n_bulb = n_led + n_incad

def fact(n):          #factorial
    prod = 1
    for i in range(1,n+1):
        prod *= i
    return prod

def nCr(n, r):         #nCr
    return (fact(n) / (fact(r) * fact(n - r)))


total_ways = nCr(n_bulb,2)
led_2_incad_0 = nCr(n_led,2)*nCr(n_incad,0)
led_1_incad_1 = nCr(n_led,1) * nCr(n_incad,1)
led_0_incad_2 = nCr(n_led,0) * nCr(n_incad,2)

# finding probabilities for each case
p_led_2_incad_0 = led_2_incad_0 / total_ways   # 0.3
p_led_1_incad_1 = led_1_incad_1 / total_ways   # 0.6
p_led_0_incad_2 = led_0_incad_2 / total_ways       # 0.1

# stating labels for clear visualisation
x_values = ['0', '1', '2']
y_values = ['0', '1', '2']

# making an empty table to store Random Var values
joint_dist = np.zeros((len(X),len(Y)))


# assigning the values to the each point in our RV domain
joint_dist[0][0] = (n_def_led*n_def_led*p_led_2_incad_0)+(n_def_led*n_def_incad*p_led_1_incad_1)+(n_def_incad*n_def_incad*p_led_0_incad_2)
joint_dist[0][1] = (def_led*n_def_led* p_led_2_incad_0) + (n_def_incad*def_led*p_led_1_incad_1)
joint_dist[0][2] = def_led * def_led * p_led_2_incad_0
joint_dist[1][0] = (p_led_0_incad_2 * def_incad*n_def_incad) + (n_def_led * def_incad * p_led_1_incad_1)
joint_dist[1][1] = p_led_1_incad_1 * def_led * def_incad
joint_dist[1][2] = 0.0      # not possible
joint_dist[2][0] = p_led_0_incad_2 * def_incad * def_incad
joint_dist[2][1] = 0.0      # not possible
joint_dist[2][2] = 0.0      # not possible

# convert to df
joint_dist_df = pd.DataFrame(joint_dist, index=x_values, columns=y_values)
print("Joint distribution for X(defective incandescent) and Y(defective LED):-")
print(joint_dist_df)


# plotting the heatmap for the joint distribution
plt.figure(figsize=(8, 6))
sns.heatmap(joint_dist_df, annot=True, cmap="YlGnBu", fmt=".4f", linewidths=.5)
plt.title('Joint Distribution of Defective Incandescent and LED Bulbs')
plt.xlabel('Defective LED Bulbs (Y)')
plt.ylabel('Defective Incandescent Bulbs (X)')
plt.show()

###################################################################################################################
# (b) Calculate the marginal probability distributions.                           
###################################################################################################################

# Marginal distribution for X
marg_X = np.round(joint_dist_df.sum(axis=1),decimals = 4)

# Marginal distribution for Y
marg_Y = np.round(joint_dist_df.sum(axis=0),decimals = 4)

# printing the required result 
print("Marginal Probability Distribution of X:", marg_X.values.tolist())
print("Marginal Probability Distribution of Y:", marg_Y.values.tolist())


###################################################################################################################
# (c) Plot the PMF of the random variable X (probability mass function, as it deals with discrete values).                 
####################################################################################################################

plt.bar(x_values, marg_X)
plt.xlabel('Number of Defective Incandescent Bulbs(X)')
plt.ylabel('Probability')
plt.title('PMF of Random Variable X')
plt.show()

########################################################################################################################                                                                                                          
# (d) Calculate the conditional probability of getting one defective bulb given the first chosen is incandescent.                                                                                        
#########################################################################################################################

# stating the values 
a = b = def_incad * n_def_incad
c = def_incad * n_def_led 
d = def_led * n_def_incad

res = a+b+c+d
print("P(one defective|1st is incandescent) :", res)

####################################################################################################################################                                                                                                
# (e) Are X and Y independent events? Explain your answer using the joint probability distribution. If Yes, would X and Y still 
# be independent events if the bulb were drawn with replacement. Why or why not?                                                                                                                                                                                                                                            
######################################################################################################################################

indep = np.allclose(np.outer(marg_X, marg_Y), joint_dist)
print("X & Y are independent event: ", indep)

##################################################################################################################################
# (f) How would the joint probability distribution and the marginal probabilities change if the bulbs                         
# were drawn with replacement after each pick?                                                                                                                                                                                      
##################################################################################################################################

print(" Joint Probability Distribution:- ")
print("With replacement, each draw will be independent of the previous. Therefore, the joint probability distribution would become indepedent.Now The probabilities for each outcome would be calculated based on the new probabilities of selecting defective bulbs. so distribution will definatly change.")
print(" Marginal Probabilities:- ")
print("The marginal probabilities will also change after each pick because the total number of bulbs available for selection will remain the same, but the number of defective bulbs might change due to replacement. Therefore, the marginal probabilities will be calculated based on the new probabilities of selecting defective bulbs and the replacement factor.So, marginal distribution  will also change as joint distribution is changing")


# simulate experiment with replacement
def simu_replace( def_incad,def_led):
    joint_probab_replace = []
    new_marg_X = []
    new_marg_Y = []
    for _ in range(2):
        p_0_0 = (1 - def_incad) * (1 -def_led)
        p_0_1 = (1 - def_incad) *def_led
        p_1_0 = def_incad * (1 -def_led)
        p_1_1 = def_incad *def_led
        joint_probab_replace.append([p_0_0, p_0_1, p_1_0, p_1_1])
        new_marg_X.append(p_0_0 + p_0_1)
        new_marg_Y.append(p_0_0 + p_1_0)
    return joint_probab_replace, new_marg_X, new_marg_Y

joint_probab_replace, new_marg_X, new_marg_Y = simu_replace(def_incad,def_led)

#Plot
plt.figure(figsize=(12, 5))
plt.subplot(1, 2, 1)
sns.heatmap(joint_probab_replace, annot=True, cmap="Blues", cbar=False, square=True, xticklabels=['0', '1'], yticklabels=['0', '1'])
plt.title('Joint Distribution with Replacement')
plt.ylabel('X (Number of defective incandescent bulbs)')
plt.xlabel('Y (Number of defective LED bulbs)')


# Plot new marginal
plt.subplot(1, 2, 2)
plt.plot(new_marg_X, label='X (Incandescent bulbs)', marker='o')
plt.plot(new_marg_Y, label='Y (LED bulbs)', marker='o')
plt.xlabel('Number of draws')
plt.ylabel('Probability')
plt.title('Marginal Distributions with Replacement')
plt.legend()
plt.xticks(range(2), range(1,3))
plt.tight_layout()
plt.show()

#################################################################################################################
# (g) How would the PMF of X be affected by sampling with replacement? Would it remain the same, or would the 
# probabilities change? Explain why.
##################################################################################################################

print("When there is sampling with replacement, the probabilities change after each draw because the bulbs are replaced back to the box and the composition for subsequent draws changes. As a result:")
print("1)The probability of drawing a defective bulb on the first draw remains the same as that of without replacement probability.As it the first case and does not affect")
print("2)Subsequent draws yield different probabilities of drawing defective bulbs due to the changing composition of the box after replacement.")
print("3)The PMF of X fluctuates as the probabilities of drawing defective and non-defective bulbs change after each draw.")

