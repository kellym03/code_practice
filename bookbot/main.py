from stats import count_words, unique_char_count, dict_to_sorted_list
import sys

def get_book_text(path):
    """Opens a file and returns its contents as a string."""
    with open(path) as f:
        return f.read()

def main():
    """Coordinates the program execution."""
    # Define the path to your book file
    #path_to_file = "books/frankenstein.txt"

    # 1. Check if the list has exactly two entries:
    # Entry 0 is 'main.py', Entry 1 is the file path.
    if len(sys.argv) != 2:
        # 2. Print the explanation message
        print("Usage: python3 main.py <path_to_book>")
        # 3. Exit with status code 1 (indicating an error occurred)
        sys.exit(1)

    path_to_file = sys.argv[1]
    
    # Get the text contents using our helper function
    text = get_book_text(path_to_file)

    #Print the use word count of the text
    num_words = count_words(text)

    character_dict = unique_char_count(text)
    
    dict_list = []
    for key in character_dict:
        if key.isalpha(): #.isalpha returns a boolean value if a character is alphanumeric
            key_value_pair = {key:character_dict[key]}
            dict_list.append(key_value_pair)
    dict_list.sort(reverse=True, key=dict_to_sorted_list)

    print(f"""============ BOOKBOT ============
Analyzing book found at {path_to_file}
----------- Word Count ----------
Found {num_words} total words
--------- Character Count -------  """)
    for item in dict_list:
        for char, count in item.items():
            print(f"{char}: {count}")
    print("============= END ===============")

    

# This calls the main function to start the program
main()