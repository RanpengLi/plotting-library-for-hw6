
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# read in data
all_spreadsheet_values = pd.read_csv("data/geotherm_data.csv", delimiter=',', header = 1)

def get_depth_and_T (data, depth_col = 1, T_col = 2):
    """ get the temperature colomn and depth colomn from a depth_average.txt outputfile.
     The 3 inputs are data (colomn number (in normal way), the ouput are two seperate data array """

    data = np.array(data, dtype=float)

    depth = data[:,(depth_col-1)]  # in m
    temperature = data[:,(T_col-1)]

    return depth, temperature


all_data = np.array(all_spreadsheet_values)
temperature_data = np.array(all_data[2:,:], dtype=float)
title = np.array(all_data[:2,:])
# depth = temperature_data[:,0] / 1000 # in km
# temperature = temperature_data[:,1]

depth, temperature = get_depth_and_T (temperature_data, 1, 2)

print (temperature.dtype, temperature)

# plotting the geotherm
temperature_figure = plt.figure()

temperature_plot = plt.plot (temperature, depth)
plt.gca().invert_yaxis()
plt.title("Geothermal gradient of a pyrolite mantle model")
plt.ylabel("Depth (km)")
plt.xlabel("Temperature (K)")

# save figure
temperature_figure.savefig('results/figure.png')

# convert to json format and save as a seperate file
all_spreadsheet_values.to_json("results/data_output_RL.json")
