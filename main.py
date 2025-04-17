def get_book_text(book_filepath):
    with open(book_filepath) as book:
        file_contents = book.read()
    return file_contents

def main():
    getbook = get_book_text("books/frankenstein.txt")
    print(getbook)

main()