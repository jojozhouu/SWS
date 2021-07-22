# the Operation class

import copy
import numpy as np


class Operation:
    """
    A single operation to be done on a world state.
    """
    def __init__(self):
        """
        Constructor

        Accept:
        1. Index of country initiating the operation
        2. Index of country accepting the operation
        3. Resource changes to the initiating country
        4. Resource changes to the accepting country
        5. Template index
        6. Template multiplier
        """

    def action(self):
        """
        Apply changes to the world according to the operation.
        You should avoid changing the input parameter directly
        and use copy.deepcopy() to create a deep copy of the
        input world object instead. The world object contains
        a method called implement(), which accept an operation,
        implement the operation onto the world object, and
        returns a boolean indicating if the operation is
        carried out successfully. You will need to use the
        implement() method here.

        Accept:
        1. A world object of type World

        Return:
        1. A boolean indicating if the changes is successfully
        applied to the world
        2. A new world object with the changes applied
        """

    def to_str(self):
        """

        """
