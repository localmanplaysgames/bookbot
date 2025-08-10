import sys

from stats import count_words, sort_character_recurrance

def check_args():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

def main():
    check_args()
    book_filepath = sys.argv[1]
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {count_words(book_filepath)} total words")
    print("--------- Character Count -------")
    for character in sort_character_recurrance(book_filepath):
        if character["char"].isalpha():
            print(f"{character["char"]}: {character["num"]}")
    print("============= END ===============")

main()