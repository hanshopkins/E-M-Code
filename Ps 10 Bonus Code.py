import numpy as np
import matplotlib.pyplot as plt

#defining the function that gives the z coordinate of the vector potential from a finite wire
def vector_potential (s, z, z_1, z_2): #I'm choosing units to that I mu_0/4 pi = 1
    return np.log(np.abs((np.sqrt(s**2 + (z_2-z)**2) + (z_2-z))/(np.sqrt(s**2 + (z_1-z)**2) + (z_1-z))))

#step 2, given two points, find what s and z are going to be from a position u, calculate the above function, then return a vector in the direction of the wire
def deal_with_line_angle(u, p_1, p_2):
    #first translating everything so that p_1 = (0,0)
    p_2 = p_2 - p_1
    u = u - p_1
    wirelength = np.linalg.norm(p_2)
    if wirelength == 0:
        print("Critical error. 0 length wire.")
    else:
        p_2 = (1.0/wirelength) * p_2 #normalizing the vector
        #I guess to find s and z, we need to project onto the wire segment
        z_value = np.dot(u, p_2.T)
        s_value = np.linalg.norm(u - z_value * p_2)
        
        if s_value != 0: #it can't compute for s = 0
            #then the vector potential is given by the above function in the direction of the wire
            #since we set p_1 to 0, we can set z_1 = 0, z_2 = the distance between p_1 and p_2
            return vector_potential(s_value, z_value, 0, wirelength) * p_2
        else: #to avoid errors, it just returns 0 if it breaks
            return np.array([0,0])
        
n = 50 ##number of points in the loop

#setting up the circular loop of points
circle_xs = []
circle_ys = []
theta = 0
for i in range(n):
    theta = i/n * 2 * np.pi
    circle_xs.append(np.cos(theta)) #setting the radius to be 1
    circle_ys.append(np.sin(theta))
    
#setting up the square loop of points
square_xs = []
square_ys = []
distance = 0
for i in range(n):
    distance = 4 * i/n
    if distance <= 1:
        square_xs.append(0.5)
        square_ys.append(distance-0.5)
    elif distance <= 2:
        square_xs.append(0.5-distance+1)
        square_ys.append(0.5)
    elif distance <= 3:
        square_xs.append(-0.5)
        square_ys.append(0.5-distance+2)
    else:
        square_xs.append(-0.5+distance-3)
        square_ys.append(-0.5)

def loop_vec_pot (x, y, points_x, points_y):
    total_vec_pot = np.array([0,0])
    for i in range(len(points_x)):
        if i != len(points_x)-1:
            total_vec_pot = total_vec_pot + deal_with_line_angle(np.array([x,y]), np.array([points_x[i],points_y[i]]), np.array([points_x[i+1],points_y[i+1]]))
        else: #if it's the last one, we connect it back to the first
            total_vec_pot = total_vec_pot + deal_with_line_angle(np.array([x,y]), np.array([points_x[i],points_y[i]]), np.array([points_x[0],points_y[0]]))
    return total_vec_pot

print("Vector potential at (0,50) from the circle loop: "+str(loop_vec_pot (0,50, circle_xs, circle_ys)))
print("Vector potential at (0,50) from the square loop: "+str(loop_vec_pot (0,50, square_xs, square_ys)))