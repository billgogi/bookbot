import sys

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents

from stats import word_count
from stats import char_count
from stats import sort

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    filepath = sys.argv[1]
    text = get_book_text(filepath)
    word_count_result = word_count(text)
    char_count_result = char_count(text)
    sorted_characters = sort(char_count_result)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count_result} total words")
    print("--------- Character Count -------")
    for char, count in sorted_characters:
        if char.isalpha():
            print(f"{char}: {count}")
    print("============= END ===============")

main()