import numpy as np

##################################################################################################################
# Question 4: In poker, a full house is a hand that contains three cards of one rank and two cards of
# another rank, such as 3 ↔ 3 ∗ 6 ∗ 6∗. (Wikipedia)
##################################################################################################################

##################################################################################################################
# (a) What is the probability of getting a full house?
##################################################################################################################

def fact(n):
    if n<=1:
        return 1
    return n*fact(n-1)
def nCr(n,r):
    return fact(n)/(fact(r)*fact(n-r))

#there are thirteen denominations 
probability_full_house=(nCr(13,2)*nCr(2,1)*nCr(4,3)*nCr(4,2))/nCr(52,5)
print("(a) Probability of getting a full house:",probability_full_house)

##################################################################################################################
# (b) Simulate a python experiment and compare with the theoretical value.
##################################################################################################################

def simulate_full_exp(trials):
    full_house = 0                                       
    for _ in range(trials):                     
        cards = np.arange(1, 53)                     
        np.random.shuffle(cards)               
        pick_5 = cards[:5]                                                                     
        counter = np.bincount((pick_5) % 13)              
        if 3 in counter and 2 in counter:                            
            full_house += 1

    new_prob = full_house / trials                            
    return new_prob                                            

probability_full_house_exp=simulate_full_exp(10000)
print("(b) Experimental Probability of getting a full house:",probability_full_house_exp)   

##################################################################################################################
# (c) What is the probability that in 1000 trials one will get at least 2 full houses? You may assume that the 
# hands were dealt independently from one another. Compare this value after simulating it in python. Calculate 
# mean and variance.
##################################################################################################################

def simulate_1000_trials(num_trials):
    full_house_count = 0
    successes = []
    for _ in range(num_trials):
        full_houses = 0
        for _ in range(1000):  # Simulate 1000 trials
            cards = np.arange(1, 53)
            np.random.shuffle(cards)
            pick_5 = cards[:5]
            counter = np.bincount((pick_5) % 13)
            if 3 in counter and 2 in counter:
                full_houses += 1
        if full_houses >= 2:
            full_house_count += 1
            successes.append(full_houses)

    mean = np.mean(successes)
    variance = np.var(successes)
    return full_house_count / num_trials, mean, variance

num_trials = 1000
probability_at_least_2_full_houses, mean, variance = simulate_1000_trials(num_trials)

print("(c) Simulated Probability of at least two full houses in 1000 trials:", probability_at_least_2_full_houses)
print("Mean:", mean)
print("Variance:", variance)





#theoretical
# Probability of getting less than 2 full houses in 1000 trials
p_less_than_2 = (1 - probability_full_house) ** 1000 + 1000 * probability_full_house * ((1 - probability_full_house) ** 999)

# Probability of getting at least 2 full houses in 1000 trials
p_at_least_2 = 1 - p_less_than_2

print("Theoretical probability of getting at least 2 full houses in 1000 trials:", p_at_least_2)
