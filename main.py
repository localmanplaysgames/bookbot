# open the book specified by the filepath and retrieve the text within it
def get_book_text(book_filepath):
    with open(book_filepath) as book:
        book_text = book.read()
    return book_text

# get the text from get_book_text and count the number of words in it
def count_book_words(book_filepath):
    book_text = get_book_text(book_filepath)
    word_count = len(book_text.split())
    return word_count

def main():
    book_word_count = count_book_words("books/frankenstein.txt")
    print(f"{book_word_count} words found in the document")

main()