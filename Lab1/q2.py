import numpy as np
import matplotlib . pyplot as plt
# Question 2: Bins! Yes binning might be tricky if you want to plot meaningful plots, in the below histogram choose an
# appropriate binning size, expiriment with the bins style, location, borders and colors. Explore the np.arange function. Add
# meaningful labels to both axes.

val = np.random.normal(size =(100),scale =3,loc =10)
hbins =np.arange(0,20,1)
plt.hist(val, bins=hbins, color='lightgreen', edgecolor='black', alpha=0.7) #histogram plot
#defining labels and title
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.title('Histogram of Randomly gnerated Data')
plt.grid(1,axis='y')
plt.tight_layout() #adjust layout

# save/show plot
plt.savefig("q2.png")
plt.show()