# Day - 6 - > DEEP DIVE: Theory: Hash Tables
print("Day 6: Deep Dive Exercises")

print()
# DEEP DIVE - 1: Micro-Challenge: The Scope Fortress
print("DEEP DIVE - 1: Micro-Challenge: The Scope Fortress")

x = 10

def change_x():
	x = 20
	print("Inside function, x =", x)

change_x()
print("Outside function, x =", x)


print()
# DEEP DIVE - 2: Micro-Challenge: The Pure Return
print("DEEP DIVE - 2: Micro-Challenge: The Pure Return")

def add(a, b):
    return a + b

res = add(5, 5)
print("The result of add(5, 5) is:", res)



print()
# DEEP DIVE - 3: Micro-Challenge: The Default Gateway
print("DEEP DIVE - 3: Micro-Challenge: The Default Gateway")

def connect(port=3306):
	print(f"Connecting to {port}")

connect()
connect(5432)


print()
# DEEP DIVE - 4: Micro-Challenge: The Logic Gate
print("DEEP DIVE - 4: Micro-Challenge: The Logic Gate")

def is_even(num):
    return num % 2 == 0

print(is_even(4))
print(is_even(7))

print("All Deep Dive programs for day 6 are complete.")
print()
