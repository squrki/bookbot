
def main():
    text = get_book("books/frankenstein.txt")
    # print(text)
    words = word_count(text)
    chars = char_count(text)
    char_report(words, chars)

def get_book(path):
    with open(path) as f:
        return f.read()
    
def word_count(text):
    words = text.split()
    return len(words)

def char_count(text):
    count = {}
    for char in text:
        if char.isalpha():
            if char.lower() in count:
                count[char.lower()] += 1
            else:
                count[char.lower()] = 1
    return count

def char_report(words, chars):
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{words} words found in the document")
    print("")
    for k, v in chars.items():
        print(f"The '{k}' character was found {v} times")
    print("--- End report ---")

main()