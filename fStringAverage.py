# This program gets 3 ints from a user, finds their avg,
# then rounds to 2 decimal places.

# User inputs to get their three numbers...
num1 = int(input("Integer #1: ")) 
num2 = int(input("Integer #2: "))
num3 = int(input("Integer #3: "))

average = (num1 + num2 + num3) / 3 # Calculates the average and puts it in a variable

print(f"Your average is: {average:.2f}") # Using f-string interpolation, rounds the average to 2 decimal places and prints it out
