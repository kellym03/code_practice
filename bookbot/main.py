from stats import count_words, unique_char_count

def get_book_text(path):
    """Opens a file and returns its contents as a string."""
    with open(path) as f:
        return f.read()

def main():
    """Coordinates the program execution."""
    # Define the path to your book file
    path_to_file = "books/frankenstein.txt"
    
    # Get the text contents using our helper function
    text = get_book_text(path_to_file)

    #Print the use word count of the text
    num_words = count_words(text)

    character_dict = unique_char_count(text)
    
    # Print the contents to the console
    print(f"Found {num_words} total words")
    print(character_dict)

# This calls the main function to start the program
main()