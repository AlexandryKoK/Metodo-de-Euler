import numpy as np
import math

def edo(x,y):
    return np.exp(-x)*np.sin(y**2)
    #return (-1.2*y + 7*np.exp(-0.3*x))

print('x_0 =')
x = float(raw_input())

print('y_0 =')
y = float(raw_input())

print('Passos=')
h = float(raw_input())

def rungekutta(x,y,h):
    for i in range(1,2):
        y0=y
        x0=x
        k1 = edo(x0,y0)
        #print(k1)
        k2 = edo(x0 + 0.5*h, y0 + 0.5*k1*h)
        #print(k2)
        k3 = edo(x0 + 0.5*h, y0 + 0.5*k2*h)
        #print(k3)
        k4 = edo(x0 + h, y0 + k3*h)
        #print(k4)
        y = y0 + (1.0 / 6.0)*(k1 + 2 * k2 + 2 * k3 + k4)*h
        print(y)
        x = x0 + h 
        print(x)
    

rungekutta(x,y,h)

