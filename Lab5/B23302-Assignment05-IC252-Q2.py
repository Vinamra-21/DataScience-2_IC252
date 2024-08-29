# The Community Mobility Reports provided by Google show movement trends by region across different categories of
# places. These reports are created with aggregated, anonymized sets of data from users who have turned on the Location
# History setting, which is off by default. The data shows how visitors to (or time spent in) categorized places change
# compared to our baseline days. A baseline day represents a normal value for that day of the week. The baseline day is the
# median value from the 5-week period Jan 3 – Feb 6, 2020. The baseline isn’t a single value for each region-category—it’s
# 7 individual values. The same number of visitors on 2 different days of the week result in different percentage changes.
# You are given a dataset containing India’s mobility data in 2021. You are expected to do the following for Mumbai City:
# (a) Consider the data given for mobility to be probabilistic in nature. Let’s assume that the data given by Google is
#     probabilistic in nature, and each mobility has a certain probability associated with it. So, on a particular day for a
#     region, we compute the expected mobility using the formula: E[Mobility] = ∑P(Mobility) × Mobility
#############################################################################################################################
# (b) Consider the following distribution during the lockdown period (1/04/2021 to 20/05/2021):
#     Grocery/Pharma Retail Transport Parks Residential Workplace
#     p = 0.2 p = 0.2 p = 0.05 p = 0.02 p = 0.5 p = 0.03
#     Plot the Expected Mobility along with all the other mobilities on the same graph to compare the mobilities.
#############################################################################################################################r
# import libraries
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# reading the file and taking useful data (last 7 rows only for mumbai)
df = pd.read_csv("2021_IN_Region_Mobility_Report.csv")
df = df[df.apply(lambda row: row.astype(str).str.contains('Mumbai', case=False).any(), axis=1)]
col_intrst = df.columns[-7:]
df = df[col_intrst]

# probabilities
prbs = {
    'grocery_and_pharmacy_percent_change_from_baseline': 0.2,
    'retail_and_recreation_percent_change_from_baseline': 0.2,
    'transit_stations_percent_change_from_baseline': 0.05,
    'parks_percent_change_from_baseline': 0.02,
    'residential_percent_change_from_baseline': 0.5,
    'workplaces_percent_change_from_baseline': 0.03
}

# finding expected by above formula
df['Expected_Mobility'] = sum(prob * df[col] for col, prob in prbs.items())
print("Expected Mobility as calculated:",df['Expected_Mobility'])

# plot
plt.figure(figsize=(12, 6))
plt.plot(df['date'], df['Expected_Mobility'], label='Expected Mobility', color='blue')
plt.plot(df['date'], df['grocery_and_pharmacy_percent_change_from_baseline'], label='Grocery/Pharma', color='green')
plt.plot(df['date'], df['retail_and_recreation_percent_change_from_baseline'], label='Retail', color='red')
plt.plot(df['date'], df['transit_stations_percent_change_from_baseline'], label='Transport', color='orange')
plt.plot(df['date'], df['parks_percent_change_from_baseline'], label='Parks', color='purple')
plt.plot(df['date'], df['residential_percent_change_from_baseline'], label='Residential', color='brown')
plt.plot(df['date'], df['workplaces_percent_change_from_baseline'], label='Workplace', color='black')
plt.xlabel('Date')
plt.ylabel('Mobility')
plt.title('Mobility Trends in Mumbai City')
plt.legend()
plt.grid(True)
plt.xticks(rotation=90, ticks=df['date'][::10])
plt.tight_layout()
plt.show()


# (c) Find the Error between the expected mobility and other mobilities using the following error measures,
#
#    i. Root Mean Squared Error.
#   ii. Mean Absolute Error.
#  iii. KL Divergence.
#############################################################################################################################


# drop the NAN values if exist
df = df.dropna()

# define the kl-divergence
def kl_dvg(p, q):
    return np.sum(p * np.log(np.abs(p / q)))

# define the Root Mean Square Error
def rmse(teo, exp):
    return np.sqrt(np.mean((teo - exp) ** 2))

# define the Absolute Mean Error
def mae(teo, exp):
    return np.mean(np.abs(teo - exp))

dict = {}

# Define a list of columns with no exceptional errors
cols_itrst = ['grocery_and_pharmacy_percent_change_from_baseline',
                       'retail_and_recreation_percent_change_from_baseline',
                       'parks_percent_change_from_baseline',
                       'residential_percent_change_from_baseline']

for col in cols_itrst:
    # Calculate RMSE
    rmse_value = rmse(df['Expected_Mobility'], df[col])
    
    # Calculate MAE
    mae_value = mae(df['Expected_Mobility'], df[col])
    
    # Calculate KL Divergence
    kl_div_value = kl_dvg(df['Expected_Mobility'], df[col])
    
    # Store the metrics in a dictionary
    dict[col] = {'RMSE': rmse_value, 'MAE': mae_value, 'KL Divergence': kl_div_value}

# Print the dictionary
for col, values in dict.items():
    print(f"For column {col}:")
    print(f"RMSE: {values['RMSE']}")
    print(f"MAE: {values['MAE']}")
    print(f"KL Divergence: {values['KL Divergence']}")
    print()

# defining column with error in the KL divergence
cols_err_intrst = ['transit_stations_percent_change_from_baseline', 'workplaces_percent_change_from_baseline']
for col in cols_err_intrst:
    if df['Expected_Mobility'].isnull().any() or df[col].isnull().any():
        print(f"NaN values detected in {col}. Skipping calculations.")
        continue
    
    # Calculate RMSE
    rmse_value = rmse(df['Expected_Mobility'], df[col])
    
    # Calculate MAE
    mae_value = mae(df['Expected_Mobility'], df[col])

    # Calculate KL Divergence
    kl_div_value = kl_dvg(df['Expected_Mobility'], df[col])
 
    print(f"For column {col}:")
    print(f"RMSE: {rmse_value}")
    print(f"MAE: {mae_value}")
    print(f"KL Divergence: {kl_div_value}")
    print()



