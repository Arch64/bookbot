from collections import Counter

def get_word_count(text):
    return len(text.split())

def get_char_count(text):
    char_count = {}
    for char in text.lower():
        if not char.isalpha():
            continue

        if char not in char_count:
            char_count[char] = 0
        char_count[char] += 1
    return char_count

def get_char_count2(text):
    return Counter(text.lower())