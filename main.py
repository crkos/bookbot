with open('books/frankenstein.txt') as book:
    file_contents = book.read()

def number_of_words(text):
    words = text.split()
    return len(words)

def count_letters(text):
    new_dict = {}
    for letter in text:
        number = 1;
        if new_dict.get(letter.lower()) == None:
            new_dict[letter.lower()] = number
        else:
            new_dict[letter.lower()] = new_dict[letter.lower()] + number
    return new_dict


number_of_words = number_of_words(file_contents)
letters_counts = count_letters(file_contents)
def print_report():
    
    print('--- Begin report of books/frankenstein.txt ---')
    print(f'{number_of_words} words found in the document')
    letters_list = []
    for letter in letters_counts:
        if letter.isalpha():
            letters_list.append(letter)
    letters_list.sort()
    for letter in letters_list:
        word_count = letters_counts[letter]
        print(f"The '{letter}' character was found {word_count} times")



print_report()