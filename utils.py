# misc helper functions

import numpy as np
import os
import pandas as pd


def read_resources():
    """
    Accepts one string parameter:
    1. the file name of the resource file.

    Returns:
    1. an numpy array of numbers that represents the respective weight for each resources.
    """


def read_initial_world():
    """
    Accepts one string parameter:
    1. the file name of the initial states file.

    Returns:
    1. a 2d numpy array that represents the initial state of each country.
    2. a list of country names.
    """


def read_transform_templates():
    """
    Accepts two parameters:
    1. the file name of the input file of the transform templates
    2. the file name of the output file of the transform templates

    Returns:
    1. an array of strings containing the resource names
    2. a list of numpy array of all input templates
    3. a list of numpy array of all output templates
    """


def print_outputs():
    """
    Writes solutions to the given file name.
    Any existing content with the same file name is cleared; all intermediate directories will
    be created if necessary, but it's okay if they're already there.
    Uses the __str__ method of the Solution class.

    @input output_schedule_filename     desired output directory
    @input solutions                    list of solutions
    """
