import numpy as np
import matplotlib.pyplot as plt
import os
from src.constants import X_AXIS_TITLE, DAYS_PER_YEAR

def single_plot(t, y, output_dir, filename, num_years, plt_title, y_axis_title, xlims, ylims, num_ticks = 8, DPI_VAL = 500, **kwargs):

    # Common plot parameters
    xticks = np.arange(0, num_years+1, num_years//num_ticks) * DAYS_PER_YEAR
    xlabels = np.arange(0, num_years+1, num_years//num_ticks)
    
    # Plot
    plt.plot(t, y, **kwargs)
    plt.title(plt_title)
    plt.xlabel(X_AXIS_TITLE)
    plt.ylabel(y_axis_title)
    plt.xticks(xticks, labels = xlabels)
    plt.xlim(xlims)
    plt.ylim(ylims)
    plt.minorticks_on()
    plt.grid(True, which = 'minor', color = '0.9')
    plt.grid(True, which = 'major', color = 'darkgrey')
    
    # Save plot
    plt.savefig(f'{output_dir}/{filename}', dpi = DPI_VAL)
    plt.close()
    
    # # Show plot
    # plt.show()
    # print()
    
def all_plots(t, y, num_years, output_dir, num_ticks = 8, DPI_VAL = 500):
    
    # Common plot parameters
    xticks = np.arange(0, num_years+1, num_years//num_ticks) * DAYS_PER_YEAR
    xlabels = np.arange(0, num_years+1, num_years//num_ticks)
    RICH_COUNTRY = "Rich Country"
    POOR_COUNTRY = "Poor Country"
    rich_col = "lime"
    poor_col = "red"
    poor_linestyle = "solid" #"dashed"
    glob_col = "forestgreen"
    
    # Extract dependent variables
    r = y[0]
    p = y[1]
    I_r = y[2]
    I_p = y[3]
    c = y[4]
    
    # Plot all results
    fig, axs = plt.subplots(3, 1) # Landscape plots
    
    # Modifications common to all plots
    for ax in axs:
        ax.set_xlabel(X_AXIS_TITLE)
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
    fig.savefig(f'{output_dir}/all_plots.png', dpi = DPI_VAL)
    # fig.show()
    # print()