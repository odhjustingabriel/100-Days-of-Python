def is_palindrome(input_string):
    cleaned_string = input_string.replace(" ", "").lower() # Remove spaces and convert to lowercase for uniformity
    return cleaned_string == cleaned_string[::-1] # Check if the string reads the same backward as forward

def main():
    user_input = input("Enter string: ")
    
    if is_palindrome(user_input):
        print("The string is a palindrome.")
    else:
        print("The string is not a palindrome.")
        
if __name__ == "__main__":
    main()