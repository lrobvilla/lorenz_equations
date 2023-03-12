import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from scipy.integrate import odeint
from mpl_toolkits.mplot3d import Axes3D

#black background
plt.style.use(['dark_background'])

#lorenz system of equation with its classical parameters
def lorenz_eq(variables, t, beta = 8/3, sigma = 10 , rho = 28):
    x, y, z = variables
    d_x = sigma * (y - x)
    d_y = x * (rho - z) - y
    d_z = x * y - beta * z
    return d_x, d_y, d_z

# some possible initial conditions 
#st0 = [0, 1, 1.05]
st0 = [1,1,20]
st1 = [1.3,1.04,20]
st2 = [1.7,1.8,19.86]
st3 = [2, 1.34, 20 + 10/33]
# st0= [60,65,10]
# st1 = [-50,30,6]

t0 = np.linspace(0, 100, 20000)
n = len(t0)

#solutions for the several initial conditions and the same time interval
sol0 = odeint(lorenz_eq, st0, t0)
sol1 = odeint(lorenz_eq, st1, t0)
sol2 = odeint(lorenz_eq, st2, t0)
sol3 = odeint(lorenz_eq, st3, t0)

#initialization and settings for the figure and the plots
fig = plt.figure('Soluciones en tiempo real',figsize=(8, 6), dpi = 100)
ax1 = fig.add_subplot(111, projection='3d')
fig.subplots_adjust(top = 0.914, bottom= 0, right= 0.855)

p0, = ax1.plot([], [], [], color='#57D702', linewidth=0.78, alpha = 0.9) #verde
p1, = ax1.plot([], [], [], color = '#AD2929', linewidth = 0.78, alpha = 0.7) #rojo
p2, = ax1.plot([], [], [], color='#2045CF', linewidth=0.78, alpha = 0.5) #azul
p3, = ax1.plot([], [], [], color='#F39C12', linewidth=0.78, alpha = 0.4) #~mostaza

#the next function initializes the animation
def init_func():

    ax1.set_xlim3d(-30,30)
    ax1.set_ylim3d(-30,30)
    ax1.set_zlim3d(0,30)
    # ax.set_xlabel("x")
    # ax.set_ylabel("y")
    # ax.set_zlabel("z")
    ax1.set_axis_off()

#the next function updates the plots in every moment of time t of t0
def animate(i):
# this next lines rotates the animation
    ax1.view_init(elev=5,azim = i/4+1)


    p0.set_data(sol0.T[0][:i], sol0.T[1][:i])
    p0.set_3d_properties(sol0.T[2][:i])

    p1.set_data(sol1.T[0][:i], sol1.T[1][:i])
    p1.set_3d_properties(sol1.T[2][:i])

    p2.set_data(sol2.T[0][:i], sol2.T[1][:i])
    p2.set_3d_properties(sol2.T[2][:i])

    p3.set_data(sol3.T[0][:i], sol3.T[1][:i])
    p3.set_3d_properties(sol3.T[2][:i])

#a very fast interval of time: 1/(2**64), 
#some decent time intervals are: 5,8,10 (greater than 15 makes the animation too slow)

#FuncAnimation calls first the init_func and then iterates animate by passing as parameters the values of frames
anim = FuncAnimation(fig,
                     animate,
                     frames = range(0,n,3),
                     interval = 0,
                     init_func = init_func(),
                     repeat = False,
                     cache_frame_data = False)

plt.show()