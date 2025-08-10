from stats import count_words, sort_character_recurrance

book_filepath = "./books/frankenstein.txt"
word_count = count_words(book_filepath)
character_count = sort_character_recurrance(book_filepath)

def main():
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for character in character_count:
        if character["char"].isalpha():
            print(f"{character["char"]}: {character["num"]}")
    print("============= END ===============")

main()