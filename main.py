def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    char_count = character_count(text)
    #print(char_count)
    text_dict =  character_count_report(char_count)

def get_book_text(path):
    with open(path) as f:
        return f.read()
    

def get_num_words(text):
    words = text.split()
    return len(words)


def character_count(text):
    lowered_text = text.lower()
    letter_counter = {}
    for letter in lowered_text:
        if letter_counter.get(letter):
            letter_counter[letter] += 1
        else:
            letter_counter[letter] = 1
    return letter_counter


def character_count_report(text_dict):
    sorted_dict = dict(sorted(text_dict.items(), key=lambda x:x[1], reverse=True))

    for key, value in sorted_dict.items():
        if key in "abcdefghijklmnopqrstuvwxyz":
            print(f"The '{key}' character was found {value} times")

    


if __name__ == "__main__":
    main()
