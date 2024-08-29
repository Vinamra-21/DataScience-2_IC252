###############################BIRTHDAY PARADOX######################################

######################### by performing  trials ########################
#import library
import numpy as np
import matplotlib.pyplot as plt

# n = 1000 #Number of trials

# x_values=list(range(2,101,1))         #x-values for graph
# y_values = []                         #y-values for graph

# for i in x_values:    #iterating x_values(number of people)
#     win = 0
#     for _ in range(n): #trials
#         bday = []     
#         for _ in range(i):
#             bday.append(np.random.randint(1, 366))
#         uniq_bday = set(bday)
#         if len(uniq_bday) < len(bday):
#             win+=1
#     y_values.append(win/n)

# # plot-graph
# plt.figure(figsize=(8,5))  #graph-fig-size
# plt.plot(x_values,y_values)
# plt.xlabel("Number of people (K)")
# plt.ylabel("Probability")
# plt.title("Probability that atleast one pair of people in the group of K have the same birthday")
# plt.grid(True)
# plt.tight_layout()

# # save/show plot
# plt.savefig("Q01_trials_graph.png")
# plt.show()

########################################################################################

################ using formula #######################
#import library
import matplotlib.pyplot as plt

y_values=[]                           #y-values for graph

def probab(x_values,y_values,n=365):  #probability calculation
    for i in x_values:
        sum=1
        for t in range(i):
            sum*=((n-t)/n)
        new_sum=(1-sum)
        y_values.append(new_sum)
 
x_values=list(range(2,101,1))         #x-values for graph
probab(x_values,y_values)
# plot-graph
plt.figure(figsize=(8,5))  #graph-fig-size
plt.plot(x_values,y_values)
plt.xlabel("Number of people (K)")
plt.ylabel("Probability")
plt.title("Probability that atleast one pair of people in the group of K have the same birthday")
plt.grid(True)
plt.tight_layout()

# save/show plot
plt.savefig("Q01_formula_graph.png")
plt.show()



