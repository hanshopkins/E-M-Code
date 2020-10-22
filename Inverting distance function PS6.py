import numpy as np
import matplotlib.pyplot as plt

eps_0 = 8.8541878176 * 10**-12
k = 1/(4* np.pi * eps_0)
R = 3.5 * 10**-10
q = 1.6021766 * 10**-10
def the_func(a):
    if (a - R**2/a) != 0:
        return k * q**2 * (-R/(a*(a - R**2/a)**2) + (R+a)/a**3)
    else:
        return 0

def approxInvert (func, y, l,h, precision, direction):
    #in order for this function to work, it needs to be in a continuous region that is monotonic
    #by the way, direction means increasing or decreasing. I couldn't come up with a better word.
    toggle = True
    k = np.abs(h-l)/10 #the width of the divisions
    pos = l
    while toggle == True:
        if direction == "decreasing" or direction == "dec": 
            while func(pos+k) > y:
                pos = pos + k
        elif direction == "increasing" or direction == "inc": 
            while func(pos+k) < y:
                pos = pos + k
        k = k/10
        if k <= precision/10: #set precision to the order of magnitude you want
            toggle = False
    return pos

print("The func inverted at 0 is " + str(approxInvert(the_func, 0, 5.66311896*10**-10, 5.66311896*10**-10 + 10**-19, 0.0000001, "inc")))

##inputing data

domain = []
image = []
for i in range(1000):
    x = 5.66311896*10**-10 + i/1000*10**-19
    domain.append(x)
    image.append(the_func(x))

f1 = plt.figure()
ax1 = f1.add_subplot(111)
ax1.plot(domain,image,marker = '', ls = '-',color="blue")
ax1.set_ylabel("F")
ax1.set_xlabel("a")