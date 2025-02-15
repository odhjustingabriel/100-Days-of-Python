def count_file_stats(file_path):
    try:
        with open (file_path, 'r') as file:
            content = file.read()
            
            # Count the number of lines
            lines = content.splitlines()
            num_lines = len(lines)
            
            # Count the number of words
            words = content.split()
            num_words = len(words)
            
            # Count the number of characters
            num_chars = len(content)
            
            # Display the results
            print(f"Number of lines: {num_lines}")
            print(f"Number of words: {num_words}")
            print(f"Number of characters: {num_chars}")
    
    except FileNotFoundError:
        print(f"The file {file_path} was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
file_path = 'C:\\Users\\odhju\\100-Days-of-Python\\text.txt'  # Replace with your file path
count_file_stats(file_path)