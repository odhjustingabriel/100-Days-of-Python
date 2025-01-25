#Create a simple script that converts a user-entered temperature from Celsius to Fahrenheit. 
#Formula: F = (C * 9/5) + 32.

# Prompt the user to enter a temperature in Celsius
celsius = float(input("Enter the temperature in Celsius: "))

# Convert Celsius to Fahrenheit
fahrenheit = (celsius * 9/5) + 32

# Display the result
print(f"{celsius} degrees Celsius is equal to {fahrenheit} degrees Fahrenheit.")