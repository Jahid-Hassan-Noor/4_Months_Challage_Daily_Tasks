# Day 14 -> DEEP DIVE: The Final Boss (Algorithmic Logic)
print("Day 14: Deep Dive Exercises")
print()



from itertools import groupby
from operator import itemgetter
from collections import Counter



# DEEP DIVE - 1: Two Sum (O(N))
print("DEEP DIVE - 1: Two Sum")

def two_sum(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        needed = target - num
        if needed in seen:
            return seen[needed], i
        seen[num] = i
numbers = [2, 7, 11, 15]
print(two_sum(numbers, 9))
print()




# DEEP DIVE - 2: Palindrome (Slicing)
print("DEEP DIVE - 2: Palindrome")

def is_palindrome(text):
    clean = "".join(text.lower().split())
    return clean == clean[::-1]
print(is_palindrome("Never odd or even"))
print(is_palindrome("Hello"))
print()




# DEEP DIVE - 3: Anagrams (Frequency)
print("DEEP DIVE - 3: Anagrams")

def are_anagrams(a, b):
    return Counter(a) == Counter(b)

print(are_anagrams("silent", "listen"))
print(are_anagrams("hello", "world"))
print()



# DEEP DIVE - 4: Flattening (Recursion)
print("DEEP DIVE - 4: Flattening")

def flatten(lst):
    result = []
    for item in lst:
        if isinstance(item, list):
            result.extend(flatten(item))
        else:
            result.append(item)
    return result
nested = [1, [2, [3, 4]]]
print(flatten(nested))
print()


# DEEP DIVE - 5: FizzBuzz (The Logic Gate)
print("DEEP DIVE - 5: FizzBuzz")

for i in range(1, 21):
    if i % 15 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
print()



# DEEP DIVE - 6: Deduplication (O(N))
print("DEEP DIVE - 6: Deduplication")

def remove_duplicates(items):
    seen = set()
    result = []
    for item in items:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result
data = [1, 2, 2, 3, 1, 4]
print(remove_duplicates(data))
print()



# DEEP DIVE - 7: Binary Search (O(log N))
print("DEEP DIVE - 7: Binary Search")

def binary_search(nums, target):
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1
sorted_nums = [1, 3, 5, 7, 9]
print(binary_search(sorted_nums, 7))
print()




# DEEP DIVE - 8: Missing Number (Math)
print("DEEP DIVE - 8: Missing Number")

nums = list(range(1, 101))
nums.remove(57)
expected_sum = 100 * 101 // 2
actual_sum = sum(nums)
print("Missing number:", expected_sum - actual_sum)
print()




# DEEP DIVE - 9: Grouping (Itertools)
print("DEEP DIVE - 9: Grouping")

items = [
    {"name": "Apple", "category": "Fruit"},
    {"name": "Carrot", "category": "Vegetable"},
    {"name": "Banana", "category": "Fruit"},
]
items.sort(key=itemgetter("category"))
for category, group in groupby(items, key=itemgetter("category")):
    print(category, list(group))
print()




# DEEP DIVE - 10: Merge Sorted Lists (O(N))
print("DEEP DIVE - 10: Merge Sorted Lists")

def merge_sorted(a, b):
    result = []
    i = j = 0
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            result.append(a[i])
            i += 1
        else:
            result.append(b[j])
            j += 1
    result.extend(a[i:])
    result.extend(b[j:])
    return result
list1 = [1, 3, 5]
list2 = [2, 4, 6]
print(merge_sorted(list1, list2))
print()


print("Deep Dive Exercises for Day 14 are Finished.")
print()