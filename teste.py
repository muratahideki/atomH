import vpython as vp
import numpy as np


R = 2
r = 0.5
t = 0

w =10#frequencia 

dt = 0.01
   
    
#criando objetos 
atom = vp.sphere(pos=vp.vector(0, 0, 0), radius=0.15, color=vp.color.red)
electron = vp.sphere(pos=vp.vector(R,0, 0), radius=0.08, color=vp.color.green, make_trail = True, retain = 250)
wave = vp.sphere(pos=vp.vector(R,0,r), radius=0.05, color=vp.color.blue, make_trail = True, retain = 250)

t = 1
while True:
    vp.rate(1/dt)
    xye = [R*np.cos(t),R*np.sin(t)]
    electron.pos = vp.vector(xye[0],xye[1],0)

    xyw = [R*np.cos(t) + r*np.cos(w*t),electron.pos.y,r*np.sin(w*t)]
    wave.pos = vp.vector(xyw[0],xyw[1],xyw[2])



    t = t+dt
