# stats.py

def get_num_words(text):
    """Counts the number of words in a given text."""
    words = text.split()
    num_words = len(words)
    return num_words

def get_character_num(text):
    """Counts the occurrences of each character in a given text."""
    text = text.lower()
    char_counts = {}
    for char in text:
        if char in char_counts: 
            char_counts[char] = char_counts[char] + 1
        else:
            char_counts[char] = 1
    return char_counts

def get_sorted_char_counts(char_counts):
    """
    Takes a dictionary of character counts and returns a sorted list of dictionaries.
    Each dictionary in the list contains a 'char' and its 'num' (count).
    The list is sorted in descending order by count, and only includes alphabetic characters.
    """
    char_list = []
    for char, count in char_counts.items():
        if char.isalpha(): # Only include alphabetic characters in the report
            char_list.append({"char": char, "num": count})
    
    # Sort the list of dictionaries by the "num" key in descending order
    char_list.sort(key=lambda x: x["num"], reverse=True)
    
    return char_list