def count_book_words(book_filepath):
    with open(book_filepath) as book:
        book_text = book.read()
    word_count = len(book_text.split())
    return word_count