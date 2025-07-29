# Aaron Sanders
# 07/29/2025

current_time_str = int(input("What is the current time (in hours 0-23)? "))
wait_time_str = int(input("How many hours do you want to wait? "))

final_time_int = current_time_str + wait_time_str
print(final_time_int % 24)
