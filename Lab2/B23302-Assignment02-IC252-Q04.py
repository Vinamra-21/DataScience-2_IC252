############################### sum of two dice ################################

#importing libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

n=10000  #number of trials
die1=np.random.randint(1,7,n) #die rolls
die2=np.random.randint(1,7,n)
#dict to store frequency of each sum
sum_dict={"sum_2":[0],"sum_3":[0],"sum_4":[0],"sum_5":[0],"sum_6":[0],"sum_7":[0],"sum_8":[0],"sum_9":[0],"sum_10":[0],"sum_11":[0],"sum_12":[0]}

for i in range(n):  #calculate sum of two die and increase it in respective list 
    temp=die1[i]+die2[i]
    sum_dict[f"sum_{temp}"][0]+=1
    
x_values=[]  #x-values list for graph
y_values=[]  #y-values list for graph

for i in range(2,13):      #calculate and append probability
    sum_dict[f"sum_{i}"].append((sum_dict[f"sum_{i}"][0])/n)
    x_values.append(i) 
    y_values.append(sum_dict[f"sum_{i}"][1])
   
#make dataframe to display frequency and probability of each sum
Table=pd.DataFrame.from_dict(sum_dict, orient='index',columns=['Frequency','Probability']) 
#save as csv
# Table.to_csv("Q04_table.csv")  
print(Table)
#plot-graph
plt.figure(figsize=(8,5)) #graph-fig-size
plt.bar(x_values,y_values,width=.7)
plt.xlabel("Value of Sum of numbers on two dice ")
plt.ylabel("Probability")
plt.title("Probability distribution of the sum of the numbers obtained on the two dice")
plt.xticks(x_values,list(sum_dict.keys()))  #defining name of points on x-axis
plt.grid(True)
plt.tight_layout()

#save/show plot
plt.savefig("Q04_graph.png")
plt.show()


        


