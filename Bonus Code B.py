import numpy as np
import matplotlib.pyplot as plt

def calc_E_field (z, charge_x, charge_y):
    r = np.sqrt(charge_x**2 + charge_y**2 + z**2)
    z_component = z/r
    return z_component/r**2 #(using units such that 4 pi epsilon_0 are 1)

def calc_disc (z):
    E = 0
    rows = 100 #number of rows and columns
    for i in range(rows):
        for j in range(rows):
            if (-1 + i * 2/rows)**2 + (1 - j * 2/rows)**2 <= 1: #checking if it's in the circle of radius 1
                E += calc_E_field(z, -1 + i * 2/rows, 1 - j * 2/rows)
    return E

omega = np.linspace(0.1,0.2,20)
image = []
for x_i in omega:
    image.append(calc_disc(x_i))

f1 = plt.figure()
ax1 = f1.add_subplot(111)
ax1.plot(omega, image, marker = '.', ls = '')
ax1.set_ylabel(r"$|\mathbf{E}|$")
ax1.set_xlabel(r"$h$")
ax1.set_title("Plotting magnitude of electric field")
ax1.set_yticklabels([])
#ax1.set_xticklabels([])