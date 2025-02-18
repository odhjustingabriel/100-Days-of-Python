#A Python script that takes user input for two numbers 
#and performs addition, subtraction, multiplication, and division.
#Display the results with descriptive output

print("Welcome to Python Math Operations")

# Prompt the user to enter two numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Perform operations
addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2

#Divison by 0
if num2 != 0:
    division = num1 / num2
else:
    division = "Undefined (Cannot divide by zero)"
    
# Display the results
print("\nResults: ")
print(f"Addition: {num1} + {num2} = {addition}")
print(f"Subtraction: {num1} - {num2} = {subtraction}")
print(f"Multiplication: {num1} * {num2} = {multiplication}")
print(f"Division: {num1} / {num2} = {division}")