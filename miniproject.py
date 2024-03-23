import json
import difflib
import requests

# Load JSON data into a Python dictionary from the provided URL
def load_dictionary_from_url(url):
    response = requests.get(url)
    if response.status_code == 200:
        data = json.loads(response.text)
        return data
    else:
        print("Failed to fetch data from the URL.")
        return None

dictionary_url = "https://raw.githubusercontent.com/mutemip/dictionary-data/master/data.json"
dictionary = load_dictionary_from_url(dictionary_url)

# Function to get definition of a word
def get_definition(word):
    if dictionary:
        word = word.lower()  #to lowercase
        if word in dictionary:
            return dictionary[word]
        else:
            
            suggestions = difflib.get_close_matches(word, dictionary.keys())
            if suggestions:
                suggestion = suggestions[0]  # Take the first suggestion
                return f"Word not found. Did you mean '{suggestion}'?"
            else:
                return "Word not found."
    else:
        return "Dictionary data not available."

# Example usage
while True:
    user_input = input("Enter a word to get its definition (or 'q' to quit): ")
    if user_input.lower() == 'q':
        break
    definition = get_definition(user_input)
    print(definition)


