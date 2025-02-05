#print("hello world")

def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    #print(text)

    num_words = get_num_words(text)
    #print(f"Total {num_words} words in this text file!")

    chars_dict = get_chars_dict(text)
    #print (chars_dict)

    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document")
    print()

    print_report(chars_dict)
    print("--- End report ---")


def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_num_words(text):
    words = text.split()
    return len(words)

def get_chars_dict(text):
    chars = {}
    for c in text.lower():
        if c in chars:
            chars[c] += 1
        else:
            chars[c] = 1
    return chars

def print_report(dict):
    list_dict = []
    for c in dict:
        if c.isalpha():
            list_dict.append({"name": c, "count": dict[c]}) 
    list_dict.sort(reverse=True, key=sort_on)

    for i in range(0, len(list_dict)):
        print(f"The '{list_dict[i]["name"]}' character was found {list_dict[i]["count"]} times")
    
def sort_on(dict):
    return dict["count"]
            
main()