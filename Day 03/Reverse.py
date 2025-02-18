def reverse_and_count_vowels(input_string):
    reversed_string = input_string[::-1] # Reverse the string
    vowels = "aeiou"
    vowel_count = sum(1 for char in input_string.lower() if char in vowels) # Count vowels (case-insensitive)
    return reversed_string, vowel_count

string = input("Enter a string to reverse and count vowels: ")
reversed_string, vowel_count = reverse_and_count_vowels(string)
print(f'Reversed string: "{reversed_string}"')
print(f'Number of vowels in the string: {vowel_count}')
