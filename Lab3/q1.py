import numpy as np
import matplotlib.pyplot as plt

##################################################################################################################
# Question 1: The exponential distribution is ideal to model waiting times (e.g, time to failure of sensors
# in a system, flood occurrence, etc.). We will be using the exponential distribution to model time to the
# arrival of the next confirmed case of Covid-19 in India. Based upon data of confirmed cases from the
# source https://www.covid19india.org/, between 17th April 2020 and 23rd April 2020, there were on
# average 1373 confirmed cases per day, i.e. on average around 57 cases per hour.
##################################################################################################################

avg_case_per_hour = 57

scale = 1 / avg_case_per_hour

# PDF of expdist
def pdf(x, scale):
    return (1 / scale) * np.exp(-x / scale)

# CDF of expdist
def cdf(x, scale):
    return 1 - np.exp(-x / scale)

wait_time_hours = np.linspace(0, 10, 1000) #1000 points between 0,10

pdf_list = pdf(wait_time_hours, scale)  #pdf for different wait time
cdf_list = cdf(wait_time_hours, scale)  #cdf for different wait time

##################################################################################################################
# (a) Write a program to plot the probability density function of the wait time for the next Covid-19
# confirmed case, where the X axis is the wait time in hours and Y axis is the probability density.
##################################################################################################################
plt.figure(figsize=(10, 5))
plt.plot(wait_time_hours, pdf_list, label='Exponential PDF', color='black')
plt.title('Probability Density Function (PDF) of Wait Time for Next COVID-19 Confirmed Case')
plt.xlabel('Wait Time (Hours)')
plt.ylabel('Probability Density')
plt.grid(True)
plt.legend()
plt.show()

###################################################################################################################
# (b) Write a program to find the probability of the wait time for the next Covid-19 confirmed case to be
# less than or equal to 1 minute (Hint: convert minutes into hours before using it in the cumulative
# density function).
###################################################################################################################

w_time_1min = 1 / 60  #hrs
p_less_1min = cdf(w_time_1min, scale)
print("(b) Probability of wait time less than or equal to 1 minute:", p_less_1min)

###################################################################################################################
# (c) Write a program to find the probability of the wait time for the next Covid-19 confirmed case to
# be between 1 minute and 2 minutes.
###################################################################################################################

w_time_2min = 2 / 60  #hrs
p_less_2min = cdf(w_time_2min, scale)
p_1min_2min = p_less_2min - p_less_1min
print("(c) Probability of wait time between 1 minute and 2 minutes:", p_1min_2min)

###################################################################################################################
# (d) Now, write a program to find the probability of the wait time for the next Covid-19 confirmed case
# to be more than 2 minutes.
###################################################################################################################

p_more_2min = 1 - p_less_2min
print("(d) Probability of wait time more than 2 minutes:", p_more_2min)

###################################################################################################################
# (e) Suppose the average number of cases per hour doubled. Write a program to find the probability
# of wait time for the next Covid-19 confirmed case to be between 1 minute and 2 minutes
###################################################################################################################

new_avg_case = avg_case_per_hour * 2
d_scale = 1/new_avg_case
dp_less_2min = cdf(w_time_2min, d_scale)
dp_less_1min = cdf(w_time_1min, d_scale)
dp_1min_2min = dp_less_2min - dp_less_1min
print("(e) Probability of wait time between 1 minute and 2 minutes after doubling the average cases per hour:",dp_1min_2min)
