text = open("Land_and_Ocean_summary.txt", "r")

data_list = []

for line in text:
    line = line.strip()
    if not line or line.startswith("%"):
        continue
    
    data_list.append(line)
text.close

def read_data(filename):
    text = open("Land_and_Ocean_summary.txt", "r")

    data_list = []

    for line in text:
        line = line.strip()
        if not line or line.startswith("%"):
            continue
        
        data_list.append(line)
    text.close

    return data_list

data_list_returned = read_data("Land_and_Ocean_summary.txt")

for line in data_list_returned[0:5]:
    print(line)

