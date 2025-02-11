import string

def process_word(word):
    # Remove punctuation and convert to lowercase
    return word.translate(str.maketrans('', '', string.punctuation)).lower()

def main():
    word_counts = {}
    
    with open('sonnets.txt', 'r') as file:
        lines = file.readlines()[:-1]
        for line in lines:
            words = line.split()
            for word in words:
                cleaned_word = process_word(word)
                if cleaned_word:
                    word_counts[cleaned_word] = word_counts.get(cleaned_word, 0) + 1
    
    sorted_word_counts = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)
    
    print("The 50 most common words by Shakespeare:")
    for word, count in sorted_word_counts[:50]:
        print(f"{word} {count}")

if __name__ == "__main__":
    main()
