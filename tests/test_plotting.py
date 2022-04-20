#!/bin/python

""" test the plotting script"""

import sys
import os

import numpy as np
#import matplotlib.pyplot as plt
#import pandas as pd

sys.path.append(os.path.join(
    os.path.dirname(__file__), ".."))

from src import plotting

def test_plot():
    """ check if plotting script run"""
    plotting.plot()

def test_read_data():
    """ test read_data_and_transform_to_json() to make sure the output has correct size"""
    current_file_location = os.path.dirname(__file__)
    data_directory = os.path.join(current_file_location,
                                    "..",
                                    "data")

    input_data_filename = os.path.join(data_directory,
                                    "geotherm_data.csv")

    test_data, test_colomn_title = plotting.read_data_and_transform_to_json(input_data_filename)

    assert test_data.shape == (55,2), \
        'unexpected size of array, array size:' + str(test_data.shape)

def test_get_depth_and_T():
    """ test if the get_depth_and_T() function output the right data colomn"""

    test_input_data = np.array([[1,2,3],[1,2,3],[1,2,3]])
    test_depth, test_T = plotting.get_depth_and_T(test_input_data, depth_col = 1, T_col = 3)
    expect_output = np.array([3,3,3])

    assert np.all(test_T == expect_output), \
        "Wrong output colomn"


def test_plot_and_save_geotherm():
    """This test runs the plot_and_save_geotherm() function and makes
    sure it creates and save a figure."""
    current_file_location = os.path.dirname(__file__)
    results_directory = os.path.join(current_file_location,
                                        "..",
                                        "results")

    test_title = "Geothermal gradient of a pyrolitic mantle.png"
    plot_filename = os.path.join(results_directory,
                                test_title)

    if os.path.exists(plot_filename):
        os.remove(plot_filename)


    plotting.plot_and_save_geotherm(np.array([1,2,3]), np.array([1,2,3]), test_title,
                                    save_figure = True, figure_name = plot_filename)

    assert os.path.exists(plot_filename)
