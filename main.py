import os
import json
import numpy as np
import scipy as sp
from scipy.integrate import solve_ivp
from src.odes import ClimateODEs
from src.plotting import single_plot, all_plots
from src.constants import DAYS_PER_YEAR

def json_to_dict(filepath: str) -> dict:
    with open(filepath) as fp:
        data = json.load(fp)
    return data

def check_ICs(filepath: str) -> tuple:
    
    # Load in the json file
    ICs_dict = json_to_dict(filepath)
    
    # Extract the variables
    r = ICs_dict["r"]
    p = ICs_dict["p"]
    c = ICs_dict["c"]
    
    # Enforce variable conditions
    assert r > 0, f"r = {r}: GDP (r) should be a strictly positive float. Please change the value of `r` in \"{filepath}\" such that r > 0"
    assert p > 0, f"p = {p}: GDP (p) should be a strictly positive. Please change the value of `p` in \"{filepath}\" such that p > 0"
    assert c >= 0, f"c = {c}: CO2 concentration (c) should be a non-negative float. Please change the value of `c` in \"{filepath}\" such that c >= 0"
    
    return r, p, c

def check_params(filepath: str) -> tuple:
    
    # Load in the json file
    params_dict = json_to_dict(filepath)
    
    # Extract the variables
    G_r = params_dict["G_r"]
    G_p = params_dict["G_p"]
    K_r = params_dict["K_r"]
    K_p = params_dict["K_p"]
    gamma = params_dict["gamma"]
    alpha = params_dict["alpha"]
    beta = params_dict["beta"]
    D = params_dict["D"] # Natural diaster intensity
    f = params_dict["f"] # Disaster frequency: A diaster happens once every f year(s)
    
    # Enforce variable conditions
    assert K_r > 0, f"K_r = {K_r}: Carrying capacity (K_r) should be a strictly positive float. Please change the value of `K_r` in \"{filepath}\" such that `K_r` > 0"
    assert K_p > 0, f"K_p = {K_p}: Carrying capacity (K_p) should be a strictly positive float. Please change the value of `K_p` in \"{filepath}\" such that `K_p` > 0"
    assert gamma > 0, f"gamma = {gamma}: CO2 Emission rate (gamma) should be a strictly positive float. Please change the value of `gamma` in \"{filepath}\" such that `gamma` > 0"
    assert alpha > 0, f"alpha = {alpha}: CO2 Emission efficiency (alpha) should be a strictly positive float. Please change the value of `alpha` in \"{filepath}\" such that `alpha` > 0"
    assert beta > 0, f"beta = {beta}: CO2 Emission rate (beta) should be a strictly positive float. Please change the value of `beta` in \"{filepath}\" such that `beta` > 0"
    
    return G_r, G_p, K_r, K_p, gamma, alpha, beta, D, f
       

def run_model(output_dir: str, ICs_filepath: str, params_filepath: str, num_years: int) -> None:
        
    # Load in initial values
    r, p, c = check_ICs(ICs_filepath)
    I_r = r
    I_p = p
    y0 = np.array([r, p, I_r, I_p, c]) # Model is normalized so that all values are in terms of present day values
    
    # Load in system parameter values
    G_r, G_p, K_r, K_p, gamma, alpha, beta, D, f = check_params(params_filepath)
    climate = ClimateODEs(G_r, G_p, K_r, K_p, gamma, alpha, beta, D, f)
    
    # Run model year by year
    t = np.array([0])
    y = y0.reshape((5, 1))
    for year in range(num_years + 1):
        t_begin = year * DAYS_PER_YEAR
        t_end = t_begin + DAYS_PER_YEAR
        t_span = (t_begin, t_end)
        t_eval = np.linspace(t_begin, t_end, DAYS_PER_YEAR + 1)
    
        # Solve the ODE system
        result = solve_ivp(climate.vec_de, t_span, y[:,-1], t_eval=t_eval)

        # Parse results
        t = np.append(t, result.t[1:], axis = 0)
        y = np.append(y, result.y[:,1:], axis = 1)
        r = y[0]
        p = y[1]
        I_r = y[2]
        I_p = y[3]
        c = y[4]
        
        # Natural Disaster
        y[0,-1] -= climate.natural_disaster(year, f, r[-1], c[-1]) # Reduces r
        y[1,-1] -= climate.natural_disaster(year, f, p[-1], c[-1]) # Reduces p
        
    single_plot(t, r, 
                output_dir = output_dir,
                filename = "Rich_GDP.png",
                num_years = num_years,
                plt_title = "GDP of richer country over time", 
                y_axis_title = "GDP relative to initial", 
                xlims = 0, 
                ylims = None
                )
    single_plot(t, p, 
                output_dir = output_dir,
                filename = "Poor_GDP.png",
                num_years = num_years,
                plt_title = "GDP of poorer country over time", 
                y_axis_title = "GDP relative to richer's initial GDP", 
                xlims = 0, 
                ylims = 0,
                )
    single_plot(t, I_r, 
                output_dir = output_dir,
                filename = "Rich_Inno.png",
                num_years = num_years,
                plt_title = "Innovation of richer country over time", 
                y_axis_title = "Innovation", 
                xlims = 0, 
                ylims = I_r[0]
                )
    single_plot(t, I_p, 
                output_dir = output_dir,
                filename = "Poor_Inno.png",
                num_years = num_years,
                plt_title = "Innovation of poorer country over time", 
                y_axis_title = "Innovation", 
                xlims = 0, 
                ylims = I_p[0]
                )
    single_plot(t, c, 
                output_dir = output_dir,
                filename = "CO2.png",
                num_years = num_years,
                plt_title = r"CO$_2$ over time", 
                y_axis_title = r"CO$_2$ Concentration", 
                xlims = 0, 
                ylims = 0
                )
    all_plots(t, y, num_years, output_dir)
    

def main():
    # CLI Values
    output_dir = "outputs"
    ICs_filepath = "params/initial_conditions.json"
    params_filepath = "params/ODE_params.json"
    
    # Define timeframe
    # num_years = 80
    num_years = 40
    
    run_model(output_dir = output_dir, 
              ICs_filepath = ICs_filepath, 
              params_filepath = params_filepath, 
              num_years = num_years)

if __name__ == "__main__":
    main()
