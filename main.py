import numpy as np
import scipy as sp
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt
from src.odes import ClimateODEs, ClimateVec

def main():
    # Initial values
    p = 0.01 # GDP of poorer country relative to rich
    y0 = ClimateVec(1, p, 1, 1, 1) # Model is normalized so that all values are in terms of present day values
    
    # Set system parameter values
    climate = ClimateODEs(1,1,1.2,1.2,1,1,1)
    
    # Define timeframe
    # N = 100000
    t_span = (0, 100)
    
    # Run the model
    result = solve_ivp(climate.vec_de, t_span, y0)
    print(result)

if __name__ == "__main__":
    main()
