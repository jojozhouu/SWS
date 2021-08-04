# the World class

import config as cfg
import copy
import heapq
import math
import numpy as np


class World:
    """
    A class representing a world state. This world state stores all information
    of the countries. It can perform operations such as computing the utility
    and search for schedules.
    """

    def __init__(self):
        """
        Initialize a world

        Accepts:
        1. A list of countries
        2. The user's country index
        3. The current schedule execution depth, i.e. how many operations
        in the schedule has been executed
        4. A list of adjusted contribution score for each country
        """

    def get_expected_utility(self):
        """
        Accepts:
        1. the index of a country for which the expected utility is calculated.
        If the country index is None, calculate the expected utility of the user's
        country.

        Returns:
        1. the expected utility of a country
        """

    def get_adjusted_contribution(self):
        """
        Accepts:
        1. the index of a country for which the expected utility is calculated.

        Returns:
        1. the discounted reward for a country
        """

    def accept(self):
        """
        Execute an operation. Update the resources, adjusted contributions,
        and schedule execution depth.

        Accepts:
        1. the operation (transfer/transform) to be applied to the world.

        Returns:
        1. a boolean that returns true if the operation has succeeded, false
        if otherwise.
        """

    def country_acceptance_probability(self):
        """
        Calculate the acceptance probability of a country

        Accepts:
        1. The country index for which the acceptance probability needs to be calculated

        Returns:
        1. The acceptance probability of the country
        """

    def world_accept_probability(self):
        """
        Calculate the acceptance probability of a country

        Accepts:
        1. None

        Returns:
        1. The probability every country in the current world will accept the
        current schedule
        """

    def to_str(self):
        return None  # placeholder
