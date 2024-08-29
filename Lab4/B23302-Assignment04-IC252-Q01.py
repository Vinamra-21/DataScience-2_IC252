################################################################################################################
# Question 1: Imagine you live in a place with three weather conditions: sunny, rainy or cloudy. You
# also have three clothing choices: T-shirt, sweater or Jacket.
################################################################################################################
################################################################################################################
# (a) Create a joint probability table representing the likelihood of experiencing a specific weather condition 
# alongside your clothing choice (Hint: Simulate a large number of samples of weather conditions with clothing choices)
################################################################################################################
import matplotlib.pyplot as plt   
import numpy as np

n=10000                                                                 #number of trials
weather = np.random.choice(['Sunny', 'Rainy', 'Cloudy'], size=n)        #random choices of weather
clothing = np.random.choice(['T-shirt', 'Sweater', 'Jacket'], size=n)   #random choices of clothing


joint_values = {(x, y): 0 for x in ['Sunny', 'Rainy', 'Cloudy'] for y in ['T-shirt', 'Sweater', 'Jacket']}

for x,y in zip(weather, clothing):                                      #count different cases
    joint_values[(x, y)] += 1

joint_probab = {(x, y): count /n for (x, y), count in joint_values.items()}

print("Joint Probability Table:")                                     #presenting as table
print("\nWeather | Clothing | Probability")
print("---------------------------------")
for (x, y), probab in joint_probab.items():
    print(f"{x:7} | {y:8} | {probab}")

################################################################################################################
# (b) Calculate the marginal probabilities of the weather and the clothing choices based on the joint
# probability table. Plot these probabilities (two plots one for weather and the other for clothing choice).
################################################################################################################ 

marginal_weather = {x: sum(joint_probab[(x, y)] for y in ['T-shirt', 'Sweater', 'Jacket']) for x in ['Sunny', 'Rainy', 'Cloudy']} #marginal probsbilities
marginal_clothing = {y: sum(joint_probab[(x, y)] for x in ['Sunny', 'Rainy', 'Cloudy']) for y in ['T-shirt', 'Sweater', 'Jacket']}

plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.bar(marginal_weather.keys(), marginal_weather.values(), color='green')
plt.title('Marginal Probability of Weather Choice')
plt.xlabel('Weather')
plt.ylabel('Probability')

plt.subplot(1, 2, 2)
plt.bar(marginal_clothing.keys(), marginal_clothing.values(), color='blue')
plt.title('Marginal Probability of Clothing Choice')
plt.xlabel('Clothing')
plt.ylabel('Probability')

plt.tight_layout()
plt.show()

################################################################################################################
# (c) Find the conditional probability of each clothing choice given a specific weather condition
################################################################################################################

# Conditional probability of each clothing choice given a specific weather condition
cond_probabab = {(x, y): joint_probab[(x, y)] / marginal_weather[x] for x in ['Sunny', 'Rainy', 'Cloudy'] for y in ['T-shirt', 'Sweater', 'Jacket']}

# Display conditional probabilities
print("\nConditional Probability Table:")
print("\nWeather | Clothing | Probability")
print("---------------------------------")
for (x, y), probab in cond_probabab.items():
    print(f"{x:7} | {y:8} | {probab}")











