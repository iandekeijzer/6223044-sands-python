import numpy as np
import signals as sig 

def test_modified_sine_wave():
    t, y = sig.modified_sine_wave(5, 2, 1000,amplitude=10.0)
    assert len(t) == 1000
    assert y[0] == 0 