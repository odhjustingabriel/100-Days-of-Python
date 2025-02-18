#input Length and Width of the rectangle
length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))

#Calculate the perimeter
perimeter = 2 * (length + width)

#Calculate Area
area = length * width

#Print the results
print("Length: ", length)
print("Width: ", width)
print(f"The area of the rectangle with length {length} and width {width} is {area}.")
print(f"The perimeter of the rectangle with length {length} and width {width} is {perimeter}.")