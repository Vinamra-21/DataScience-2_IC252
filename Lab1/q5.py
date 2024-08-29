import numpy as np
import matplotlib . pyplot as plt
# Question 5: Create a subplot with two plots side by side. Plot a sine wave in the first subplot. Plot a cosine wave in the
# second subplot. Add labels, titles, and a legend to the plots.

x = np.linspace(0, 2 * np.pi, 100) #x values for both sin and cos
y_sin = np.sin(x) #y values for sine
y_cos = np.cos(x) #y values for cosine
fig, axs = plt.subplots(1, 2, figsize=(12, 4))  #layout 2 subplots

# Plot1 sine wave
axs[0].plot(x, y_sin, label='Sine Wave', color='black')
axs[0].set_title('Sine Wave (y=sin(x))')
axs[0].set_xlabel('x-values')
axs[0].set_ylabel('y-values')
axs[0].legend()

# Plot2 cosine wave
axs[1].plot(x, y_cos, label='Cosine Wave', color='black')
axs[1].set_title('Cosine Wave (y=cos(x))')
axs[1].set_xlabel('x-values')
axs[1].set_ylabel('y-values')
axs[1].legend()

plt.tight_layout() #adjust layout

# save/show plot
plt.savefig("q5.png")
plt.show()

