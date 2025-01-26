def is_palindrome(input_string):
    cleaned_string = input_string.replace(" ", "").lower() # Remove spaces and convert to lowercase for uniformity
    return cleaned_string == cleaned_string[::-1] # Check if the string reads the same backward as forward

string = input("Enter a string to check if it's a palindrome: ")
if is_palindrome(string):
    print(f'"{string}" is a palindrome.')
else:
    print(f'"{string}" is not a palindrome.')