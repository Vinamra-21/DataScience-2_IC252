# 5. Write a python program to estimate the value of π using Monte Carlo simulation. Generate animation of the simulation
# where estimates of π converges with an increase in the number of samples. Plot the Monte Carlo estimate of π where
# x-axis represent number of sample (1 to 3000) and y-axis represent estimate of π.
##########################################################################################################################

# import libraries
import random
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

n_samp = 3000
circle_pt = 0
square_pt = 0
pi_apx_values = []

# limits and axes
fig, ax = plt.subplots()
ax.set_xlim(0, n_samp)
ax.set_ylim(3.14 - 0.5, 3.14 + 0.5)

# stating the line area
line, = ax.plot([], [], lw=2)

# constructor
def init():
    line.set_data([], [])
    return line,

# animate
def animator(i):
    global circle_pt, square_pt
    x_value_rand = random.uniform(-1, 1)
    y_value_rand = random.uniform(-1, 1)
    origin_dist = x_value_rand**2 + y_value_rand**2
    
    # monte-carlo logic
    if origin_dist <= 1:
        circle_pt += 1
    square_pt += 1

    # approximating pi
    pi = 4 * circle_pt / square_pt
    pi_apx_values.append(pi)

    x = list(range(1, len(pi_apx_values) + 1))  
    y = pi_apx_values
    
    line.set_data(x, y)
    
    return line,

# animation
animator = animation.FuncAnimation(fig, animator, init_func=init, frames=n_samp, interval=1, blit=True)

# plotting the exact value of pi from numpy
val_x = np.linspace(1,3001,3000)
val_y = [0]* 3000
for i in range(3000):
    val_y[i] = np.pi

val_y = np.array(val_y)


plt.plot(val_x,val_y, label = "Exact value of π" )
plt.xlabel('Number of Samples')
plt.ylabel('Estimate of π')
plt.title('Monte Carlo Estimation of π')
plt.legend()
plt.grid()
plt.show()

pi_values = []
current_pi = 0

# Creating the figure and adding the circle patch
fig2, ax2 = plt.subplots(figsize=(7, 8))
ax2.add_patch(plt.Circle((0, 0), 1, color='black', fill=False))

# Loop for generating points and estimating pi
for point in range(n_samp):
    x, y = random.uniform(-1, 1), random.uniform(-1, 1)
    if x ** 2 + y ** 2 <= 1:
        current_pi += 1
    pi_values.append(current_pi * 4 / (point + 1))

    ax2.plot(x, y, 'ro', markersize=3,color="skyblue")
    ax2.set_title(f"Current value of pi: {current_pi * 4 / (point + 1):.4f}")
    plt.pause(0.005)

plt.show()

