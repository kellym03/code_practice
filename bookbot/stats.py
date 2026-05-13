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

def dict_to_sorted_list(dictionary): #This function is designed to be used with the .sort() key= parameter so that it knows when dealing with a list of dictionaries what to sort it on. 
    return list(dictionary.values())[0] # If you removed the [0], your function would return a list (like [44538]) instead of a number (like 44538). The .sort() method would then try to compare [44538] < [29493]. While Python can sometimes compare lists, it is much slower and less predictable than comparing raw numbers.

"""
When you call dict_list.sort(key=dict_to_sorted_list), this is what happens behind the scenes:
The Extraction Phase: 
Python goes through your list and runs every dictionary through your function. 
It creates a temporary "invisible list" of just the results (the numbers).{'e': 44538} becomes 44538{'t': 29493} becomes 29493{'a': 25894} becomes 25894
The Sorting Phase: 
Python now performs the actual math. It compares these plain numbers. 
It knows that $44538 > 29493$, so it knows the dictionary associated with 44538 should come first.
The Re-ordering Phase: 
Python moves the original dictionaries into their new positions based on where their "translated" numbers landed.
"""