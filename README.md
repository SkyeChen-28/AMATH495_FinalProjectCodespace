# AMATH 495 Final Project

A repository for all code used for my AMATH 495 Final Project. [Final project deliverable document](https://github.com/SkyeChen-28/AMATH495_FinalProjectCodespace/blob/main/AMATH_495___Final_Project_Deliverable.pdf)

## Summary of Model

This is a "toy model" of the global economy and how it is affected by, and affects the global climate system. The model assumes only two countries exist, a rich developed nation, and a developing nation. Both nations GDP's are modelled using a logistics curve where the developed economy will have an initial condition closer to it’s carrying capacity allowing it to grow approximately linearly, and the developing economy will have an initial condition significantly less than it’s carrying capacity allowing it to grow exponentially. The developed economy starts with a GDP much larger than the developing economy. Both countries emit CO2 proportional to their current GDP.
Once a year, a global natural disaster happens and it reduces the GDP of both countries. The impact to GDP is inversely propotional to the current GDP of each country, and proportional to the current total amount of CO2 in the atmosphere.
The model will produce plots on how CO2 levels change over time as well as how the GDP of each country changes over time.

## Running the Program

### Dependencies

Use the command below to install program dependencies:

```{bash}
pip install -r requirements.txt
```

### Usage

The program will use default arguments if you simply run

```{bash}
python main.py
```

You can specify arguments for the program to take in as input

```{bash}
python main.py -o ./outputs -i ./params/initial_conditions.json -p ./params/ODE_params.json -n 40
```

Use this command

```{bash}
python main.py --help
```

To display this help message:

```{bash}
usage: main.py [-h] [-o OUTPUT_DIR] [-i ICS_FILEPATH] [-p PARAMS_FILEPATH] [-n NUM_YEARS]

options:
  -h, --help            show this help message and exit
  -o OUTPUT_DIR,        --output-dir OUTPUT_DIR
                        [str] The directory to store all program outputs to (default: ./outputs)
  -i ICS_FILEPATH,      --ICs-filepath ICS_FILEPATH
                        [str] The filepath to the initial conditions json file (default: ./params/initial_conditions.json)
  -p PARAMS_FILEPATH,   --params-filepath PARAMS_FILEPATH
                        [str] The filepath to the ODE system parameters json file (default: ./params/ODE_params.json)
  -n NUM_YEARS,         --num-years NUM_YEARS
                        The number of years to run the simulation for (default: 40)
```
