import sys
from stats import count_book_words, sort_dictionary

def main():

    arguments = sys.argv
    
    if len(arguments) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_url = arguments[1]

    # book_url = "books/frankenstein.txt"
    word_count = count_book_words(book_url)
    letter_count = sort_dictionary(book_url)

    print("============ BOOKBOT ============")
    print(f"Analysing book found at {book_url}...")

    print("----------- Word Count ----------")

    print(f"Found {word_count} total words")
    print("--------- Character Count -------")

    for letter, count in letter_count.items():
        if letter.isalpha():
            print(f"{letter}: {count}")
        else:
            pass
            
    print("============= END ===============")

main()