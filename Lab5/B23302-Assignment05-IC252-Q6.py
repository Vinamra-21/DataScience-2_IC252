# 6. Evaluate the integral  f(x) = ∫π0  sin^4(3x)dx
# using a Monte Carlo approach. Generate animation of the simulation where estimates of the integral converges with an
# increase in the number of samples. Plot the Monte Carlo estimate of integral where x−axis represent number of sample
# (1 to 2000) and y−axis represent estimate of ∫10 f(x)dx. Also, calculate the exact value of the integration and compare it
# with the simulated one.
#############################################################################################################################

# import libraries
from scipy import integrate
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

#integration range
a = 0
b = np.pi
c = 1

# fn to integrate
def f(x):
  return (np.sin(3*x))**4

n_samp = 2000

x_values = np.random.uniform(a, b, (n_samp, n_samp))
estimate_int = (b - a) * np.sum(f(x_values), axis=1) / n_samp
exact_int, err = integrate.quad(f, a, b)

fig = plt.figure(figsize=(12, 6)) # plot
plt.xlim(-0.5, n_samp)
plt.ylim(exact_int - 0.5, exact_int + 0.5)
plt.title('Monte Carlo Estimation of Integral')
plt.xlabel('Number of Samples')
plt.ylabel('Estimating Integral')
plt.grid()

# assigning for eaxct and error value on same
line_md, = plt.plot([], [], lw=2)
line_ex, = plt.plot([], [], lw=2, linestyle='-.')

# consturctor
def init():
    line_md.set_data([], [])
    line_ex.set_data([], [])
    return line_md, line_ex

def ani(frm):
    line_md.set_data(range(frm + 1), estimate_int[:frm + 1])
    line_ex.set_data(range(frm + 1), [exact_int]* (frm + 1))
    return line_md, line_ex

# animation
ani = animation.FuncAnimation(fig, ani, init_func=init, frames=n_samp, interval=50, blit=True)
plt.show()
