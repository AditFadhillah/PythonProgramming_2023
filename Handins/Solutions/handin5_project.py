"""Handin 5 - Project part"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib


def construct_rectangles(years, anomalies, bottom=0.0, height=1.0):
    """
    Construct a list of (year, bottom_coordinate, width, height, value) objects
    """
    
    rectangles = []
    for i in range(len(years)):
        year = years[i]
        anomaly = anomalies[i]
        rectangles.append((year, bottom, 1, height, anomaly))

    # Or:
    for year, anomaly in zip(years, anomalies):
        rectangles.append((year, bottom, 1, height, anomaly))

    return rectangles

class ColorMapper:
    """
    Wrapper class for matplotlib cmap that maps a range of values to 
    a [0,1] range, such that values can be mapped to colors.
    """

    def __init__(self, values, cmap_str='RdBu_r'):
        """
        Constructor. Extracts min and max values from a numpy array of values, and uses 
        this to determine how to map values to colors.
    
        :param values: Numpy array of float values
        :param cmap_str: String argument for color map, which will be sent to matplotlib.
        """

        # Save attributes
        self.cmap = plt.get_cmap(cmap_str)

        self.min_value = np.min(values)
        self.max_value = np.max(values)                        

        self.max_value = max(abs(self.min_value), abs(self.max_value))
        self.min_value = -self.max_value

    def get_color(self, value):
        """
        Retrieve color corresponding to a particular value.
        """
        return self.cmap((value - self.min_value) / (self.max_value - self.min_value))

    
def plot_stripes(list_of_rectangles,
                 color_mapper,
                 colorbar=True,
                 figure_width=20, figure_height=5):
    """
    Visualize list of rectangles, where each rectangle is specified in the format
    (x-coordinate, y-coordinate, width, height, value). The color_mapper is
    used to look up colors corresponding to the values provided for each rectangle.

    :param list_of_rectangles: List of (x-coordinate, y-coordinate, width, height, value) tuples
    :param color_mapper: ColorMapper object used to lookup values for each block
    :param colorbar: Whether to include a color bar
    :param figure_width: Width of figure
    :param figure_height: Height of figure
    :return: None
    """

    _, ax = plt.subplots(1, figsize=(figure_width, figure_height))
    x_values = []
    y_values = []
    for rectangle in list_of_rectangles:

        anomaly_value = rectangle[-1]

        rect = matplotlib.patches.Rectangle(rectangle[:2], rectangle[2], rectangle[3],
                                            linewidth=1, edgecolor='none',
                                            facecolor=color_mapper.get_color(anomaly_value))
        ax.add_patch(rect)
        x_values += [rectangle[0], rectangle[0]+rectangle[2]]
        y_values += [rectangle[1], rectangle[1]+rectangle[3]]

    ax.set_xlim(min(x_values), max(x_values))
    ax.set_ylim(min(y_values), max(y_values))

    if colorbar:
        from mpl_toolkits.axes_grid1 import make_axes_locatable
        divider = make_axes_locatable(plt.gca())
        ax_cb = divider.new_horizontal(size="1%", pad=0.1)
        matplotlib.colorbar.ColorbarBase(ax_cb, cmap=color_mapper.cmap,
                                         orientation='vertical',
                                         norm=matplotlib.colors.Normalize(
                                             vmin=color_mapper.min_value,
                                             vmax=color_mapper.max_value))
    plt.gcf().add_axes(ax_cb)
    plt.show()





