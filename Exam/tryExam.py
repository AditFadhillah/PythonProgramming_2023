import re

def is_prime(query_number):
    if query_number <= 1:
        return False
    for i in range(2, query_number):
        if query_number % i == 0:
            return False
    return True

def prime_range(lower, upper):
    primes = []
    for num in range(lower, upper):
        if is_prime(num):
            primes.append(num)
    return primes

def prime_range_one_liner(lower, upper):
    """Returns a list of prime numbers between lower and upper (exclusive)"""
    return [num for num in range(lower, upper) if is_prime(num)]

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
    column1_sum = 0.0
    column2_sum = 0
    for row in data_list_of_lists:
        column1_sum += row[0]
        column2_sum += row[1]
    column1_avg = column1_sum / len(data_list_of_lists)
    column2_avg = column2_sum / len(data_list_of_lists)
    return [column1_avg, column2_avg]

def transpose_list_of_lists(data_list_of_lists):
    num_rows = len(data_list_of_lists)
    num_cols = len(data_list_of_lists[0])
    transposed = []
    for j in range(num_cols):
        new_row = []
        for i in range(num_rows):
            new_row.append(data_list_of_lists[i][j])
        transposed.append(new_row)
    return transposed

