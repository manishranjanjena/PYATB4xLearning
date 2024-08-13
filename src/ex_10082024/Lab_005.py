
#Task #1
#-------------------------------------------------------
# Home Can you create a Program I will give you number(userinput and print table)
#
# f"{}" String format concept
# User input - num int -> 10, 100, -1, 2, 3.14 -> input
# 9x1 = 9
# 9x2 = 18... till 10
#-------------------------------------------------------

table = float(input("Enter the number : "))
print(f"The table of {table} is")
print(f"{table}*1={table*1}")
print(f"{table}*2={table*2}")
print(f"{table}*3={table*3}")
print(f"{table}*4={table*4}")
print(f"{table}*5={table*5}")
print(f"{table}*6={table*6}")
print(f"{table}*7={table*7}")
print(f"{table}*8={table*8}")
print(f"{table}*9={table*9}")
print(f"{table}*10={table*10}")
print("  ")


#Task #2
#-------------------------------------------------------
# Create a program , take 2 inputs from the user num1, num2 and give them
# max
# pow num1 to num2
# sub, mul, sum, div.
# Format your out with f{""}
#-------------------------------------------------------



num1 = int(input("Enter the num1 : "))
num2 = int(input("Enter the num2 : "))

print(f"Maximum number is: {max(num1, num2)}")
print(f"The {num1} to the power of {num2} is = {pow(num1, num2)}")
print(f"Sum is {num1}+{num2}={num1+num2}")
print(f"Sub is {num1}-{num2}={num1-num2}")
print(f"Mul is {num1}*{num2}={num1*num2}")
print(f"Div is {num1}/{num2}={num1/num2:.3f}")
