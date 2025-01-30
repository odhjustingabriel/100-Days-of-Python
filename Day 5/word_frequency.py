# Dictionaries and Sets
# a program to count the frequency of each word in a user-provided text.

def count_word_frequency(text):
    # Convert the text to lowercase to make the counting case-insensitive
    text = text.lower()
    
    # Remove punctuation from the text
    punctuation = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    for char in text:
        if char in punctuation:
            text = text.replace(char, '')
    
    # Split the text into words
    words = text.split()
    
    # Use a dictionary to count the frequency of each word
    word_frequency = {}
    for word in words:
        if word in word_frequency:
            word_frequency[word] += 1
        else:
            word_frequency[word] = 1
    
    return word_frequency

def main():
    # Ask the user for input text
    user_input = input("Enter a text to analyze: ")
    
    # Count the frequency of each word
    frequency = count_word_frequency(user_input)
    
    # Display the word frequencies
    print("\nWord Frequencies:")
    for word, count in frequency.items():
        print(f"{word}: {count}")

if __name__ == "__main__":
    main()