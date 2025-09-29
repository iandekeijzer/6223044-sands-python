# -*- coding: utf-8 -*-
import numpy as np

def u(start, finish,delay, amplitude):
    t= np.linspace(start,finish,1000)
    return np.where(t<0+delay, 0, amplitude)
 
    
def generate_sine_wave(frequency, duration, sample_rate):
     t= np.linspace (0, duration, sample_rate)
     y= np.sin(frequency*2*np.pi*t)
     return y
 





