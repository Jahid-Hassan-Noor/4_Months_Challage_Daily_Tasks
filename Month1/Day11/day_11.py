# Day - 10 - > DEEP DIVE: Theory: Functional Programming (Lambda Map)
print("Day 10: Deep Dive Exercises")

import time
from functools import reduce


print()
# DEEP DIVE - 1: Micro-Challenge: The Anonymous Function
print("DEEP DIVE - 1: Micro-Challenge: The Anonymous Function")
add = lambda x, y: x + y
print(add(3,4))
print()


# DEEP DIVE - 2: Micro-Challenge: The Mapper
print("DEEP DIVE - 2: Micro-Challenge: The Mapper")
nums = [1, 2, 3]
squared = list(map(lambda x: x**2, nums))
print(squared)
print()


# DEEP DIVE: 3 - Micro-Challenge: The Filter
print("DEEP DIVE: 3 - Micro-Challenge: The Filter")
nums = [1, 2, 3, 4, 5, 6]
positive_nums = list(filter(lambda x: x > 0, nums))
print(positive_nums)
print()


# DEEP DIVE: 4 - Micro-Challenge: The Reducer
print("DEEP DIVE: 4 - Micro-Challenge: The Reducer")
product = reduce(lambda x, y: x * y, [1, 2, 3, 4])
print(product)
print()



# DEEP DIVE: 5 - Micro-Challenge: The Custom Sort Key
print("DEEP DIVE: 5 - Micro-Challenge: The Custom Sort Key")
data = ["100px", "20px", "3px"]
data.sort(key=lambda x: int(x[:-2]))
print(data)



# DEEP DIVE: 6 - Micro-Challenge: The Zip Lock
print("DEEP DIVE: 6 - Micro-Challenge: The Zip Lock")
names = ["A", "B"]
ages = [20, 30]
combined = dict(zip(names, ages))
print(combined)



# Deep DIVE: 7 - Micro-Challenge: List Comprehension Speed
print("Deep DIVE: 7 - Micro-Challenge: List Comprehension Speed")
listx = list(range(1000000))
start_time = time.time()
squared = [x**2 for x in listx]
end_time = time.time()
print(f"List comprehension took {end_time - start_time:.4f} seconds")
print()



# DEEP DIVE: 8 - Micro-Challenge: Any & All
print("DEEP DIVE: 8 - Micro-Challenge: Any & All")
nums = [1, 2, -3]
has_negative = any(x < 0 for x in nums)
all_positive = all(x > 0 for x in nums)
print(f"Has negative: {has_negative}, All positive: {all_positive}")
print()



# DEEP DIVE: 9 - Micro-Challenge: Partial Functions
print("DEEP DIVE: 9 - Micro-Challenge: Partial Functions")
from functools import partial
def power(base, exp): return base ** exp
square = partial(power, exp=2)
print(f"Square of 5: {square(5)}")
print()




# DEEP DIVE: 10 - Micro-Challenge: The Immutability Test
print("DEEP DIVE: 10 - Micro-Challenge: The Immutability Test")
data = (1, 2, 3)
new_data = tuple(map(lambda x: x * 2, data))
print(new_data)
print()


print("Deep Dive Exercises for Day 11 are Finished.")