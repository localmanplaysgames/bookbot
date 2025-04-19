from stats import count_book_words, sort_dictionary

def main():

    book_url = "books/frankenstein.txt"
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