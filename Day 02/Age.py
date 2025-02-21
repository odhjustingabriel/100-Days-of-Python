#Prompts the user to input their age.
#Calculates the number of days they’ve lived (approximate = 365 days/year).

name = input("Enter your name: ")
age = int(input("Enter your age: "))
       
days_lived = age * 365

print(f"Your name is {name} and you are {age} years old.\nYou have been alive for {days_lived} days.")

