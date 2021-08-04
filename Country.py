# the Country class and make_countries helper function


class Country:
    def __init__(self):
        """
        Initialize a country

        Accepts:
        1. The country index
        2. The country's initial resource quantity
        3. The country's current resource quantity

        A country object should also has a member variable that represent the quality
        score of the country. This can be initialized using the evaluate() function
        and the resource quantity.
        """

    def evaluate(self):
        """
        Calculate the country's quality score

        Accepts:
        1. None

        Returns:
        1. The current country's quality score (double)
        """

    def operate(self):
        """
        Check if the country has all the resources necessary to complete an
        operation. If not, return false. Otherwise apply the operation on
        the current country and return true.

        Accepts:
        1. An array indicating the net effect of an operation on the country's
        resource

        Returns:
        1. True if the country can complete the operation, false if otherwise.
        """

    def to_str(self):
        return None  # placeholder


def build_country():
    """
    Create a list of country object

    Accepts:
    1. The 2d numpy array read in by the read_initial_world() method in utils.py

    Returns:
    1. A list of countries in the 2d array
    """
