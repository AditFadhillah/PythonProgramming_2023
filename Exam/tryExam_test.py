import tryExam

# Q1.a
check_prime1 = tryExam.is_prime(10)
check_prime2 = tryExam.is_prime(11)
print(check_prime1, check_prime2)

# Q1.b
primes1 = tryExam.prime_range(0, 42)
print(primes1)

# Q1.c
primes2 = tryExam.prime_range_one_liner(0, 42)
print(primes2)

# Q2.a
print(tryExam.cpr_regexp.match("123456-7890"))

# Q2.b
century = tryExam.cpr_century("111111-1118")
print(century)
""" error = tryExam.cpr_century("hello")
print(error) """

# Q3.a
import random
data = [ [random.random() for j in range(2)] for i in range(20) ]
print(data)
columns_averages = tryExam.calc_column_averages(data)
print(columns_averages)

# Q3.b
data_transposed = tryExam.transpose_list_of_lists(data)
print(data_transposed)