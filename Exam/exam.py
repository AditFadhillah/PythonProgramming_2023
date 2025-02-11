import random

# Q1
def is_prime(query_number):
    '''determines wether input is a prime'''
    if query_number < 2:
        return False
    for number in range(2, query_number):
        if query_number % number == 0:
            return False
    return True

def prime_range(lower, upper):
    '''Return range of all prime numbers between lower and upper'''
    numbers = []
    for number in range(lower, upper):
        if is_prime(number):
            numbers.append(number)
    return numbers

def prime_range_one_liner(lower, upper):
    '''Return range of all prime numbers between lower and upper. One-line version of prime_range'''
    return [number for number in range(lower, upper) if is_prime(number)]

import re
cpr_regexp = re.compile(r"([0-9]{2})([0-9]{2})([0-9]{2})-?([0-9]{4})")

def cpr_century(cpr_number_str):
    '''Extract century information from CPR number'''

    match = cpr_regexp.match(cpr_number_str)
    assert match is not None

    DD, MM, YY, IIII = [int(x) for x in match.groups()]

    century = None
    if IIII < 4000:
        century = 1900
    elif IIII < 5000:
        if YY < 37:
            century = 2000
        else:
            century = 1900
    elif IIII < 9000:
        if YY < 58:
            century = 2000
        else:
            century = 1800
    else:
        if YY < 37:
            century = 2000
        else:
            century = 1900

    return century


def calc_column_averages(data_list_of_lists):
    '''Calculate average of list of lists with inner lists of size 2'''
    sums = [0.0, 0.0]
    for row in data_list_of_lists:
        sums[0] += row[0]
        sums[1] += row[1]
    return [sums[0]/len(data_list_of_lists), sums[1]/len(data_list_of_lists)]

def transpose_list_of_lists(data_list_of_lists):
    '''Transpose list of lists with inner lists of size 2'''
    col_lists = [[], []]
    for row in data_list_of_lists:
        col_lists[0].append(row[0])
        col_lists[1].append(row[1])
    return [col_lists[0], col_lists[1]]

def calc_column_averages_pandas(anomaly_df):
    '''calculate mean of all columns in dataframe'''
    return anomaly_df.mean()

def get_positive_anomalies(anomaly_df):
    '''select rows in dataframe which have positive anomalies'''
    return anomaly_df[anomaly_df['Annual Anomaly'] > 0]

def remove_uncertain_anomalies(anomaly_df):
    '''Remove rows where the uncertainty is larger than 10% of the absolute anomaly value'''
    mask = (anomaly_df['Annual Unc.'] / anomaly_df['Annual Anomaly'].abs()) < 0.1
    return anomaly_df[mask]

def set_uncertain_anomalies_to_nan(anomaly_df):
    '''Set rows where uncertainty is larger than 10% of the absolute anomaly value to nan'''
    anomaly_df_new = anomaly_df.copy()
    mask = (anomaly_df['Annual Unc.'] / anomaly_df['Annual Anomaly'].abs()) >= 0.1
    anomaly_df_new['Annual Anomaly'][mask] = float('nan')
    return anomaly_df_new

class Coin:
    '''Coin simulator class'''
    
    def __init__(self, tails_probability=0.5):
        '''Constructor'''
        self.tails_probability = tails_probability

    def toss(self):
        '''Toss a single coin'''
        if random.random() < self.tails_probability:
            return "TAILS"
        else:
            return "HEADS"

    def toss_multiple(self, n_tosses):
        '''Toss multiple coins'''
        result = {"HEADS": 0, "TAILS": 0}
        for i in range(n_tosses):
            result[self.toss()] += 1
        return result
