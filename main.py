from stats import *
import sys

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    #book_loc = "books//frankenstein.txt"
    book_loc = sys.argv[1]
    
    book_data = get_book_text(book_loc)
    word_count = get_word_count(book_data)
    char_count = get_char_count(book_data)

    sorted_dict = dict(sorted(char_count.items(), key=lambda x:x[1], reverse=True))
    #word_count.sort(reverse=True, key=lambda a : a)
    #sorted_char_count = sorted(char_count, reverse=True, key=lambda a: char_count[a])

    
    
    make_book_report(book_loc, word_count, sorted_dict)

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def make_book_report(book_loc, word_count, char_count):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_loc}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for key, value in char_count.items():
        print(f"{key}: {value}")

main()