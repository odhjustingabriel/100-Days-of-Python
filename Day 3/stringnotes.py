s = "abcdefghij"

print(s[::-1])#reverse a string [jihgfedcba]
print(s[::-2])#every 2nd letter from the end [jhfdb]
print(s[::2])#every 2nd letter from the start [acegi]
print(s[5:2:-1])#partial reverse from the 5 to 2 index [fed]
print(s[2:5])#from index 2 to 5[cde]
#[start:stop:step]

data = "apple,banana,cherry,dates,mangoes,oranges"
print(data.split(',', 3))  #['apple', 'banana', 'cherry', 'dates,mangoes,oranges']

# Right split (rsplit)
print(data.rsplit(',', 2))  #['apple,banana,cherry,dates', 'mangoes', 'oranges']

# Remove leading/trailing characters
dirty = "***Hello!!!***"
print(dirty.strip('*!'))  # Hello

# Custom stripping
url = "https://www.example.com/"
print(url.strip('htps:/'))  # www.example.com

# Replace multiple patterns
text = "I like cats, cats are cool."
print(text.replace("cats", "dogs", 1))  # "I like dogs, cats are cool."

# Use translation tables for multiple substitutions
translation_table = str.maketrans({'a': '4', 'e': '3', 'i': '1'})
message = "Hack the planet!"
print(message.translate(translation_table))  # H4ck th3 pl4n3t!