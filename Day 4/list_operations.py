#A program to find the largest number in a list of integers.
#Sort the list in ascending order without using the built-in sort() method


def find_largest_number(numbers):
    largest = numbers[0]
    for num in numbers:
        if num > largest:
            largest = num
    return largest

def bubble_sort(numbers):
    
    n = len(numbers)
    for i in range(n):
        for j in range(0, n-i-1):
            if numbers[j] > numbers[j+1]:
                # Swap the elements
                numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
    return numbers

def main():
    user_input = input("Enter a list of numbers (separate using commas): ")
    
    # Convert the input string into a list of integers
    numbers = [int(num) for num in user_input.split(',')]
    
    largest_number = find_largest_number(numbers)
    print(f"The largest number in the list is: {largest_number}")
    
    sorted_numbers = bubble_sort(numbers)
    print(f"The sorted list in ascending order is: {sorted_numbers}")

if __name__ == "__main__":
    main()