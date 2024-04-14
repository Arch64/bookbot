def main():
    book_report('books/frankenstein.txt')

def book_report(book_loc):
    book_contents = read_book(book_loc)
    words_count = word_counter(book_contents)
    letter_count = count_letters(book_contents)
    sorted_letter_count = sorted_by_frequency(letter_count)

    print(f'''--- Begin report of {book_loc} ---''')
    print(f'{words_count} words found in the document')
    print()

    for letter, frequency in sorted_letter_count:
        print(f"The '{letter}' character was found {frequency} times")

    print('--- End report ---')


def read_book(book_loc):
    with open (book_loc) as f:
        file_contents = f.read()
    return file_contents


def word_counter(file):
    words = file.split()
    return len(words)


def count_letters(file):
    letter_counter = {}
    for letter in file:
        letter = letter.lower()
        if letter in letter_counter:
            letter_counter[letter] += 1
        else:
            letter_counter[letter] = 1
    return letter_counter


def sorted_by_frequency(letter_dictonary):
    data = {key:value for key, value in letter_dictonary.items() if key.isalpha()}
    sorted_data = sorted(data.items(), key=lambda x:x[1], reverse=True)
    return sorted_data


main()