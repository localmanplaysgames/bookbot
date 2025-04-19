from stats import count_book_words

def main():
    book_word_count = count_book_words("books/frankenstein.txt")
    print(f"{book_word_count} words found in the document")

main()