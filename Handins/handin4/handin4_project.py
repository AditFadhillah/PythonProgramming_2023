"""
handin4_project.py


AnomalyData class for reading and processing data from a file
It can filter data by years and extract values for the first year of each decade
module also includes data processing functions used by the class


Classes:
- AnomalyData

Functions:
- read_data(filename, year_range=None)
- one_value_per_decade()

"""

class AnomalyData:
    """
    AnomalyData class for reading and processing data from a file

    Args:
    filename (str): name of file
    year_range (tuple of two numbers, optional): range of years

    Attributes:
    data (dict): dictionary with data values for each year in specified range
    keys are years, and values are lists of data

    """

    def __init__(self, filename, year_range=None):
        """
        Initialize AnomalyData object with data from a file

        """
        self.data = self.read_data(filename, year_range)

    def read_data(self, filename, year_range=None):
        """
        Read data from a file, filter by years, and return as a dictionary

        Args:
        filename (str): name of file
        year_range (tuple of two numbers, optional): range of years

        Returns:
        data_dict: dictionary where keys are years and values are lists of data

        """
        file = open(filename, "r")
        data_dict = {}

        for line in file:
            line = line.strip()
            if not line or line.startswith("%"):
                continue

            year_str, *data_values = line.split()
            year = int(year_str)

            if year_range is None or (year_range[0] <= year < year_range[1]):
                data_list = []
                for val in data_values:
                    if val != "NaN":
                        data_list.append(float(val))
                    else:
                        data_list.append(float("nan"))
                data_dict[year] = data_list

        file.close()
        # return dictionary
        return data_dict
    
    def one_value_per_decade(self):
        """
        Create dictionary with one value per decade from the data attribute

        Returns:
        decade_dict: dictionary with one value per decade, keys are years and
        values are lists of data

        """
        decade_dict = {}
        
        for year in self.data.keys():
            # check if the year is a multiple of 10
            if year % 10 == 0:  
                decade_dict[year] = self.data[year]
        
        # return dictionary
        return decade_dict
