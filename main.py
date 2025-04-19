from stats import count_book_words, count_book_letters

def main():
    book_word_count = count_book_words("books/frankenstein.txt")
    print(f"Word count: {book_word_count}")
    book_letter_count = count_book_letters("books/frankenstein.txt")
    print(book_letter_count)

main()