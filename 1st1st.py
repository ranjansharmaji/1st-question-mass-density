import numpy as np
import matplotlib.pyplot as ml
import scipy.constants import pi 

def f(x):
    return 10*4*x*x*pi

def trap(f,n,a,b):
    h=(b-a)/float(n)
    intgr=0.5*h*(f(a)+f(b))
    for i in range(1,int(n)):
        intgr=intgr+h*f(a+i*h)
    return intgr

a=0
b=10
n=3
print(trap(f,n,a,b))
    
    

