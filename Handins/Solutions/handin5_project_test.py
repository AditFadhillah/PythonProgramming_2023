import handin5_project
import numpy as np

# Q1
anomaly_data = np.genfromtxt('Land_and_Ocean_summary.txt', comments='%')
print(anomaly_data)

# Q2
color_mapper = handin5_project.ColorMapper(anomaly_data[:,1])
print(color_mapper.get_color(0.))

# Q3
rectangles = handin5_project.construct_rectangles(years=anomaly_data[:,0], anomalies=anomaly_data[:,1])
handin5_project.plot_stripes(rectangles, color_mapper)


