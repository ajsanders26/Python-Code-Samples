# Aaron Sanders
# 07/20/2025

# Module 3 Problem 3: Greet only the users you (Aaron) or the instructor (Galen Turoci),

user = "Aaron"
instructor = "Galen Turoci"

name = input("Enter your name: ")
if name == user or name == instructor:
    print(f"Hello {name}! Nice to meet you.")
else:
    print("Your name does not match a valid user!")
