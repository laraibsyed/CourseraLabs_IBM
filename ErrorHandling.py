import math

def safe_divide(numerator, demoninator):
    try:
        result = numerator // demoninator
        print(numerator, "/", demoninator, "=", result)
    except ZeroDivisionError:
        print("Error: Cannot divide by 0")

num1 = int(input("Enter the numerator: "))
num2 = int(input("Enter the denominator: "))

safe_divide(num1, num2)

def square_root(number1):
    try:
        answer = math.sqrt(number1)
        print("The square root of ", number1, " is: ", answer)
    except ValueError:
        print("Invalid input! Please enter a positive integer or a float value.")

number1 = float(input("Enter a number: "))
square_root(number1)

def math_task(num):
    try:
        divider = num - 5
        res = num / divider
        print("The result is: ", res)
    except Exception as e:
        print("An error occurred during the calculation.")

num = float(input("Enter a number: "))
math_task(num)