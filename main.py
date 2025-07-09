import sys
from stats import get_num_words, get_histogram, get_sort_histogramlist

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        return f.read(-1)

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        exit(1)

    filepath = sys.argv[1]
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    booktext = get_book_text(filepath)
    histogram = get_histogram(booktext)
    sorted = get_sort_histogramlist(histogram)
    print(f"Found {get_num_words(booktext)} total words")
    print("----------- Word Count ----------")
    for itm in sorted:
        print (f"{itm['char']}: {itm['num']}")

main()
