def main():
    path_to_file = "books/frankenstein.txt"
    text = get_book_text(path_to_file)
    word_count = count_words(text)
    lowered_text = text.lower()
    print(f"Word count: {word_count}")
    letter_counts = count_letters(lowered_text)
    for letter, count in letter_counts.items():
        print(f"'{letter}': {count}")

   
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
    return charactercount

main()