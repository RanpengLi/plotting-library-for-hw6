
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# read in data
all_spreadsheet_values = pd.read_csv("data/geotherm_data.csv", delimiter=',', header = 1)

all_data = np.array(all_spreadsheet_values)
temperature_data = np.array(all_data[2:,:], dtype=float)
title = np.array(all_data[:2,:])
depth = temperature_data[:,0] / 1000 # in km
temperature = temperature_data[:,1]

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
