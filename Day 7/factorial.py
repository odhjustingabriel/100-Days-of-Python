import math

def calculate_factorial(input_number):
    factorial = math.factorial(input_number)
    return factorial

def main():
        
 user_input = int(input("Enter Number: "))
 calculate_factorial(user_input)
 
 print(f"The factorial of {user_input} is {calculate_factorial(user_input)}")

    
if __name__ == "__main__":
    main()