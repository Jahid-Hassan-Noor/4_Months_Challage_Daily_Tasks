print("Day 4: Deep Dive Exercises")


# DEEP DIVE - 1: : The Reference Trap
print("DEEP DIVE - 1: : The Reference Trap")
a = [1, 2, 3]
b = a  
b.append(99)
print("List a after modifying b:", a)
print("List b after modification:", b)
print("1st Program is complete.")




# DEEP DIVE - 2: Micro-Challenge: The Slicing Surgeon
print("DEEP DIVE - 2: Micro-Challenge: The Slicing Surgeon")
data = [10, 20, 30, 40, 50]
new_data = data[-1:-4:-1]
print("Existing data:", data)
print("The new sliced list is:", new_data)
print("2nd Program is complete.")




# DEEP DIVE - 3: Micro-Challenge: The Stack Emulator
print("DEEP DIVE - 3: Micro-Challenge: The Stack Emulator")
data = []
data.append(1)
data.append(2)
data.append(3)
print("Stack after pushes:", data)
data.pop()
print("Stack after one pop:", data)
data.pop()
print("Stack after second pop:", data)
print("3rd Program is complete.")




# DEEP DIVE - 4: Micro-Challenge: The One-Line Architect
print("DEEP DIVE - 4: Micro-Challenge: The One-Line Architect")
data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
new_data = [num**2 for num in data if num % 2 == 0]
print("Existing data:", data)
print("The new list with squares of even numbers is:", new_data)
print("4th Program is complete.")

