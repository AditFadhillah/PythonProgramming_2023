from handin3_project import read_data2
from handin3_project import read_data3

""" # test read data for all years
data_all_years = read_data2("Land_and_Ocean_summary.txt")
print("Data for all years:")
for line in data_all_years:
    print(line) """

# test read data for specific year range
year_range = (2000, 2010)
data_range = read_data2("Land_and_Ocean_summary.txt", year_range)
print("\nData for the specified year range (2000-2010):")
for line in data_range: 
    print(line)


# test accesing data from specific year
year_range = (2015, 2018)
temp_anomaly_data = read_data3("Land_and_Ocean_summary.txt", year_range)
value_2015 = temp_anomaly_data[2015][0]
value_2016 = temp_anomaly_data[2016][0]
value_2017 = temp_anomaly_data[2017][0]

print(f"Temperature anomaly for 2015: {value_2015}")
print(f"Temperature anomaly for 2016: {value_2016}")
print(f"Temperature anomaly for 2017: {value_2017}")
