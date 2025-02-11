import handin3

# test read_word_file function
word_list = handin3.read_word_file(filename='british-english')
# print the first 10 lines
print(word_list[0:10]) 

# tst read_word_file2 function with a filter, define the filter
filtered_word_list = handin3.read_word_file2(filename='british-english', filter_re_str=r'^py[A-Za-z]{4}$')
# print filtered lines
print(filtered_word_list) 
