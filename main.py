def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    print(text)
    print(get_chars(text))
    report(dict_to_sorted_list(get_chars(text)), book_path, get_book_length_words(text))
    
    

def get_chars(text):
    chars = {}
    lowercase_text = text.lower()
    for char in lowercase_text:
        if char.isalpha():
            if char in chars:
                chars[char] += 1
            else:
                chars[char] = 1
    return chars

def report(sorted_list, book_path, num_words):
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document")
    print()

    for item in sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"the '{item['char']}' character was found {item['num']} times")

def sort_on(dict):
    return dict["num"]

def dict_to_sorted_list(dict):
    list = [] 
    for ch in dict:
        list.append({"char": ch, "num": dict[ch]})
    list.sort(reverse=True, key=sort_on)
    return list







def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def get_book_length_words(text):
    words = text.split()
    return len(words)
    
if __name__ == "__main__":
    main()