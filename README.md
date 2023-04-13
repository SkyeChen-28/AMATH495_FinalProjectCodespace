# AMATH 495 Final Project

A repository for all code used for my AMATH 495 Final Project

## Dependencies

Use the command below to install program dependencies:

```{bash}
pip install -r requirements.txt
```

## Usage

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
