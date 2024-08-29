# 4. Create a Python class BivariateGaussianDistribution for a continuous random variable (X,Y ). Include methods for:
# ..init(self,mean_x,mean_y,var_x,var_y,cov): Initialize with a function that calculates the joint PDF for given values
# of X and Y .
# ..calculate_pdf(self,x,y): This method should return the joint PDF value for input x and y.
# ..marginal_pdf_x(self,x): This method should calculate and return the marginal PDF of X for a given value of x
# (integrate the joint PDF over all possible Y values). (Bonus: Implement marginal pdf y for Y )
# ..plot_pdf_contour(self): This method should create a contour plot visualizing the joint PDF using libraries like
# matplotlib.
# A snippet of the code for above problem is:
# class BivariateGaussian(BivariateDistribution):
# def __init__(self, mean_x, mean_y, var_x, var_y, cov):
# # ... (initialize parameters for a bivariate Gaussian distribution)
# # Example usage
# distribution = BivariateGaussian(...)
# pdf_value = distribution.calculate_pdf(1.5, 2.0)
# marginal_pdf_x = distribution.marginal_pdf_x(1.0)
# distribution.plot_pdf_contour()
###############################################################################################################################

#import libraries
import numpy as np
import matplotlib.pyplot as plt

class BivariateGaussianDistribution:
    
    # constructor
    def __init__(self, mean_x, mean_y, var_x, var_y, cov):
        self.mean_x = mean_x
        self.mean_y = mean_y
        self.var_x = var_x
        self.var_y = var_y
        self.cov = cov

    def calculate_pdf(self, x, y):   #pdf
        exp = -0.5 * ((x - self.mean_x)**2 / self.var_x + (y - self.mean_y)**2 / self.var_y - 2 * self.cov * (x - self.mean_x) * (y - self.mean_y) / (self.var_x * self.var_y - self.cov**2))
        cof = 1 / (2 * np.pi * np.sqrt(self.var_x * self.var_y - self.cov**2))
        return cof * np.exp(exp)

    def marginal_pdf_x(self, x): #marginal x
        y_values = np.linspace(-10, 10, 1000)
        pdf_values = np.array([self.calculate_pdf(x, y) for y in y_values])
        return np.trapz(pdf_values, y_values)

    def marginal_pdf_y(self, y): #marginal y
        x_values = np.linspace(-10, 10, 1000)
        pdf_values = np.array([self.calculate_pdf(x, y) for x in x_values])
        return np.trapz(pdf_values, x_values)

    def plot_pdf_contour(self):     # plot
        x = np.linspace(-10, 10, 100)
        y = np.linspace(-10, 10, 100)
        X, Y = np.meshgrid(x, y)
        Z = self.calculate_pdf(X, Y)
        plt.figure(figsize= (12,6))
        plt.contourf(X, Y, Z, cmap='viridis')
        plt.xlabel('X')
        plt.ylabel('Y')
        plt.title('Bivariate Gaussian PDF Contour Plot')
        plt.colorbar()
        plt.show()

# Example usage
mean_x = 0
mean_y = 0
var_x = 1
var_y = 2
cov = 0.5
distribution = BivariateGaussianDistribution(mean_x, mean_y, var_x, var_y, cov)
pdf_value = distribution.calculate_pdf(1.5, 2.0)
mrg_val_x = distribution.marginal_pdf_x(1.0)
mrg_val_y = distribution.marginal_pdf_y(1.0)
distribution.plot_pdf_contour()
