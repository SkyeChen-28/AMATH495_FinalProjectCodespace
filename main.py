import os
import numpy as np
import scipy as sp
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt
from src.odes import ClimateODEs

def main():
    # CLI Values
    output_dir = "outputs"
    
    # Initial values
    r = 1
    p = 0.01 # GDP of poorer country relative to rich
    I_r = 1
    I_p = 1
    c = 1
    y0 = np.array([r, p, I_r, I_p, c]) # Model is normalized so that all values are in terms of present day values
    
    # Set system parameter values
    G_r = 3e-3
    G_p = 9e-4
    K_r = 1.1
    K_p = 0.7
    gamma = 1
    alpha = 1
    beta = 1
    climate = ClimateODEs(G_r, G_p, K_r, K_p, gamma, alpha, beta)
    D = 1e-5 # Natural diaster intensity
    f = 3 # Disaster frequency: A diaster happens once every f year(s)
    
    # Define timeframe
    days_per_year = 365
    num_years = 80
    # num_years = 40
    
    # Run model year by year
    t = np.array([0])
    y = y0.reshape((5, 1))
    for year in range(num_years + 1):
        t_begin = year * days_per_year
        t_end = t_begin + days_per_year
        t_span = (t_begin, t_end)
        t_eval = np.linspace(t_begin, t_end, days_per_year + 1)
    
        # Solve the ODE system
        result = solve_ivp(climate.vec_de, t_span, y[:,-1], t_eval=t_eval)

        # Parse results
        t = np.append(t, result.t, axis = 0)
        y = np.append(y, result.y, axis = 1)
        r = y[0]
        p = y[1]
        I_r = y[2]
        I_p = y[3]
        c = y[4]
        
        # Natural Disaster
        if ((year != 0) and (year % f == 0)):
            y[0,-1] -= 0.9 * r[-1] * (1 - np.exp(- D*c[-1] / r[-1])) # Reduces r
            y[1,-1] -= 0.9 * p[-1] * (1 - np.exp(- D*c[-1] / p[-1])) # Reduces p
    
    
    # Plot results
    fig, axs = plt.subplots(3, 1) # Landscape plots
    # fig, axs = plt.subplots(1, 3) # Portrait plots
    
    # Common plot parameters
    x_axis_title = "Time (years)"
    num_ticks = 8
    xticks = np.arange(0, num_years+1, num_years//num_ticks) * days_per_year
    xlabels = np.arange(0, num_years+1, num_years//num_ticks)
    RICH_COUNTRY = "Rich Country"
    POOR_COUNTRY = "Poor Country"
    rich_col = "lime"
    poor_col = "red"
    poor_linestyle = "solid" #"dashed"
    glob_col = "forestgreen"
    
    # Modifications common to all plots
    for ax in axs:
        ax.set_xlabel(x_axis_title)
        ax.set_xticks(xticks, labels = xlabels)
        ax.minorticks_on()
        ax.grid(True, which = 'minor', color = '0.9')
        ax.grid(True, which = 'major', color = 'darkgrey')
        
    # Define indices
    GDP_idx = 0
    innovation_idx = 1
    CO2_idx = 2
    
    # Plot GDPs
    axs[GDP_idx].plot(t, r, label = RICH_COUNTRY, color = rich_col)
    axs[GDP_idx].plot(t, p, label = POOR_COUNTRY, color = poor_col, linestyle = poor_linestyle)
    axs[GDP_idx].set_title("GDP over time")
    axs[GDP_idx].set_ylabel("GDP")
    axs[GDP_idx].set_xlim(0)
    axs[GDP_idx].set_ylim(0)
    
    # Plot innovation
    axs[innovation_idx].plot(t, I_r, label = RICH_COUNTRY, color = rich_col)
    axs[innovation_idx].plot(t, I_p, label = POOR_COUNTRY, color = poor_col, linestyle = poor_linestyle)
    axs[innovation_idx].set_title("Innovation over time")
    axs[innovation_idx].set_ylabel("Innovation")
    axs[innovation_idx].set_xlim(0)
    axs[innovation_idx].set_ylim(0)
    
    # Plot CO2 concentration
    axs[CO2_idx].plot(t, c, label = "Global", color = glob_col)
    axs[CO2_idx].set_title(r"CO$_2$ over time")
    axs[CO2_idx].set_ylabel(r"CO$_2$ Concentration")  
    axs[CO2_idx].set_xlim(0)
    axs[CO2_idx].set_ylim(0)
    
    # More common mods after labels have been added
    for ax in axs:
        ax.legend()
    
    # Show the plot
    if (not os.path.exists(output_dir)):
        os.mkdir(output_dir)
    fig.tight_layout(rect = (0,0,0.95,1), h_pad = -1)
    fig.set_size_inches((8.5, 11), forward = False)
    fig.savefig(f'{output_dir}/plots.png', dpi = 500)
    fig.show()
    print()
    

if __name__ == "__main__":
    main()
