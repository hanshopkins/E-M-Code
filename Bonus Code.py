import numpy as np
import matplotlib.pyplot as plt

#choosing R = 1

#setting up the charges in a square grid
def set_charge (r_sq):
    return np.e**(-r_sq/2.0)
    
rows = 100 #number of rows and columns

charge_q = []
charge_x = []
charge_y = []

for i in range(rows):
    for j in range(rows):
        charge_q.append(set_charge((-2 + i * 4/rows)**2 + (2 - j * 4/rows)**2))
        charge_x.append(-2 + i * 4/rows)
        charge_y.append(2 - j * 4/rows)

#finding potential with the formula v = q/d (using units such that 4 pi epsilon_0 are 1)
matrix_generator = []
points = 50 #the actual number of points is this squared

for i in range(points + 1):
    values = []
    for j in range(points + 1):
        y = -4 + j*8/points #starting from x = -4 R why not
        z = 4 - i*8/points
        voltage_sum = 0
        for k in range(len(charge_q)): #calculating the voltage for each charge
            d = np.sqrt((charge_x[k])**2 + (y - charge_y[k])**2 + z**2)
            if d > 0.001: #ignoring the charges that are right on the point, which hopefully doesn't ruin it too much
                voltage_sum += charge_q[k]/d
            else:
                voltage_sum += charge_q[k]/0.001 #or else just add a high potential
        values.append(voltage_sum) 
    matrix_generator.append(values)

potential = np.array(matrix_generator)
#drawing the figure
f1 = plt.figure()
ax1 = f1.add_subplot(111)
ax1.imshow(X = potential, extent = (-4 - 4/points, 4 + 4/points, -4 - 4/points, 4 + 4/points))
ax1.set_ylabel(r"$z$")
ax1.set_xlabel(r"$y$")
ax1.set_title("Thin plane with charge distribution")
ax1.set_aspect('equal')