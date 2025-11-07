import numpy as np
import signals as sig 

#testing generate_sine_wave function
def test_generate_sine_wave():
    t, y = sig.generate_sine_wave(4,2,10000)
    assert len(t) == 10000
    assert y[0] == 0
    assert np.isclose(max(y), 1, atol=1e-6)

#testing modified_sine_wave function
def test_modified_sine_wave():
    t, y = sig.modified_sine_wave(5, 2, 10000,amplitude=10.0)
    assert len(t) == 10000
    assert y[0] == 0 
    assert np.isclose(max(y), 10, atol=1e-6)
 
#testing unit step function
def test_u():
    t, y= sig.u(-10,10,3,10000)
    assert len(t) == 10000
    assert np.isclose(max(y),3, atol=1e-6)
    assert y[0] == 0
    assert y[9000] == 3

#testing modified unit step function
def test_modified_u():
    t, y= sig.modified_u(-10,10,-2,3,10000)
    assert len(t) == 10000
    assert np.isclose(max(y), 3, atol=1e-6)
    assert y[0] == 0
    assert y[9000] == 3