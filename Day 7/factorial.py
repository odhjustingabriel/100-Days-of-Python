def calculate_factorial(input_number):
    if input_number < 0:
        return "Factorial is not defined for negative numbers."
    elif input_number == 0 or input_number == 1:
        return 1
    else:
        result = 1
        for i in range(2, input_number + 1):
            result *= i
        return result

def main():
        
 user_input = int(input("Enter Number: "))
 calculate_factorial(user_input)
 
 print(f"The factorial of {user_input} is {calculate_factorial(user_input)}")

    
if __name__ == "__main__":
    main()