def count_book_words(book_filepath):
    with open(book_filepath) as book:
        book_text = book.read()
    word_count = len(book_text.split())
    return word_count

def count_book_letters(book_filepath):
    with open(book_filepath) as book:
        book_text = book.read()
    character_dictionary = {}
    for c in book_text.lower():
        if c in character_dictionary:
            character_dictionary[c] += 1
        else:
            character_dictionary[c] = 1
    return character_dictionary

def sort_dictionary(book_filepath):
    with open(book_filepath) as book:
        book_text = book.read()
    character_dictionary = {}
    for c in book_text.lower():
        if c in character_dictionary:
            character_dictionary[c] += 1
        else:
            character_dictionary[c] = 1
    character_dictionary = dict(sorted(character_dictionary.items(), key=lambda item: item[1], reverse=True))
    return character_dictionary