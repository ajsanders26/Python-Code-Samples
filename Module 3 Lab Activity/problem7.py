# Aaron Sanders
# 07/20/2025

# Module 3 Problem 7: Calculate the day of the week you will arrive given the starting day

start_day = input("Enter the starting day you leave with a number (e.g. Sunday=0, Monday=1): ")
length = input("Enter the number of days you will be gone: ")

end_day = int(start_day) + int(length) % 7

print(f"You will return on Day {end_day}.")
