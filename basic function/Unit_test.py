import numpy as np
from function import fit_line

def test_fit_line_correct_values():
    #Generating simple data y = 2x + 1
    x = np.array([0, 1, 2, 3, 4])
    y = 2 * x + 1

    slope, intercept = fit_line(x, y)
    assert round(slope, 2) == 2.00
    assert round(intercept, 2) == 1.00

def test_fit_line_with_noise():
    x = np.array([0, 1, 2, 3, 4])
    y = 2 * x + 1 + np.random.normal(0, 0.1, size=len(x))
    slope, intercept = fit_line(x, y)

    #Checking the values the slope is close to
    assert abs(slope - 2) < 0.2
    assert abs(intercept - 1) < 0.2
