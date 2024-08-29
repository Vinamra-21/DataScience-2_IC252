import numpy as np
import matplotlib . pyplot as plt
# Question 4: array operations in np.array and np math functions. Plot the function:
# f(x) = (sin^7(x) + cos^5(x))/(e^x)
# in the domain: x ∈ [0, 4].
# Do not use for loops for the same.

def f(x: np . ndarray ) -> np . ndarray :
    return ( np.sin(x)**7 + np.cos(x)**5 )/ np.exp(x)

steps =1000 #note: 4/steps generates 1000 evenly spaced points between 0 and 4)
x= np.arange(0 ,4 , 4/steps )
y= f(x)
plt.plot(x, y, color='black')
plt.title('f(x) = (sin^7(x) + cos^5(x))/(e^x)')
plt.xlabel('x-values')
plt.ylabel('y-values')

plt.tight_layout() #adjust layout

# save/show plot
plt.savefig("q4.png")
plt.show()
