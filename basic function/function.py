import numpy as np
from scipy.stats import linregress

#Fits a line with linear regression then returns slope and intercept
def fit_line(x, y):
    slope, intercept, r_value, p_value, std_err = linregress(x, y)
    return slope, intercept
