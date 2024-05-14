def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    report(text, book_path)

def get_book_text(path):
    with open(path) as f:
        return f.read()

def total_words(book):
    words = book.split()
    print(f"Total Words: {len(words)}")

def count_letters(book):
    words = book.lower()
    letters = {}    
    for char in words:
        if char in letters:
            letters[char] += 1
        else:
            letters[char] = 1
    return letters

def report(book, path):
    sorted_chars = chars_dict_to_sorted_list((count_letters(book)))

    print(book)
    print(f"--- Begin report of {path} ---")
    total_words(book)
    print()
    for item in sorted_chars:
        if not item["char"].isalpha():
            continue
        print(f"The '{item['char']}' character was found {item['num']} times")

    print("--- End report ---")

def sort_on(dict):
    return dict["num"]

def chars_dict_to_sorted_list(num_chars_dict):
    sorted_list = []
    for ch in num_chars_dict:
        sorted_list.append({"char": ch, "num": num_chars_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

main()