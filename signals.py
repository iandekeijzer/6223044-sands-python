# -*- coding: utf-8 -*-
import numpy as np

#defines the unit-step funtion 
def u(start, finish, amplitude, sample_rate):
    """
    Generate a unit step function.

    Parameters
    ----------
    start : float or int
        The starting value of the time axis.
    finish : float or int
        The ending value of the time axis.
    amplitude : float or int
        The height of the unit step function after t >= 0.
    sample_rate : int
        The number of samples between `start` and `finish`.

    Returns
    -------
    t : numpy.ndarray
        The time values from `start` to `finish`.
    y : numpy.ndarray
        The amplitude values (0 for t < 0, `amplitude` for t >= 0).
    """
    t= np.linspace(start,finish,sample_rate)
    y = np.where(t < 0, 0, amplitude)
    return t, y


#defines the sine wave function
def generate_sine_wave(frequency, duration, sample_rate):
    """
    Generate a sine wave.

    Parameters
    ----------
    frequency : float
        The amount of cycli per second of the sine wave in Hz.
    duration : float
        The duration of the sine wave in seconds.
    sample_rate : int
        The number of samples per second.

    Returns
    -------
    t : numpy.ndarray
        The time values from 0 to `duration`.
    y : numpy.ndarray
        The sine wave values at the given time points.
    """
    t= np.linspace (0, duration, sample_rate)
    y= np.sin(frequency*2*np.pi*t)
    return t, y

#defines the modification of the original sine wave function
def modified_sine_wave(frequency, duration, sample_rate, amplitude=1.0):
    """
    Generate a sine wave with adjustable amplitude.

    Parameters
    ----------
    frequency : float
        The amount of cycli per second of the sine wave in Hz.
    duration : float
        The duration of the sine wave in seconds.
    sample_rate : int
        The number of samples per second.
    amplitude : float, optional
        The amplitude of the sine wave (the default is 1.0).

    Returns
    -------
    t : numpy.ndarray
        The time values from 0 to `duration`.
    y : numpy.ndarray
        The sine wave values scaled by `amplitude`.
    """
    t= np.linspace (0, duration, sample_rate)
    y= amplitude*np.sin(frequency*2*np.pi*t)
    return t, y

#defines the modification of the original unit step function
def modified_u(start, finish,delay, amplitude, sample_rate):
    """
    Generate a delayed unit step function.

    Parameters
    ----------
    start : float or int
        The starting value of the time axis.
    finish : float or int
        The ending value of the time axis.
    delay : float or int
        Time delay applied to the step (step occurs at t = `delay`).
    amplitude : float or int
        The height of the unit step function after t >= delay.
    sample_rate : int
        The number of samples between `start` and `finish`.

    Returns
    -------
    t : numpy.ndarray
        The time values from `start` to `finish`.
    y : numpy.ndarray
        The amplitude values (0 for t < delay, `amplitude` for t >= delay).
    """
    t= np.linspace(start,finish,sample_rate)
    y = np.where(t < 0, 0, amplitude)
    return t, y




