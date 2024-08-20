def main():
    path_to_file = "books/frankenstein.txt"
    text = get_book_text(path_to_file)
    word_count = count_words(text)
    lowered_text = text.lower()
    print("--- Begin report of books/frankenstein.txt --- \n")
    print(f"{word_count} words found in the document\n")
    letter_counts = count_letters(lowered_text)
    # Assuming letter_counts is a list of dictionaries like [{'h': 1}, {'e': 1}, ...]
    letter_counts.sort(reverse=True, key=sort_on)
    for letter_count in letter_counts:
        for letter, count in letter_count.items():
            print(f"The character '{letter}' was found {count} times in the document")
    print("--- End report ---")


   
def count_words(text):
    words = text.split()
    return len(words)

def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_letters(lowered_text):
    charactercount = {}
    for i in lowered_text:
        if i in charactercount:
            charactercount[i] += 1
        else:
            charactercount[i] = 1
    
    # Generate a list of dictionaries
    list_of_dicts = [{letter: count} for letter, count in charactercount.items()]
    
    return list_of_dicts

def sort_on(letter_count_dict):
    # Extract the single value from the dictionary, which is the count
    return next(iter(letter_count_dict.values()))

main()