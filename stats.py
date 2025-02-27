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
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {words} total words")
    print("--------- Character Count -------")
    for k, v in chars.items():
        print(f"{k}: {v}")
    print("============= END ===============")