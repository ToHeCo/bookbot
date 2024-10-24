def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = word_count(text)
    char_dict = char_count(text)
    print_report(book_path,num_words,char_dict)

def get_book_text(path):
    with open(path) as f:
        return f.read()

def word_count(text):
    words = text.split()
    return len(words)

def char_count(text):
    char_count = {}
    for char in text:
        if char.lower() not in char_count:
            char_count[char.lower()] = 1
        elif char.lower() in char_count:
            char_count[char.lower()] += 1
    return char_count

def sort_on(dict):
    return dict["num"]

def print_report(book, numWords, charDict):
    print(f'--- Begin report of {book} ---')
    print(f'{numWords} words was found in the document \n')
    
    for char in dict(sorted(charDict.items(), key=lambda item: item[1], reverse= True)):
        if char.isalpha():
            print(f'The {char} was found {charDict[char]} times')
    print("--- End report ---")


main()
    
