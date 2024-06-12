def count_characters(text):
    char_count = {}  # Initialize an empty dictionary

    for char in text:  # Loop through each character in the text
        char = char.lower()  # Convert character to lowercase
        if char.isalpha():  # Ensure we only count alphabetic characters
            if char in char_count:  # If the character is already in the dictionary
                char_count[char] += 1  # Increment the count
            else:
                char_count[char] = 1  # Initialize the count to 1

    return char_count  # Return the dictionary of character counts

def sort_on(char_count):
    return char_count["num"]

def main():
    with open("books/frankenstein.txt") as f:
        book = f.read()
        
    words = book.split()  # This line splits the text into words
    word_count = len(words)  # This line counts the number of words
    print(f"{word_count} words found in the document\n")  # This prints the number of words
    
    char_counts = count_characters(book)  # Count the characters in the book text

    # Convert dictionary to list of dictionaries for sorting
    char_list = [{"char": char, "num": count} for char, count in char_counts.items()]
    char_list.sort(reverse=True, key=sort_on)  # Sort characters by their frequency

    # Print sorted character frequency
    for item in char_list:
        print(f"The '{item['char']}' character was found {item['num']} times")

main()