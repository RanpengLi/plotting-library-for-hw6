#!/bin/python

"""This module contains functions to read temperature data and plot geotherm."""

import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt



def read_data_and_transform_to_json (filename, headerline = 2, write_as_json = True, json_name = "geotherm_data.json"):
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

    if write_as_json:
        all_spreadsheet_values.to_json(json_name)

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


def plot_and_save_geotherm (depth,
                            temperature,
                            title = "Geotherm Gradient",
                            m_to_km = True,
                            save_figure = False,
                            figure_name= "Geotherm Gradient"):
    """ Plot geotherm (depth vs temperature)
    5 input are
    depth,
    temperature,
    optional: title = "Geotherm Gradient" (will also be the name of figure),
    optional: m_to_km = True
    optional: ifsave = False
    figure_name = "Geotherm Gradient.png"
    """

    if m_to_km:
        depth = depth/1000

    figure = plt.figure()
    temperature_plot = plt.plot (temperature, depth)
    plt.gca().invert_yaxis()
    plt.title(title)
    plt.ylabel("Depth (km)")
    plt.xlabel("Temperature (K)")
    plt.show()


    if save_figure:
        figure.savefig(figure_name)


def plot():
    """ plot the geotherm"""

    current_file_location = os.path.dirname(__file__)

    data_file = "geotherm_data.csv"

    filename =  os.path.join(current_file_location,
                                            "..",
                                            "data",
                                            data_file)

    path_to_json =  os.path.join(current_file_location,
                                        "..",
                                        "results",
                                        "data_output.json")

    temperature_data, colomn_title = read_data_and_transform_to_json (filename, write_as_json = True, json_name = path_to_json)
    pyr_depth, pyr_temperature = get_depth_and_T (temperature_data)

    plot_title = "Geothermal gradient of a pyrolitic mantle"
    path_to_figure =  os.path.join(current_file_location,
                                            "..",
                                            "results",
                                            plot_title)

    plot_and_save_geotherm( pyr_depth,
                            pyr_temperature,
                            plot_title,
                            save_figure = True,
                            figure_name = path_to_figure )


if __name__ == "__main__":
    plot()
    