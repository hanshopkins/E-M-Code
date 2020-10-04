import numpy as np
import matplotlib.pyplot as plt

V_0 = 1 #by choice
eps = 8.854 * 10**-12 #epsilon_0
R = 0.025
d = 5
a = np.sqrt(d**2-R**2)
lambda_1 =(2*np.pi*eps*V_0)/(np.arctanh(np.sqrt(1-(R/d)**2)))

def E_exact (x,y):
    if (((x-d)**2 + y**2 >= R**2) and ((x+d)**2 + y**2 >= R**2)): #avoiding the part that's a conductor
        E_vec = (lambda_1/(2*np.pi*eps)*((x-a)/((x-a)**2 + y**2) - (x+a)/((x+a)**2 + y**2)), lambda_1/(2*np.pi*eps)*((y)/((x-a)**2 + y**2) - (y)/((x+a)**2 + y**2))) ##computiong the vector first the finding magnitude
        return np.sqrt(E_vec[0]**2 + E_vec[1]**2) #finding the magnitude of the vector
    else:
        #setting it to 0 if it's on the conductor
        return 0
        
#finding electric field at a bunch of points then plotting it

matrix_generator = []
points_x = 100 #basically sets the aspect ratio of the graph
points_y = 60
 
x_initial = -8.0
x_final = 8.0
y_center = 0
y_initial = (x_final-x_initial)/2 * points_y/points_x + y_center #make y depend on x and the aspect ratio cenetered around y_center
y_final = -(x_final-x_initial)/2 * points_y/points_x + y_center

for i in range(points_y + 1):
    values = []
    for j in range(points_x + 1):
        x = x_initial + j*(x_final - x_initial)/points_x
        y = y_initial - i*(y_initial-y_final)/points_y
        values.append(E_exact(x,y)) 
    matrix_generator.append(values)

E_magnitudes = np.array(matrix_generator)
        
#finding how the electric field changes relative to an angle around the right wire (at a distance of 0.1 m)
angles = np.linspace(-np.pi, np.pi, 500)
angles_image = []

for theta in angles:
    angles_image.append(E_exact(0.1 * np.cos(theta)-d, 0.1* np.sin(theta)))
        
#plotting the electric field between the two wires at y = 0

xs_1 = np.linspace(-d+R, d-R, 500)
xs_1_image = []

for x_i in xs_1:
     xs_1_image.append(E_exact(x_i, 0))
     
#plotting the electric field near the left wire at y = 0
xs_2 = np.linspace(-d+R, -d+R+0.01, 500)
xs_2_image = []

for x_i in xs_2:
      xs_2_image.append(E_exact(x_i, 0))
 
#drawing the figure s
f1 = plt.figure()
ax1 = f1.add_subplot(111)
ax1.imshow(X = E_magnitudes, extent = (x_initial - (x_final-x_initial)/2/points_x, x_final - (x_final-x_initial)/2/points_x, y_final - (y_final-y_initial)/2/points_y, y_initial + (y_final-y_initial)/2/points_y))
ax1.set_ylabel(r"$y$")
ax1.set_xlabel(r"$x$")
ax1.set_title("Exact Electric Field")
ax1.set_aspect('equal')
     
f2 = plt.figure()
ax1 = f2.add_subplot(111)
ax1.plot(angles, angles_image, marker = '', linestyle = '-')
ax1.set_ylabel(r"$|E|$")
ax1.set_xlabel(r"$\theta$")
ax1.set_title("Electric field in a circle around x = -5, y = 0")


f3 = plt.figure()
ax1 = f3.add_subplot(111)
ax1.plot(xs_1, xs_1_image, marker = '', linestyle = '-')
ax1.set_ylabel(r"$|E|$")
ax1.set_xlabel(r"$x$")
ax1.set_title("Electric field between the two wires with y = 0")
 
f4 = plt.figure()
ax1 = f4.add_subplot(111)
ax1.plot(xs_2, xs_2_image, marker = '', linestyle = '-')
ax1.set_ylabel(r"$|E|$")
ax1.set_xlabel(r"$x$")
ax1.set_title("Electric field near the left wire at y = 0")


print("Electric field at the very edge of the left wire is "+str(E_exact(-d+R,0)))