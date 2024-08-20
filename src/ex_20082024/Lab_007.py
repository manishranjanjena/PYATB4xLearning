#Question:
'''Create a program that determines whether a given year is a leap year.
A leap year is divisible by 4, but not by 100 unless it is also divisible by 400.
Use an if-else statement to make this determination.'''

# Year = int(input("Enter Year : \n"))
#
# if Year % 4 == 0 and Year % 100 != 0 or Year % 400 == 0:
#     print(f"This {Year} is a Leap year")
# else:
#     print(f"This {Year} is not a Leap year")

#Or we can write -------

Year = int(input("Enter Year : \n"))

if Year % 400 == 0:
    print(f"This {Year} is a Leap year")
elif Year % 100 == 0:
    print(f"This {Year} is not a Leap year")
elif Year % 4 == 0:
    print(f"This {Year} is a Leap year")
else:
    print(f"This {Year} is not a Leap year")


#Question:
'''
Write a program that classifies a triangle based on its side lengths. 
Given three input values representing the lengths of the sides, 
determine if the triangle is 
equilateral (all sides are equal), isosceles (exactly two sides are equal), or scalene (no sides are equal). 
Use an if-else statement to classify the triangle.
'''

sideA = float(input("Enter the side A in cm: \n"))
sideB = float(input("Enter the side B in cm: \n"))
sideC = float(input("Enter the side C in cm: \n"))

if sideA == sideB == sideC:
    print("Triangle is called Equilateral.")
elif sideA == sideB or sideA == sideC or sideB == sideC:
    print("Triangle is called Isosceles.")
else:
    print("Triangle is called Scalene.")
