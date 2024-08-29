#################################STIRLING'S FORMULA###################################
#importing libraries
import matplotlib.pyplot as plt
import numpy as np

def facto(k): #factorial calculator
    if k==0:
        fact=1
        return fact
    else:
        fact=1
        for i in range(1,k+1):
            fact=fact*i
        return fact

def formu(x_values,y_values):   #ratio calculator given in ps
    for i in x_values:
        sum=((facto(i))/(((2*np.pi*i)**(1/2))*((i/np.e)**i)))
        y_values.append(sum)

y_values=[]                  #y-values list for graph
x_values=list(range(1,100,1)) #x-values list for graph
formu(x_values,y_values) 
#plot-graph
plt.plot(x_values,y_values) 
plt.xlabel("x-values") 
plt.ylabel("y-values")
plt.yticks(np.arange(1,1.25,.05)) #defining points on the y-axis
plt.title(f"Plot of ratio : n!/((√(2nπ)).((n/e)^n))")
plt.grid(True)
plt.tight_layout()

#show/save graph
plt.savefig("Q02_graph.png") 
plt.show()
