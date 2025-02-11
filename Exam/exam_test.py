import exam

# Q1.a
print("\nQ1.a")
check_prime1 = exam.is_prime(10)
check_prime2 = exam.is_prime(11)
print(check_prime1, check_prime2)

# Q1.b
print("\nQ1.b")
primes1 = exam.prime_range(0, 42)
print(primes1)

# Q1.c
print("\nQ1.c")
primes2 = exam.prime_range_one_liner(0, 42)
print(primes2)

# Q2.a
print("\nQ2.a")
print(exam.cpr_regexp.match("123456-7890"))

# Q2.b
print("\nQ2.b")
century = exam.cpr_century("111111-1118")
print(century)

# Q3.a
print("\nQ3.a")
import random
data = [ [random.random() for j in range(2)] for i in range(20) ]
print(data)
columns_averages = exam.calc_column_averages(data)
print(columns_averages)

# Q3.b
print("\nQ3.b")
data_transposed = exam.transpose_list_of_lists(data)
print(data_transposed)

# Q4.a
print("\nQ4.a")
import pandas as pd
anomaly_df = pd.read_table('Land_and_Ocean_summary.txt', comment="%",
                           delimiter="\s+", index_col=0, usecols=range(5),
                           names=['Year', 'Annual Anomaly', 'Annual Unc.',
                                  'Five-year Anomaly', 'Five-year Unc.'])
column_averages_series = exam.calc_column_averages_pandas(anomaly_df)
print(column_averages_series)

# 4.b
print("\nQ4.b")
positive_anomalies = exam.get_positive_anomalies(anomaly_df)
print(positive_anomalies)

# 4.c
print("\nQ4.c")
anomaly_df_filtered = exam.remove_uncertain_anomalies(anomaly_df)
print(anomaly_df_filtered)

# 4.d
print("\nQ4.d")
anomaly_df_w_nans = exam.set_uncertain_anomalies_to_nan(anomaly_df)
print(anomaly_df_w_nans)

# 5.a
print("\nQ5.a")
coin = exam.Coin()
print(coin.tails_probability)

# 5.b
print("\nQ5.b")
biased_coin = exam.Coin(tails_probability=0.25)
print(biased_coin.toss())
print(biased_coin.toss())
print(biased_coin.toss())

# 5.c
print("\nQ5.c")
toss_statistics = coin.toss_multiple(1000)
print(toss_statistics)