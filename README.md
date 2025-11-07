# Python project AES

## Table of Contents
1. [Introduction](#Introduction)
2. [Contents](#Contents)
3. [How to use this repository](#How-to-use-this-repository)


## Introduction
Welcome to my repository, in this repository you shall find a few files which contain functions to generate and modify signals. All of the functions in this repository are written in python. In this README I will explain how to use these afformentioned functions.

## Contents
This repository contains the following:
- a file filled with python functions that describe a few different functions including:
    1. A sine wave function ```generate_sine_wave(frequency, duration, sample_rate```.
    2. A Unit step function ```u(start, finish, amplitude, sample_rate)```.
    3. A function with a modified sine wave function ```modified_sine_wave(frequency, duration, sample_rate, amplitude=1.0)```.
    4. A function with a delayed unit step function ```modified_u(start, finish,delay, amplitude, sample_rate)```.

- a file with functions that run and plot the functions above.

- a toml file which should be used to install all the tools necessary for using the files in this repository

- a file which contains tests to verify the signal functions

- a file which was used to test if we were able to correctly, add, commit and push our files to our repository.
## How to use 
To preface: to be able to use these functions you need to install the numpy and matplotlib modules onto your computer

We have two main files we should use, signals.py, which contains all the signals mentioned above, and run.py, which we use to run and plot the signals we made with signals.py.
Using the functions contained within the signals file, we can open the run.py file and generate and plot signals using to matplotlib.pyplot.
Within the run.py file you can choose your own values for each variable in the function, for example you can choose how far to delay the unit step function, or choose another frequency for the sine wave function.

If needed you can also use the ```test_python_functions``` file to see if the functions work properly, if so you should see the following result:

![Test result](Users/iande/pytest_succes.png)

But most importantly, have fun when using this repository.



