# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np

def u(start, finish,delay, amplitude):
    t= np.linspace(start,finish,1000)
    return np.where(t<0+delay, 0, amplitude)



