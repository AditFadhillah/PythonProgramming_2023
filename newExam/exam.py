# Python Programming for Data Science

import numpy as np
import pandas as pd
import re

def create_number_string(min, max):
    """Returns a string of numbers from min to max"""
    result = ''
    for num in range(min, max + 1):
        result += str(num) + " "
    return result

def create_hash_string(length):
    """Returns a string of # of specific length"""
    result = ''
    odd = False
    if length % 2 == 1:
        length += 1 
        odd = True 
    half = int(int(length)/2)
    for num in range(half-1):
        result += "#" + "_"
    if odd == True:
        result += "#"
    else:
        result += "#_"
    return result

def generate_concentric_squares(size):
    """Returns a string of concentric squares of # of specific length"""
    if size % 2 == 0:
        raise ValueError("size must be odd")
    arr = np.full((size, size), '#')
    for i in range(1, size, 2):
        arr[i:-i, i] = ' '
        arr[i:-i, -i-1] = ' '
        arr[i, i:-i] = ' '
        arr[-i-1, i:-i] = ' '
    return arr

def create_jazz_regexp():
    """Returns a regular expression that matches jazz musicians data"""
    result = r"[Nn]ame:\s*([A-Z][a-z]+ [A-Z][a-z]+)[.,;]\s*[Aa]ctive:\s*(\d{4})-(\d{4})[.]\s*[Ii]nstrument:\s*([a-z]+)"
    return result

def parse_jazz_data(regexp, text):
    """Returns a list of tuples of jazz musicians data"""
    result = []
    for line in text.splitlines():
        match = re.match(regexp, line)
        if match:
            result.append(match.groups())
    return result

def parse_jazz_data_sorted(regexp, text):
    """Returns a list of tuples of jazz musicians data 
    sorted by how many years they were active"""
    result = parse_jazz_data(regexp, text)
    result.sort(key=lambda x: int(x[2]) - int(x[1]), reverse=True)
    return result

def read_data(data_filename):
    """Open file and read its content into a list of strings, 
    ignoring all comment lines"""
    result = []
    with open(data_filename) as file:
        for line in file:
            if not line.startswith("#"):
                result.append(line.strip())
    return result

def read_data2(data_filename):
    """Open file and iterate over the lines, 
    using dictionary"""
    result = []
    with open(data_filename) as file:
        for line in file:
            if line.startswith("#"):
                continue
            elif line.startswith("date,temp,status"):
                header = line.strip().split(",")
                continue
            else:
                data = line.strip().split(",")
                date = data[0].split("-")
                result.append({header[0]:(int(date[0]), int(date[1]), int(date[2])), header[1]:float(data[1]), header[2]:data[2]})
    return result

def read_data3(data_filename):
    """Open file and iterate over the lines, 
    store the data into a dictionary of 
    dictionaries of dictionaries"""
    result = {}
    with open(data_filename) as file:
        for line in file:
            if line.startswith("#"):
                continue
            elif line.startswith("date,temp,status"):
                header = line.strip().split(",")
                continue
            else:
                data = line.strip().split(",")
                date = data[0].split("-")
                if int(date[0]) not in result:
                    result[int(date[0])] = {}
                if int(date[1]) not in result[int(date[0])]:
                    result[int(date[0])][int(date[1])] = {}
                result[int(date[0])][int(date[1])][int(date[2])] = float(data[1]), data[2]
    return result
    
def read_data_pandas(data_filename):
    """Read the file, and return it as a pandas dataframe"""
    df = pd.read_csv(data_filename, comment="#")
    return df

def count_entries_per_year(data_df):
    """Use pandas groupby to group entries by the year values"""
    result = data_df.groupby(data_df["date"].str[:4]).count()
    return result["temp"]

def create_pivot_table(data_df):
    """Retuns a pivot table of temperature values for each year, index by dates"""
    result = []
    for year, df in data_df.groupby(data_df["date"].str[:4]):
        df = df.copy()
        df["date"] = df["date"].str[5:]
        df.rename(columns={"temp":year}, inplace=True)
        df.drop(columns=["status"], inplace=True)
        df.set_index("date", inplace=True)
        if len(df) == 365:
            df.loc["02-29"] = np.nan
        result.append(df)
    result = pd.concat(result, axis=1)
    return result


def plot_temperatures(pivoted_df): 
    """Plot temperature values for each year in dataframe""" 
    # Importing here in function to make function self-contained 
    import matplotlib 
    import matplotlib.pyplot as plt 
    
    # Ensure that dates and years are sorted correctly 
    pivoted_df.sort_index(axis='index', inplace=True) 
    pivoted_df.sort_index(axis='columns', inplace=True) 

    # Initialize plot 
    fig, ax = plt.subplots(figsize=(12, 4)) 

    # Setup line colors 
    years = pivoted_df.columns 
    norm = matplotlib.colors.Normalize(vmin=0, vmax=len(years)) 
    matplotlib.cm.OrRd(norm(1)) 
    colors = [matplotlib.cm.Greys(norm(idx)) for idx in range(len(pivoted_df.columns)-1)] + ['red'] 
    lw = [1] * (len(colors)-1) + [3] 
    from cycler import cycler 
    ax.set_prop_cycle(cycler(color=colors, lw=lw)) 
    
    # Create plot 
    pivoted_df.plot(ax=ax) 

    # Set tick marks to Month values 
    labels = pivoted_df.reset_index()['date'][pivoted_df.reset_index()['date'].str[3:] == '01'] 
    ax.set_xticks(labels.index, ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']) 
    ax.set_ylabel("temperature") 

    # create legend 
    box = ax.get_position() 
    ax.set_position([box.x0, box.y0, box.width * 0.8, box.height]) 
    # Put the legend to the right of the current axis 
    ax.legend(loc='center left', bbox_to_anchor=(1, 0.5), ncol=6) 
    
    fig.show()



