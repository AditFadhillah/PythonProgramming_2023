# Python Programming for Data Science

import exam

# Q1
print("Q1.a")
print(exam.create_number_string(3,13))

print("\nQ1.b")
print(exam.create_hash_string(13))
print(exam.create_hash_string(12))

print("\nQ1.c")
print(exam.generate_concentric_squares(3))
print(exam.generate_concentric_squares(7))
print(exam.generate_concentric_squares(9))
print(exam.generate_concentric_squares(13))

# Q2
print("\nQ2.a")
jazz_musicians_data = """Name: Lester Young, Active:1933-1959. Instrument: saxophone
name: Dizzy Gillespie, active: 1935-1993. Instrument:trumpet
name: Billie Holiday, Active: 1930-1959. Instrument: vocalist
Name: Dexter Gordon. Active: 1940-1986. Instrument: saxophone
name: Duke Ellington; active: 1914-1974. instrument: piano
name: Oscar Peterson.Active:1945-2007.Instrument: piano
"""
jazz_regexp = exam.create_jazz_regexp()

print("\nQ2.b")
print(exam.parse_jazz_data(jazz_regexp, jazz_musicians_data))

print("\nQ2.c")
print(exam.parse_jazz_data_sorted(jazz_regexp, jazz_musicians_data))

# Q3
print("\nQ3.a")
temp_data1 = exam.read_data("era5_daily_global_sfc_temp_1940-2023.csv")
print(temp_data1[:5])

print("\nQ3.b")
temp_data2 = exam.read_data2("era5_daily_global_sfc_temp_1940-2023.csv")
print(temp_data2[:5])

print("\nQ3.c")
temp_data3 = exam.read_data3("era5_daily_global_sfc_temp_1940-2023.csv")
# Works fine but its too long to show on the terminal
# print(temp_data3)

# Q4
print("\nQ4.a")
data_df = exam.read_data_pandas("era5_daily_global_sfc_temp_1940-2023.csv")
print(data_df)

print("\nQ4.b")
print(exam.count_entries_per_year(data_df))

print("\nQ4.c")
pivoted_df = exam.create_pivot_table(data_df)
print(pivoted_df)

exam.plot_temperatures(pivoted_df)