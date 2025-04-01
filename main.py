from stats import get_num_words, get_num_characters, sorted_characters
from sys import argv, exit

def get_book_text(path_to_file):
    with open(path_to_file) as book_file:
        contents = book_file.read()
        return contents

def main():
    try:
        book_contents = get_book_text(argv[1])
        num_words = get_num_words(book_contents)
        char_dict = get_num_characters(book_contents)
        sorted_list = sorted_characters(char_dict)
        print(' BOOKBOT '.center(30,'='))
        print(f'Analyzing book found at {argv[1]}...')
        print(' Word Count '.center(30,'-'))
        print(f'Found {num_words} total words')
        print(' Character Count '.center(30,'-'))
        for char in sorted_list:
            print(f'{char['name']}: {char['count']}')
        print(' END '.center(30,'-'))
    except IndexError:
        print('Usage: python3 main.py <path_to_book>')
        exit(1)
        


main()