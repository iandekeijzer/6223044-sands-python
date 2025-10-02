import signals as sig
import matplotlib.pyplot as plt

#generate sine wave function
t, y = sig.generate_sine_wave(4,2,100)
plt.figure(1)
plt.plot(t, y)
plt.grid(True)
plt.title("Sine wave")
plt.xlabel("Time")
plt.ylabel("Amplitude")


#generate unit step function
t, y= sig.u(-10,10,3,10000)
plt.figure(2)
plt.plot(t, y)
plt.grid(True)
plt.title("Unit step function")
plt.xlabel("Time")
plt.ylabel("Height")


#generate a modified sine wave with a predetermined amplitude
t,y = sig.modified_sine_wave(5, 2, 1000,amplitude=10.0)
plt.figure(3)
plt.plot(t, y)
plt.grid(True)
plt.title("Modified Sine wave")
plt.xlabel("Time")
plt.ylabel("Amplitude")


#generate a modified unit step function with a predetermined delay
t, y= sig.modified_u(-10,10,-2,3,10000)
plt.figure(4)
plt.plot(t, y)
plt.grid(True)
plt.title("Modified Unit step function")
plt.xlabel("Time")
plt.ylabel("Height")
plt.show() 
