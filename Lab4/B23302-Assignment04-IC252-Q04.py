################################################################################################################
# Question 4: A small radio repair shop repairs two types of radios: AM and FM. The time to repair an
# AM radio follows a normal distribution with a mean of 1 hour (μAM = 1) and a standard deviation of
# 0.5 hours (σAM = 0.5). The time to repair an FM radio follows a normal distribution with a mean of 1.5
# hours (μF M = 1.5) and a standard deviation of 0.75 hours (σF M = 0.75). Simulate the repair times for
# 100 AM radios and 100 FM radios using their respective normal distributions. You can use any random
# number generation library or statistical software to achieve this.
################################################################################################################
################################################################################################################
# (a) Plot the joint probability distribution of the repair times for AM and FM radios.
################################################################################################################

import numpy as np
import matplotlib.pyplot as plt


n_trials = 1000
mean_am = 1
std_dev_am = 0.5
mean_fm = 1.5
std_dev_fm = 0.75

# repair time from normal distribution 
repair_t_am = np.random.normal(mean_am, std_dev_am, n_trials)
repair_t_fm = np.random.normal(mean_fm, std_dev_fm, n_trials)

#individual histograms 
plt.figure(figsize=(10, 4))
plt.subplot(1, 2, 1)
plt.hist(repair_t_am, bins=20, edgecolor='black',color = 'green', alpha=0.7)
plt.xlabel('Repair Time for AM Radio (in hours)')
plt.ylabel('Number of radio out of  '+ str(n_trials))
plt.grid(True)
plt.title('Probability Distribution Repair Time for AM Radios')
plt.subplot(1, 2, 2)
plt.hist(repair_t_fm, bins=20, edgecolor='black',color = 'green', alpha=0.7)
plt.xlabel('Repair Time for FM Radio (in hours)')
plt.ylabel('Number of radio out of  ' + str(n_trials))
plt.grid(True)
plt.title('Probability Distribution Repair Time for FM Radios')
plt.tight_layout() 
plt.show()

#individual scatter plots
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.scatter(repair_t_am, np.arange(n_trials), alpha=0.5)
plt.xlabel('Repair Time for AM Radio (hours)')
plt.ylabel('Sample')
plt.title('Scatter Plot of Repair Times for AM Radios')
plt.subplot(1, 2, 2)
plt.scatter(repair_t_fm, np.arange(n_trials), alpha=0.5)
plt.xlabel('Repair Time for FM Radio (hours)')
plt.ylabel('Sample')
plt.title('Scatter Plot of Repair Times for FM Radios')
plt.tight_layout()
plt.show()

#joint scatter plot
plt.scatter(repair_t_am, repair_t_fm, alpha=0.5)
plt.xlabel('Repair Time for AM Radios (hours)')
plt.ylabel('Repair Time for FM Radios (hours)')
plt.title('Joint Probability Distribution of Repair Times for AM and FM Radios')
plt.grid(True)
plt.show()

#joint 2d histogram
plt.figure(figsize=(8, 6))
plt.hist2d(repair_t_am, repair_t_fm, bins=15, cmap='Blues')
plt.colorbar(label='Frequency')
plt.xlabel('Repair Time for AM Radios (hours)')
plt.ylabel('Repair Time for FM Radios (hours)')
plt.title('Joint Probability Distribution of Repair Times for AM and FM Radios')
plt.grid(True)
plt.show()



################################################################################################################
# (b) What is the probability that the repair time for the FM radio will be less than 1 hour given the AM
# radio repair takes 2 hours?
################################################################################################################

# counting for asked common condition
rep_am_2_fm_less_1 = np.sum((repair_t_fm < 1))/n_trials

print("Probability that the repair time for the FM radio will be less than 1 hour given the AM radio repair takes 2 hours:", rep_am_2_fm_less_1)

################################################################################################################
# (c) Define a new random variable, T, representing the total repair time for both AM and FM radios.
# T = RepairTimeAM + RepairTimeFM. Simulate the total repair time (T) for 100 pairs of AM and FM radios.
################################################################################################################

# defining the intervals
T = repair_t_am + repair_t_fm

# printing the case for addition
for i in range(100):
    print(f"Total repair time for pair {i+1}: {T[i]} hours")

################################################################################################################
# (d) Plot the distribution (histogram) of the total repair time (T). Calculate the mean and standard
# deviation of the total repair time (T) obtained through simulation
################################################################################################################

# finding mean and std for the total repair time (T)
mean_T = np.mean(T)
std_dev_T = np.std(T)

# Theoretical
mean_theo_T = mean_am + mean_fm
std_dev_theo_T = (np.sqrt(((std_dev_am)*2) +((std_dev_fm)*2)))

# simulating huge trials for theoratical and random values
T_nd = np.random.normal(mean_T,std_dev_T,n_trials)
T_nd_theo = np.random.normal(mean_theo_T,std_dev_theo_T,n_trials)

plt.figure(figsize=(10, 5))
# plot for experimental 

plt.subplot(1,2,1)
plt.hist(T_nd, bins=20, edgecolor='black',color = 'green', alpha=0.7)
plt.xlabel('Repair Time for both (hours)')
plt.ylabel('No. of radios out of '+ str(n_trials))
plt.grid(True)
plt.title('Distribution of experimental (AM+FM)')

# plot for theoratical
plt.subplot(1,2,2)
plt.hist(T_nd_theo, bins=20, edgecolor='black',color = 'green', alpha=0.7)
plt.xlabel('Repair Time for both (hours)')
plt.ylabel('No. of radios out of '+ str(n_trials))
plt.grid(True)
plt.title('Distribution of theoratical (AM+FM)')
plt.show()

################################################################################################################
# (e) Assume a customer arrives at the shop, and there’s already one repair in progress (either AM or
# FM). Let Y be a random variable indicating the remaining repair time (from the ongoing repair).
# Derive the probability density function (PDF) of Y if Y originated from an AM radio repair (YAM)
# and another PDF if Y originated from an FM radio repair (YFM). Utilize the change of variable formula for this.
################################################################################################################

Y = "remaining repair time"

# calculating the remain from total
re_rep_tim_AM = T - repair_t_am
re_rep_tim_FM = T - repair_t_fm

# plotting histogram for same  
plt.hist(re_rep_tim_AM, bins=20,edgecolor = 'black' ,density=True, alpha=0.7, label='AM Radio')
plt.hist(re_rep_tim_FM, bins=20, density=True,edgecolor = 'black', alpha=0.7, label='FM Radio')
plt.xlabel('Remaining Repair Time in hours')
plt.ylabel('Probability Density')
plt.title('PDF of Remaining Repair Time')
plt.legend()
plt.grid(True)
plt.show()

# # pdf for y(AM) by change of variable formula
# def rem_tim_AM(y, mean_AM, std_AM):
#     return (1 / std_AM) * np.exp(-((y - mean_AM) / std_AM)**2 / 2) / np.sqrt(2 * np.pi)

# # pdf for y(FM) by change of variable formula
# def rem_tim_FM(y, mean_FM, std_FM):
#     return (1 / std_FM) * np.exp(-((y - mean_FM) / std_FM)**2 / 2) / np.sqrt(2 * np.pi)


# # Define a range of values for remaining repair time (Y)
# y_values = np.linspace(0, 3, 100)

# # pdf for all cases of the combination
# pdf_AM_AM = rem_tim_AM(y_values, mean_am, std_dev_am)
# pdf_FM_FM = rem_tim_FM(y_values, mean_fm, std_dev_fm)
# pdf_AM_FM = rem_tim_AM(y_values, mean_fm, std_dev_fm)
# pdf_FM_AM = rem_tim_FM(y_values, mean_am, std_dev_am)

# # Plotting the PDFs for all cases
# plt.plot(y_values, pdf_AM_AM, label='AM-AM')
# plt.plot(y_values, pdf_FM_AM, label='FM-AM')
# plt.plot(y_values, pdf_AM_FM, label='AM-FM')
# plt.plot(y_values, pdf_FM_FM, label='FM-FM')
# plt.xlabel('Remaining Repair Time (hours)')
# plt.ylabel('Probability Density')
# plt.title('PDF of Remaining Repair Time for Different Radio combinations')
# plt.legend()
# plt.grid(True)
# plt.show()