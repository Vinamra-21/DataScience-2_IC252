
import numpy as np
from statistics import NormalDist
##################################################################################################################
# Question 3: A manufacturing company produces widgets, and the weights of these widgets follow a normal distribution
# with a mean weight of 150 grams and a standard deviation of 10 grams. The quality control team is responsible for 
# ensuring that the weights of the widgets meet certain specifications. Simulate 100 such samples in python and answer 
# the following questions.
##################################################################################################################

mean = 150
std_dev = 10
n = 100
samples = np.random.normal(mean, std_dev, n) #noraml distribution

##################################################################################################################
# (a) What is the probability that a randomly selected widget weighs less than 140 grams?
##################################################################################################################

p_less_140 = sum(sample<140 for sample in samples)/n
print("(a) probability that a randomly selected widget weighs less than 140 grams:", p_less_140)

##################################################################################################################
# (b) The company has a policy that only the top 5% of the heaviest widgets will be shipped as premium
# products. What is the minimum weight a widget must have to qualify as a premium product?
##################################################################################################################

premium_prdt_w = np.percentile(samples, 95)
print("(b) Minimum weight a widget must have to qualify as a premium product:", premium_prdt_w)

##################################################################################################################
# (c) If the company wants to set a weight limit so that only the lightest 10% of widgets are considered defective
# and need further inspection, what is the maximum weight allowed for a widget to be considered within the acceptable range?
##################################################################################################################

lightest_prdt_w = np.percentile(samples, 10)
print("(c) Maximum weight allowed for a widget to be considered within the acceptable range:", lightest_prdt_w)

##################################################################################################################
# (d) What is the probability that a product is neither premium nor defective?
# Validate and compare the answer of each subpart with its theoretically calculated answer.
##################################################################################################################

prdt_no_prev_def = (1 - 0.05 - 0.1)
print("(d) Probability that a product is neither premium nor defective:", prdt_no_prev_def)

print()
##################################################################################################################
# Hint: To calculate theoretically you may explore the statistics. NormalDist library
##################################################################################################################

# Theoretical part(a)
tp_less_140 = NormalDist(mean, std_dev).cdf(140)
print("Theoretical Probability that a randomly selected widget weighs less than 140 grams:",tp_less_140)

# Theoretical part(b)
t_premium_prdt_w = NormalDist(mean, std_dev).inv_cdf(0.95)
print("Theoretical Minimum weight a widget must have to qualify as a premium product:", t_premium_prdt_w)

# Theoretical part(c)
t_lightest_prdt_w = NormalDist(mean, std_dev).inv_cdf(0.10)
print("Theoretical Maximum weight allowed for a widget to be considered within the acceptable range:", t_lightest_prdt_w)

# Theoretical part(d)
t_prdt_no_prev_def = 1 - (0.05 + 0.10)
print("Theoretical Probability that a product is neither premium nor defective:", t_prdt_no_prev_def)