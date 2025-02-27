from stats import word_count, char_count, char_report
import sys

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    text = get_book_text(sys.argv[1])
    # print(text)
    words = word_count(text)
    chars = char_count(text)
    # print(chars)
    char_report(words, chars)

def get_book_text(path):
    with open(path) as f:
        return f.read()
    
main()