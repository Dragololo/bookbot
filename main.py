# main.py

import sys
from stats import get_num_words, get_character_num, get_sorted_char_counts

def get_book_text(path_to_file): 
    """Reads the content of a book from a given file path."""
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

def main():
    """
    Main function to orchestrate the book analysis and report generation.
    """
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    path_to_file = sys.argv[1] # The book path is the second argument from the command line

    # --- Data Processing ---
    book_text = get_book_text(path_to_file)
    num_words = get_num_words(book_text)
    char_counts = get_character_num(book_text)
    sorted_char_list = get_sorted_char_counts(char_counts)

    # --- Report Generation ---
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path_to_file}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    
    for item in sorted_char_list:
        print(f"{item['char']}: {item['num']}")
        
    print("============= END ===============")

if __name__ == "__main__":
    main()