# Palindrome: a word or phrase that reads the same backwards as forwards

def is_palindrome(input_string):
    cleaned_string = input_string.replace(" ", "").lower() # Remove spaces and convert to lowercase for uniformity
    return cleaned_string == cleaned_string[::-1] # Checks if string is a palindrome

def main():
    user_input = input("Enter string: ")
    
    if is_palindrome(user_input):
        print(f"{user_input} is a palindrome.")
    else:
        print(f"{user_input} is not a palindrome.")
        
if __name__ == "__main__":
    main()