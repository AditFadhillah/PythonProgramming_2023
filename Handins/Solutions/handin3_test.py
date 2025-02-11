import handin3

word_list = handin3.read_word_file('british-english')
print(word_list)

filtered_word_list = handin3.read_word_file2('british-english', filter_re_str='^py[a-zA-Z]{4}$')
print(filtered_word_list)
