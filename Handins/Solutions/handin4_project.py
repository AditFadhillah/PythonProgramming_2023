

class AnomalyData:
    """Class for managing temperature anomaly data"""
    
    def __init__(self, filename, year_range=(float("-inf"), float("inf"))):
        """Constructor"""

        self.data = {}
        
        file_handle = open(filename)

        # Note: we can iterate directly over a file object
        for line in file_handle:

            # Overwriting line with stripped version
            # (we don't need original)
            line = line.strip()

            if len(line) == 0 or line[0] == '%':
                continue

            # Split string into list of strings
            line_split = line.split()

            year = int(line_split[0])

            # Convert list of strings to a list of floats
            line_split_numbers = []
            for entry in line_split[1:]:   # Note: skipping year value
                line_split_numbers.append(float(entry))

            if year >= year_range[0] and year < year_range[1]:
                self.data[year] = line_split_numbers

        file_handle.close()


    def one_value_per_decade(self):
        """Filter data so that only one entry per decade is retrained"""
        
        one_value_dict = {}
        for year in self.data:

            # Check whether year is a "round" value
            if year % 10 == 0:
                # If so, add entry to new dictionary
                one_value_dict[year] = self.data[year]
                
        return one_value_dict

                
