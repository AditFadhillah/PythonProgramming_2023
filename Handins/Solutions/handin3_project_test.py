import handin3_project

# Q1 Calling read_data2 with and without optional argument
handin3_project.read_data2(filename='Land_and_Ocean_summary.txt')
handin3_project.read_data2(filename='Land_and_Ocean_summary.txt', year_range=(2015, 2018))

# Q2 Calling read_data2 
temp_anomaly_data = handin3_project.read_data3(filename='Land_and_Ocean_summary.txt', year_range=(2015, 2018))
print(temp_anomaly_data)
