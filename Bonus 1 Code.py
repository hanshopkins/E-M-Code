import numpy as np
import matplotlib.pyplot as plt
from scipy.special import comb

V_0 = 1 #by choice
R = 1 #also by choice
n_max = 55 #the highest n I want to calculate to
theta_0 = np.pi/2

#defining the legendre polynomials with a formula I found on wikipedia
def legp (n,x):
    sum_ = 0
    for k in range(n+1):
        sum_ += comb(n,k, exact = True)**2 * (x-1)**(n-k) * (x+1)**k
    return 1/2**n * sum_

#building the matrix to invert
matrix_generator = []

for i in range(n_max+1):
    theta = (i/n_max)*np.pi
    values = []
    
    if theta <= theta_0: #switching the cases depending on theta
        for j in range(n_max+1):
            values.append(R**j * legp(j, np.cos(theta)))
        matrix_generator.append(values)
    else:
        for j in range(n_max+1):
            values.append((2*j +1) * R**(j-1) * legp(j, np.cos(theta)))
        matrix_generator.append(values)

matrix = np.array(matrix_generator)

#creating RHS
matrix_generator = []

for i in range(n_max+1):
    theta = (i/n_max)*np.pi
    if theta <= theta_0:
        matrix_generator.append(V_0)
    else:
        matrix_generator.append(0)

RHS = np.array(matrix_generator)
RHS.transpose()

#inversing the big matrix
matrix = np.linalg.inv(matrix)

#muliplying to find coefficients
coefficients = np.matmul(matrix, RHS)

#finding the potential for all theta
angles = np.linspace(0, np.pi, 500)
angles_image = []

for theta in angles:
    sum_ = 0
    for i in range(n_max+1):
        sum_ += coefficients[i] * R**i * legp(i, np.cos(theta))
    angles_image.append(sum_)
        
#plotting the potential versus theta    
f1 = plt.figure()
ax1 = f1.add_subplot(111)
ax1.plot(angles, angles_image, marker = '', linestyle = '-')
ax1.set_ylabel(r"Potential $V$")
ax1.set_xlabel(r"$\theta$")
ax1.set_title(r"The potential on the sphere for $\theta_0 = \frac{\pi}{2}$")

#doing a similar thing for charge distribution

#building the matrix with the charge equations
matrix_generator = []

for i in range(n_max+1):
    theta = (i/n_max)*np.pi
    values = []
    for j in range(n_max+1):
        values.append((2*j +1) * R**(j-1) * legp(j, np.cos(theta)))
    matrix_generator.append(values)

matrix = np.array(matrix_generator)

charge_values = np.matmul(matrix, coefficients.transpose())

angles = []
for i in range(n_max+1):
    angles.append((i/n_max)*np.pi)

f2 = plt.figure()
ax1 = f2.add_subplot(111)
ax1.plot(angles, charge_values, marker = '', linestyle = '-')
ax1.set_ylabel(r"Charge Density $\rho$")
ax1.set_xlabel(r"$\theta$")
ax1.set_title(r"The charge density on the sphere for $\theta_0 = \frac{\pi}{2}$")