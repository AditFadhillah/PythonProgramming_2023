import csv
import string

# Function to generate a letter frequency signature string for a given text file
def generate_letter_frequency(file_path):
    # Read the content of the file, count letter frequencies, and return a sorted frequency fingerprint
    letter_frequency = {}
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read().lower()
        for char in text:
            if char.isalpha():
                letter_frequency[char] = letter_frequency.get(char, 0) + 1
    
    # Sort the letter frequencies by count in descending order
    sorted_frequency = ''.join(sorted(letter_frequency, key=letter_frequency.get, reverse=True))
    return sorted_frequency

# Function to load the language lookup table from a CSV file
def load_language_lookup_table(table_path):
    # Read the CSV file and save its content in a dictionary for easy lookup
    language_lookup = {}
    with open(table_path, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            language = row[0]
            frequencies = row[1:]
            language_lookup[language] = ''.join(frequencies)
    return language_lookup

# Function to compare letter frequencies and detect the language
def detect_language(letter_frequency, language_lookup_table):
    # Compare letter frequency with known languages and find the closest match
    closest_language = None
    min_distance = float('inf')
    
    for language, frequency in language_lookup_table.items():
        distance = levenshtein(letter_frequency, frequency)
        if distance < min_distance:
            min_distance = distance
            closest_language = language
    
    return closest_language

def levenshtein(s1, s2):
    """Calculates the edit distance between two strings s1 and s2 using the Levenshtein Algorithm,
    based on: https://en.wikipedia.org/wiki/Levenshtein_distance. Levenshtein returns the
    number of edits (insertions, deletions or substitutions) are required to change one string
    in the other.

    Args:
        s1 (str): String 1 to compare using Levenshtein's algorithm.
        s2 (str): String 2 to compare using Levenshtein's algorithm.

    Returns:
        int: number of edits that are needed to change s1 in s2, as calculated by the Levenshtein
        Algorithm.
    """
    # Create a 2D list, filled with 0, that has len(s1) + 1 columns and len(s2) + 1 rows
    matrix = [[0 for x in range(len(s2) + 1)] for y in range(len(s1) + 1)]

    # Fill the first row and column with numbers 0 - n
    for i in range(len(s1) + 1):
        matrix[i][0] = i
    for i in range(len(s2) + 1):
        matrix[0][i] = i

    # Perform Levenshtein algorithm using dynamic programming.
    # Loop through all cells of the distance matrix, if the corresponding letters of a cell
    # are equal: fill that cell with the number top-left of it. If not, fill it with the minimum
    # of the cells left, above and top-left of it and increment that number with 1.
    for row in range(1, len(matrix)):
        for col in range(1, len(matrix[0])):
            if s1[row - 1] == s2[col - 1]:
                matrix[row][col] = matrix[row - 1][col - 1]
            else:
                matrix[row][col] = min(
                    matrix[row - 1][col] + 1,
                    matrix[row][col - 1] + 1,
                    matrix[row - 1][col - 1] + 1
                )

    # The Levenshein distance result is the bottom-right number in the distance matrix.
    return matrix[-1][-1]

if __name__ == "__main__":
    # Prompt the user for the text file to analyze
    file_path = input("Which text file should we analyze? ")

    # Call the functions to generate the letter frequency and load the language lookup table
    try:
        letter_frequency = generate_letter_frequency(file_path)
        csvfile = "letter-frequency-per-language.csv"
        language_lookup_table = load_language_lookup_table(csvfile)

        # Call the function to detect the language based on the letter frequency
        detected_language = detect_language(letter_frequency, language_lookup_table)

        # Print out the detected language
        print(f"Language detected: {detected_language}")
    except FileNotFoundError:
        print("File not found. Please provide a valid file path.")
    except KeyError:
        print("Language lookup table not found. Make sure to include 'letter-frequency-per-language.csv'.")

