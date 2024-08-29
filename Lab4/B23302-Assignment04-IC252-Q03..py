
################################################################################################################
# Question 3: Two professors teach the same Statistics course. Professor A’s exams follow a normal
# distribution with a mean (μ) of 78 and a standard deviation (σ) of 5. Professor B’s exams are also
# normally distributed, with a mean (μ) of 85 and a standard deviation (σ) of 3. A student randomly
# picks a professor’s course to enroll in (let Professor = “A” or “B”). They are also interested in knowing
# the difficulty level (Easy, Medium, Hard) assigned to their exam by the professor. The difficulty is
# assigned independently with the following probabilities:
# • Easy: 0.3
# • Medium: 0.5
# • Hard: 0.2
################################################################################################################
# (a) Find the joint probability distribution P(X,Y ). This will represent the probability of getting a
# specific score (X) along with a particular difficulty level (Y ).
################################################################################################################
import numpy as np
import matplotlib.pyplot as plt

mean_A = 78
std_dev_A = 5

mean_B = 85
std_dev_B = 3

p_easy = 0.3
p_medium = 0.5
p_hard = 0.2
levels=['easy','medium','hard']
n_trials = 100

score_A = np.random.normal(mean_A, std_dev_A, n_trials)
score_B = np.random.normal(mean_B, std_dev_B, n_trials)

def probab_normal(x, mean, std_dev): 
    return (1 / (std_dev * np.sqrt(2 * np.pi))) * np.exp(-0.5 * (((x - mean) / std_dev) ** 2))

#array for joint probab
jnt_probab_A = np.zeros((len(score_A), len(levels)))
jnt_probab_B = np.zeros((len(score_B), len(levels)))


# fxn to calculate the joint probabilities for array
def joint_probab_cal(score,mean,std_dev,jnt_probab):
    for i, score in enumerate(score):
        for j, difficulty in enumerate(levels):
            probab = probab_normal(score, mean, std_dev)
            if difficulty == 'easy':
                jnt_probab[i, j] = probab * p_easy
            elif difficulty == 'medium':
                jnt_probab[i, j] = probab * p_medium
            else:
                jnt_probab[i, j] = probab * p_hard
    return jnt_probab            


# calling fxn to get required joit probabilities
jnt_prb_A = joint_probab_cal(score_A,mean_A,std_dev_A,jnt_probab_A)
jnt_prb_B = joint_probab_cal(score_B,mean_B,std_dev_B,jnt_probab_B)


# printing the required joint probabilities
print("Joint probability  P(X, Y) for Professor 'A':")
print("         Score (X\Y)              Easy         |          Medium          |          Hard  ")
print("---------------------------------------------------------------------------------------------------")
for i, score in enumerate(score_A):
    print(f"{score:19}:   {jnt_prb_A[i, 0]:22}  |  {jnt_prb_A[i, 1]:22}  |  {jnt_prb_A[i, 2]:22}")
print()
print("---------------------------------------------------------------------------------------------------")
print()
print("Joint probability  P(X, Y) for Professor 'B':")
print("         Score (X\Y)              Easy         |          Medium          |          Hard  ")
print("---------------------------------------------------------------------------------------------------")
for i, score in enumerate(score_B):
    print(f"{score:19}:   {jnt_prb_B[i, 0]:22}  |  {jnt_prb_B[i, 1]:22}  |  {jnt_prb_B[i, 2]:22}")
print()
print("---------------------------------------------------------------------------------------------------")
print()

################################################################################################################
# (b) Calculate the marginal probability distributions.
################################################################################################################
# Marginal probability distributions for Professor A
marginal_prob_A_X = np.sum(jnt_probab_A, axis=1) / n_trials
marginal_prob_A_Y = np.sum(jnt_probab_A, axis=0)

marginal_prob_A_Y /= np.sum(marginal_prob_A_Y) # Normalize marginal probability distribution

print("Marginal probability distribution for Professor A - Score (X):")
for i, score in enumerate(score_A):
    print(f"Score: {score}, Probability: {marginal_prob_A_X[i]}")

print("\nMarginal probability distribution for Professor A - Difficulty-Level (Y):")
for i, difficulty in enumerate(levels):
    print(f"Difficulty: {difficulty}, Probability: {marginal_prob_A_Y[i]}")

print()
print("---------------------------------------------------------------------------------------------------")
print()

# Marginal probability distributions for Professor B
marginal_prob_B_X = np.sum(jnt_probab_B, axis=1) / n_trials
marginal_prob_B_Y = np.sum(jnt_probab_B, axis=0)

marginal_prob_B_Y /= np.sum(marginal_prob_B_Y) # Normalize marginal probability distribution

print("Marginal probability distribution for Professor B - Score (X):")
for i, score in enumerate(score_B):
    print(f"Score: {score}, Probability: {marginal_prob_B_X[i]}")

print("\nMarginal probability distribution for Professor B - Difficulty-Level (Y):")
for i, difficulty in enumerate(levels):
    print(f"Difficulty: {difficulty}, Probability: {marginal_prob_B_Y[i]}")

print()
print("---------------------------------------------------------------------------------------------------")
print()

################################################################################################################
# (c) Calculate the conditional probability P(X > 80|Y = “Easy”) - the probability of getting a score
# higher than 80 given the exam is Easy.
################################################################################################################
#for professor A
# score>80
scr_mor_80_A = np.where(score_A > 80)[0]
# easy also
scr_mor_80_easy_A = (np.sum(jnt_prb_A[scr_mor_80_A, 0]))
#total easy
tot_esy_A = np.sum(jnt_prb_A[:, 0])
#conditional probab
cond_probab_A=scr_mor_80_easy_A/tot_esy_A
print("Conditional probability (Professor A) P(X > 80|Y = “Easy”):", cond_probab_A)

#for professor B
# score>80
scr_mor_80_B = np.where(score_B > 80)[0]
# easy also
scr_mor_80_easy_B = (np.sum(jnt_prb_B[scr_mor_80_B, 0]))
#total easy
tot_esy_B = np.sum(jnt_prb_B[:, 0])
#conditional probab
cond_probab_B=scr_mor_80_easy_B/tot_esy_B
print("Conditional probability (Professor B) P(X > 80|Y = “Easy”):", cond_probab_B )

print("Conditional probability P(X > 80|Y = “Easy”):", (cond_probab_A + cond_probab_B)/2)

print()
print("---------------------------------------------------------------------------------------------------")
print()
################################################################################################################
# (d) Plot the probability density functions (PDFs) of both Professor A’s and Professor B’s exams on the
# same graph. Clearly label the axes and curves.
################################################################################################################

#calculating pdf
x_values = np.linspace(50, 110, 1000)
pdf_A = probab_normal(x_values, mean_A, std_dev_A)
pdf_B = probab_normal(x_values, mean_B, std_dev_B)

plt.plot(x_values, pdf_A, label='Professor A')
plt.plot(x_values, pdf_B, label='Professor B')
plt.xlabel('Marks')
plt.ylabel('Probability Density')
plt.title('PDFs of marks obtained')
plt.grid(True)
plt.legend()
plt.show()

# plot of same data as histogram
plt.figure(figsize=(10, 4))

plt.subplot(1, 2, 1)
plt.hist(score_A, bins=30, edgecolor='black',color = 'green', alpha=0.7)
plt.xlabel("Marks")
plt.ylabel('Number of students')
plt.grid(True)
plt.title('(PDF) Professor A')

plt.subplot(1, 2, 2)
plt.hist(score_B, bins=30, edgecolor='black',color = 'green', alpha=0.7)
plt.xlabel("Marks")
plt.ylabel('Number of students')
plt.grid(True)
plt.title('(PDF) Professor B')

plt.tight_layout()  
plt.show()


################################################################################################################
# (e) How would the joint probability distribution change if the difficulty level was not assigned independently 
# and instead, professors were more likely to assign harder exams to students with higher expected scores (based 
# on professor)?
################################################################################################################
def joint_probab_cal_e(score, mean, std_dev):
    jnt_probab = np.zeros((len(score), len(levels)))
    for i, score in enumerate(score):
        for j, difficulty in enumerate(levels):
            probab = probab_normal(score, mean, std_dev)
            # Adjust difficulty based on expected score
            if difficulty == 'easy':
                jnt_probab[i, j] = probab * p_easy
            elif difficulty == 'medium':
                jnt_probab[i, j] = probab * p_medium
            else:
                jnt_probab[i, j] = probab * (p_hard + (score - mean) * 0.01)        # for hard making it more probable
    return jnt_probab

# calculating the  joint dependent
jnt_prb_A_dpnd = joint_probab_cal_e(score_A, mean_A, std_dev_A)
jnt_prb_B_dpnd = joint_probab_cal_e(score_B, mean_B, std_dev_B)

# printing the required joint probabilities
print("Joint probability  P(X, Y) for Professor 'A'(high score-hard):")
print("         Score (X\Y)              Easy         |          Medium          |          Hard  ")
print("---------------------------------------------------------------------------------------------------")
for i, score in enumerate(score_A):
    print(f"{score:19}:   {jnt_prb_A_dpnd[i, 0]:22}  |  {jnt_prb_A_dpnd[i, 1]:22}  |  {jnt_prb_A_dpnd[i, 2]:22}")
print()
print("---------------------------------------------------------------------------------------------------")
print()
print("Joint probability  P(X, Y) for Professor 'B'(high score-hard):")
print("         Score (X\Y)              Easy         |          Medium          |          Hard  ")
print("---------------------------------------------------------------------------------------------------")
for i, score in enumerate(score_B):
    print(f"{score:19}:   {jnt_prb_B_dpnd[i, 0]:22}  |  {jnt_prb_B_dpnd[i, 1]:22}  |  {jnt_prb_B_dpnd[i, 2]:22}")
print()
print("---------------------------------------------------------------------------------------------------")
print()


#  Increased Probability for Hard Difficulty : for students with higher expected scores, there will
#  be a higher probability of encountering harder problems in their exams.
#  This would lead to an increase in the joint probability of higher scores and harder difficulty levels.