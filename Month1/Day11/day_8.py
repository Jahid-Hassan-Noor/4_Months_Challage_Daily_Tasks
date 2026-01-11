# Day - 8 - > DEEP DIVE: Theory: The Physics of Code (Time Complexity)
print("Day 8: Deep Dive Exercises")

import time


print()
# DEEP DIVE - 1: Micro-Challenge: The Linear Scan (O(N))
print("DEEP DIVE - 1: Micro-Challenge: The Linear Scan (O(N))")

numbers = list(range(1_000_000))
if -5 in numbers:
    print("-5 found in the list.")
else:
    print("-5 not found in the list.")
print()


# DEEP DIVE - 2: Micro-Challenge: The Hash Lookup (O(1)))
print("DEEP DIVE - 2: Micro-Challenge: The Hash Lookup (O(1))")

numbers_set = set(numbers)
if -5 in numbers_set:
    print("-5 found in the set.")
else:
    print("-5 not found in the set.")
print()


# DEEP DIVE - 3: Micro-Challenge: The Insertion Trap (O(N))
print("DEEP DIVE - 3: Micro-Challenge: The Insertion Trap (O(N))")
my_list = [1, 2, 3, 4, 5]
my_list.append(6)
print("List after appending:", my_list)
my_list.insert(0, 0)
print("List after insertion:", my_list)
print()


# DEEP DIVE - 4: Micro-Challenge: The Queue Bottleneck (Pop)
print("DEEP DIVE - 4: Micro-Challenge: The Queue Bottleneck (Pop)")

my_list = [1, 2, 3, 4, 5]
print("Original list:", my_list)
my_list.pop()
print("List after popping last element:", my_list)
popped_element = my_list.pop(0)
print("Popped element:", popped_element)
print("List after popping:", my_list)
print()

# DEEP DIVE - 5: Micro-Challenge: The String Builder (O(N^2) )
print("DEEP DIVE - 5: Micro-Challenge: The String Builder (O(N^2))")
s = "a"
for i in range(1, 10000):
    s += "a"
print("Final string length:", len(s))
print()


# DEEP DIVE - 6: Micro-Challenge: The Lenght Trick (O(1))
print("DEEP DIVE - 6: Micro-Challenge: The Lenght Trick (O(1))")
billion_list = list(range(1_000_000_000))
print("Length of billion_list:", len(billion_list))
print()

# DEEP DIVE - 7: Micro-Challenge: The Quadratic Nested Loop (O(N^2))
print("DEEP DIVE - 7: Micro-Challenge: The Quadratic Nested Loop (O(N^2))")
n = 1000
count = 0
for i in range(n):
    for j in range(n):
        count += 1
print("Count:", count)



# DEEP DIVE - 8: Micro-Challenge: The Sorting Cost (O(N log N))
print("DEEP DIVE - 8: Micro-Challenge: The Sorting Cost (O(N log N))")
import random

# Create a random list of integers
random_list = [random.randint(0, 1000) for _ in range(20)]

# Sort the list (do not sort inside a loop!)
sorted_list = sorted(random_list)

print("Original list:", random_list)
print("Sorted list:", sorted_list)

print()


# DEEP DIVE - 9: Micro-Challenge: The Dictionary Creator (O(1))
print("DEEP DIVE - 9: Micro-Challenge: The Dictionary Creator (O(1))")

kvpairs = [(str(i), i) for i in range(1_000_000)]

start_time = time.time()
dict_pairs = dict(kvpairs)
build_time = time.time() - start_time

start_time = time.time()
search_val = dict_pairs.get("999999")
search_time = time.time() - start_time

print(f"Time to build dict: {build_time:.6f} seconds")
print(f"Time to search dict: {search_time:.10f} seconds")

print()


# DEEP DIVE - 10: Micro-Challenge: The Slice Copy (O(k))
print("DEEP DIVE - 10: Micro-Challenge: The Slice Copy (O(k))")

data = list(range(10_000_000))

start = time.time()
slice = data[0:5000]
elapsed = time.time() - start

print(f"Time to slice 5000 elements: {elapsed:.8f} seconds")