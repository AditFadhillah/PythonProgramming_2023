from handin4_project import AnomalyData
from handin4_project import AnomalyData

# create an instance of AnomalyData without specifying a year range
anomaly_data = AnomalyData('Land_and_Ocean_summary.txt')

# access and print specific value from the data
value = anomaly_data.data[1990][0]

print(f"Value for the year 1990: {value}")

# call the one_value_per_decade method to extract data for one value per decade
decade_dict = anomaly_data.one_value_per_decade()

print("One Value Per Decade:")
print(decade_dict)
