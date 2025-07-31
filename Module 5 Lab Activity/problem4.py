# Aaron Sanders
# 07/30/2025

# Prints numbers 1 to 50, displaying divisability of 3 and 5 in place of valid numbers
for i in range(1, 51):
    if i % 3 == 0 and i % 5 == 0:
        print("Divisible by both")
    elif i % 3 == 0:
        print("Divisible by 3")
    elif i % 5 == 0:
        print("Divisible by 5")
    else:
        print(i)
