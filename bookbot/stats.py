def count_words(book_text):
    word_count = len(book_text.split())
    return word_count

def unique_char_count(book_text):
    lower_book_text = book_text.lower()
    char_dict = {}
    for char in lower_book_text:
        if(char in char_dict):
            char_dict[char] += 1
        else:
            char_dict[char] = 1
    return char_dict