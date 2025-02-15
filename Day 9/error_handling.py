# Error Handling (try-except)
def divide_numbers():
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        
        result = num1 / num2
        print(f"The result of {num1} divided by {num2} is {result}")
        
    except ZeroDivisionError:
        print("Error! Division by zero is not allowed.")
    except ValueError:
        print("Error! Invalid input. Please enter valid numbers.")
    except Exception as e:
        print("An unexpected error occurred: {e}")
        
divide_numbers()