# Day - 6 - > DEEP DIVE: Theory: Error Handling (Exceptions)
print("Day 6: Deep Dive Exercises")


print()
# DEEP DIVE - 1: Micro-Challenge: The Input Guard
print("DEEP DIVE - 1: Micro-Challenge: The Input Guard")

def get_number():
    while True:
        try:
            num = int(input("Enter a number: "))
            return num
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

num = get_number()
print(f"You entered: {num}")




print()
# DEEP DIVE - 2: Micro-Challenge: The Matha Safety Net
print("\nDEEP DIVE - 2: Micro-Challenge: The Matha Safety Net")

x = 0
try:
    res = 100 / x
    print("Result:", res)
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")



print()
# DEEP DIVE - 3: Micro-Challenge: The Cleanup Crew
print("\nDEEP DIVE - 3: Micro-Challenge: The Cleanup Crew")

try:
    a = 10
    b = 0
    result = a / b
    print("Result:", result)
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")
finally:
    print("Execution Complete")




print()
# DEEP DIVE - 4: Micro-Challenge: The Custom Signal
print("\nDEEP DIVE - 4: Micro-Challenge: The Custom Signal")

num = int(input("Enter a number: "))
if num < 0:
    raise ValueError("No negatives")
print("You entered:", num)




print("All Deep Dive programs for day 7 are complete.")