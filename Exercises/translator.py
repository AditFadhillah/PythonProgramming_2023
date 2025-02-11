
english_to_german = {
    "good day": "Guten Tag!",
    "good morning": "Guten Morgen!",
    "goodbye": "Auf Wiedersehen!",
    "how are you": "Wie geht's?",
    "my name is python": "Mein Name ist Python!",
    "do you speak english": "Sprechen Sie Englisch?",
    "where is the bathroom": "Wo ist die Toilette?",
    "thank you": "Danke!",
    "i am sorry": "Es tut mir leid!",
    "a large beer please": "Ein großes Bier, bitte!"
}

def translate_to_german(english_sentence):
    # Remove non-alphabetic and non-space characters, and make it lowercase
    cleaned_sentence = ""
    for char in english_sentence:
        if char.isalpha() or char.isspace():
            cleaned_sentence += char.lower()

    # Check if the cleaned sentence is in the dictionary
    translation = english_to_german.get(cleaned_sentence, "No translation found!")
    
    return translation

if __name__ == "__main__":
    english_sentence = input("English sentence to translate: ")
    translation = translate_to_german(english_sentence)
    print(translation)
