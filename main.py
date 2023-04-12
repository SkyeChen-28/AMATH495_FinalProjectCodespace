import numpy as np
import scipy as sp
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt
from src.odes import ClimateODEs

def main():
    # Initial values
    p = 0.01 # GDP of poorer country relative to rich
    y0 = np.array([1, p, 1, 1, 1]) # Model is normalized so that all values are in terms of present day values
    
    # Set system parameter values
    climate = ClimateODEs(1,1,1.1,1.1,1,1,1)
    
    # Define timeframe
    # N = 100000
    t_span = (0, 100)
    
    # Run the model
    result = solve_ivp(climate.vec_de, t_span, y0)

    # Parse results
    t = result.t
    y = result.y
    r = y[0]
    p = y[1]
    I_r = y[2]
    I_p = y[3]
    c = y[4]
    
    # Plot results
    # fig, axs = plt.subplots(3, 1)
    fig, axs = plt.subplots(1, 3)
    GDP_idx = 0
    innovation_idx = 1
    CO2_idx = 2
    
    # Plot GDPs
    xlabels = "Time (days)"
    axs[GDP_idx].plot(t, r)
    axs[GDP_idx].plot(t, p)
    axs[GDP_idx].set_title("GDP over time")
    axs[GDP_idx].set_xlabel(xlabels)
    axs[GDP_idx].set_ylabel("GDP")
    
    # Plot innovation
    axs[innovation_idx].plot(t, I_r)
    axs[innovation_idx].plot(t, I_p)
    axs[innovation_idx].set_title("Innovation over time")
    axs[innovation_idx].set_xlabel(xlabels)
    axs[innovation_idx].set_ylabel("Innovation")
    
    # Plot CO2 concentration
    axs[CO2_idx].plot(t, c)
    axs[CO2_idx].set_title(r"CO$_2$ over time")
    axs[CO2_idx].set_xlabel(xlabels)
    axs[CO2_idx].set_ylabel(r"CO$_2$ Concentration")
    
    # Show the plot
    fig.show()
    print()
    

if __name__ == "__main__":
    main()
