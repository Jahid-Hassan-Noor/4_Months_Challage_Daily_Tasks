# Day - 9 - > DEEP DIVE: Theory: Infinite Memory (Generators)
print("Day 9: Deep Dive Exercises")

import time
import sys


print()
# DEEP DIVE - 1: Micro-Challenge: The Basic Yield
print("DEEP DIVE - 1: Micro-Challenge: The Basic Yield")

def gen():
    yield 1
    yield 2
    yield 3

for value in gen():
    print(value)
print()


# DEEP DIVE - 2: Micro-Challenge: The Memory Profile
print("DEEP DIVE - 2: Micro-Challenge: The Memory Profile")
list_comp = [x for x in range(1_000_000)]
gen_expr = (x for x in range(1_000_000))

print("List comprehension size:", sys.getsizeof(list_comp), "bytes")
print("Generator expression size:", sys.getsizeof(gen_expr), "bytes")
print()


# DEEP DIVE: 3 - Micro-Challenge: The Infinite Sequence
print("DEEP DIVE: 3 - Micro-Challenge: The Infinite Sequence")

def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

fib_gen = fibonacci()
for i in range(10):
    print(next(fib_gen))
print()


# DEEP DIVE: 4 - Micro-Challenge: The One-Time Trap
print("DEEP DIVE: 4 - Micro-Challenge: The One-Time Trap")
def simple_gen():
    yield 1
    yield 2
    yield 3

g = simple_gen()
print("First loop:")
for x in g:
    print(x)

print("Second loop (should print nothing):")
for x in g:
    print(x)
print()


# DEEP DIVE: 5 - Micro-Challenge: The Next Protocol
print("DEEP DIVE: 5 - Micro-Challenge: The Next Protocol")
g = (x for x in range(3))
print("Calling next(g) manually:")
try:
    print(next(g))
    print(next(g))
    print(next(g))
    print(next(g))
except StopIteration:
    print("StopIteration exception raised!")



# DEEP DIVE: 6 - Micro-Challenge: The Pipeline (Chaining)
print("DEEP DIVE: 6 - Micro-Challenge: The Pipeline (Chaining)")
def numbers(n):
    for i in range(n):
        yield i

def square(gen):
    for x in gen:
        yield x * x

def filter_even(gen):
    for x in gen:
        if x % 2 == 0:
            yield x

pipeline = filter_even(square(numbers(10)))

for value in pipeline:
    print(value)
print()



# DEEP DIVE: 7 - Micro-Challenge: The Large File Reader
print("DEEP DIVE: 7 - Micro-Challenge: The Large File Reader")
def fake_large_file(num_lines):
    for i in range(num_lines):
        yield f"Line {i}\n"

for line in fake_large_file(5):
    print(line.strip())
print()



# DEEP DIVE: 8 - Micro-Challenge: Yield Forom
print("DEEP DIVE: 8 - Micro-Challenge: Yield Forom")
def gen_a():
    yield 1
    yield 2

def gen_b():
    yield 3
    yield 4

def main_gen():
    yield from gen_a()
    yield from gen_b()

for value in main_gen():
    print(value)
print()



# DEEP DIVE: 9 - Micro-Challenge: The send() Method
print("DEEP DIVE: 9 - Micro-Challenge: The send() Method")
def receiver():
    total = 0
    while True:
        value = yield total
        if value is None:
            break
        total += value

gen = receiver()
print(next(gen))

print(gen.send(10))
print(gen.send(5))
print(gen.send(20))
print()


# DEEP DIVE: 10 - Micro-Challenge: State Retention (Running Average)
print("DEEP DIVE: 10 - Micro-Challenge: State Retention (Running Average)")
def running_average():
    total = 0
    count = 0
    while True:
        value = yield total / count if count else 0
        total += value
        count += 1

avg = running_average()
next(avg)

print(avg.send(10))
print(avg.send(20))
print(avg.send(30))
