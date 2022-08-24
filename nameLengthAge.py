# This program says "Hello," asks the user for their name and age, and prints out the
# length of their name and how old they will be in a year.

print("Hello, World!") # Output

name = input("What is your name?: ") # Gets user name
print("Nice to meet you, " + str(name)) # Turns name into a string and prints out a greeting to the user

print("The length of your name is: " + str(len(name))) # Gets the length of the users name

age = int(input("What is your age?: ")) # Gets the user age

print("In a year you will be: " + str(age + 5)) # Tells the user how old they will be in five years from now
