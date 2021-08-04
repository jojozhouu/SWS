# misc helper functions

import numpy as np
import os
import pandas as pd


def read_resources(filename):
    """
    Accepts one string parameter:
    1. the file name of the resource file.

    Returns:
    1. an numpy array of numbers that represents the respective weight for each resources.
    """
    os.chdir("D:\桌面\SeeU\Python Project课\Github Repo\SWS\inputs")
    file = pd.read_excel(filename)
    resource_weight = np.array(file["Weight"])
    return resource_weight

def read_initial_world(filename):
    """
    Accepts one string parameter:
    1. the file name of the initial states file.

    Returns:
    1. a 2d numpy array that represents the initial state of each country.
    2. a list of country names.
    """
    os.chdir("D:\桌面\SeeU\Python Project课\Github Repo\SWS\inputs")
    file = pd.read_excel("Initial-Countries-Default.xlsx")
    initial_res = np.array(file)
    country = list(file["Country"])
    return initial_res, country

def read_transform_templates(input_filename, output_filename):
    """
    Accepts two parameters:
    1. the file name of the input file of the transform templates
    2. the file name of the output file of the transform templates

    Returns:
    1. an array of strings containing the resource names
    2. a list of numpy array of all input templates
    3. a list of numpy array of all output templates
    """
    os.chdir("D:\桌面\SeeU\Python Project课\Github Repo\SWS\inputs")
    input_file = pd.read_excel("Production-Templates-Input.xlsx",header=0)
    output_file = pd.read_excel("Production-Templates-Output.xlsx",header=1)
    resources = np.array(input_file.columns[1:],dtype=str)
    input_temp = list(input_file.values)
    output_temp = list(output_file.values)
    return resources, input_temp, output_temp
    
    
    
    
    
    
    