#Prompts the user to input their age.
#Calculates the number of days they’ve lived (approximate = 365 days/year).

#Prompt user age
age = int(input("Enter your age: "))

#Calculate the number of days lived
days_lived = age * 365

#Print the result
print(f"Your are {age} years old and have lived for {days_lived} days.")

