import sys
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# read in data

def read_data_and_transform_to_json (filename, headerline = 2, if_to_json = True):
    """ read in the data file, generate a data array and a title array
    3 inputs are:
    filename
    optional: headerline = 2 (counts in normal way)
    optional: if_to_json = True
    It returns, a data array and a title array """

    all_spreadsheet_values = pd.read_csv(filename, delimiter=',', header = (headerline-1))
    all_data = np.array(all_spreadsheet_values)
    output_data = np.array(all_data[headerline:,:], dtype=float)
    title = np.array(all_data[:headerline,:])

    if if_to_json:
        all_spreadsheet_values.to_json("results/data_output.json")

    return  output_data, title



def get_depth_and_T (data, depth_col = 1, T_col = 2):
    """ get the temperature colomn and depth colomn from a depth_average.txt outputfile.
     The 3 inputs are:
     data, 
     optional: colomn number (in normal way) of depth, default = 1 ,
     optional: colomn number (in normal way) of T, default =2
     The ouput are two seperate data array: depth, temperature """

    data = np.array(data, dtype=float)

    depth = data[:,(depth_col-1)]  # in m
    temperature = data[:,(T_col-1)]

    return depth, temperature



# depth = temperature_data[:,0] / 1000 # in km
# temperature = temperature_data[:,1]



# print (temperature.dtype, temperature)

# plotting the geotherm

def plot_and_save_geotherm(depth, temperature, title, m_to_km = True, ifsave = False):
    """ Plot geotherm (depth vs temperature)
    5 input are 
    depth, 
    temperature, 
    title (will also be the name of figure)
    optional: m_to_km = True
    optional: ifsave = False """

    if m_to_km:
        depth = depth/1000
   
    figure = plt.figure()
    temperature_plot = plt.plot (temperature, depth)
    plt.gca().invert_yaxis()
    plt.title(title)
    plt.ylabel("Depth (km)")
    plt.xlabel("Temperature (K)")
    plt.show()
   
   
    current_file_location = os.path.dirname(__file__)


    figure_name =  os.path.join(current_file_location,
                                        "..",
                                        "results",
                                        title)

    if ifsave:
        figure.savefig(figure_name)


filename = "data/geotherm_data.csv"
temperature_data, colomn_title = read_data_and_transform_to_json (filename, if_to_json = True)
pyr_depth, pyr_temperature = get_depth_and_T (temperature_data)
plot_title = "Geothermal gradient of a pyrolitic mantle"
plot_and_save_geotherm(pyr_depth, pyr_temperature, plot_title, ifsave = True )


# convert to json format and save as a seperate file

