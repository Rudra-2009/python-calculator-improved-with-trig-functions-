#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      HP
#
# Created:     10/05/2024
# Copyright:   (c) HP 2024
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import math

print("Python Calculator")

while True:
  operator = input("Please enter your desired operator (+, -, *, /, %, //, sin, cos) or 'q' to quit: ")

  if operator == 'q':
    break

  if operator in ["+", "-", "*", "//"]:
    first = input("Enter first number: ")
    second = input("Enter second number: ")
    try:
      first = int(first)
      second = int(second)
    except ValueError:
      print("Invalid input. Please enter numbers only.")
      continue

    if operator == "+":
      ans = first + second
      print("Your answer is", ans)
    elif operator == "-":
      ans = first - second
      print("Your answer is", ans)
    elif operator == "*":
      ans = first * second
      print("Your answer is", ans)
    elif operator == "//":
      ans = first // second
      print("Your answer is", ans)

  elif operator in ["/", "%"]:
    first = input("Enter first number: ")
    second = input("Enter second number: ")
    try:
      first = int(first)
      second = int(second)
    except ValueError:
      print("Invalid input. Please enter numbers only.")
      continue

    if operator == "/":
      if second == 0:
        print("Error: Cannot divide by zero")
      else:
        ans = first / second
        print("Your answer is", ans)
    elif operator == "%":
      ans = first % second
      print("Your remainder is", ans)

  elif operator.lower() in ["sin", "cos"]:
    val = input("Enter an angle in degrees: ")
    try:
      degree = float(val)
    except ValueError:
      print("Invalid input. Please enter a number for the angle.")
      continue

    if operator.lower() == "sin":
      sin_val = round(math.sin(math.radians(degree)), 4)
      print("Sin of", degree, "degrees is", sin_val)
    elif operator.lower() == "cos":
      cos_val = round(math.cos(math.radians(degree)), 4)
      print("Cos of", degree, "degrees is", cos_val)

  else:
    print("Invalid operator. Please try again.")

print("Thank you for using the calculator!")
