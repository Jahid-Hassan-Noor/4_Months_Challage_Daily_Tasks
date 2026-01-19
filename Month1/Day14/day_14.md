# Day 14: The Final Boss – Algorithmic Logic

## Theory: Algorithmic Thinking

Day 14 focuses on key algorithmic patterns that help solve common problems efficiently. Each capstone problem teaches a reusable logic technique rather than a one-off solution.

---

## DEEP DIVE - 14.1: Two Sum (O(N))

Given a list of numbers and a target, the goal is to find two numbers whose sum equals the target. A brute-force solution checks all pairs, but the efficient approach uses a dictionary to track numbers already seen. For each number, we calculate the difference from the target and check if it exists in the dictionary. This allows finding the pair in a single pass with O(N) complexity.

---

## DEEP DIVE - 14.2: Palindrome Check (Slicing)

To check if a string is a palindrome, we normalize it by removing spaces and converting to lowercase. Then we compare the string with its reverse using slicing (`s[::-1]`). This method is simple and readable, creating a reversed copy in memory while correctly handling spaces and cases.

---

## DEEP DIVE - 14.3: Anagrams (Frequency Counting)

An anagram has the same letters in a different order. To check this, we can either sort both strings and compare them, or count the frequency of each character using `collections.Counter`. Frequency counting is faster for longer strings, running in O(N), and ensures both strings contain exactly the same characters.

---

## DEEP DIVE - 14.4: Flattening a List (Recursion)

Nested lists can be flattened using recursion. For each element, if it is a list, we recursively flatten it; if not, we add it to the result. This approach handles lists of any depth naturally and keeps the logic clean and easy to understand.

---

## DEEP DIVE - 14.5: FizzBuzz (Logical Ordering)

FizzBuzz prints numbers 1–100 with multiples of 3 as "Fizz", multiples of 5 as "Buzz", and multiples of both as "FizzBuzz". The critical insight is that we must check divisibility by 15 first to correctly handle numbers divisible by both 3 and 5. Order matters to produce accurate output.

---

## DEEP DIVE - 14.6: Deduplication (O(N))

Removing duplicates while preserving order requires tracking which items have already been seen. Using a set for membership checks and a list for the result ensures each item appears only once and maintains the original sequence. Direct use of `set()` alone would destroy order.

---

## DEEP DIVE - 14.7: Binary Search (O(log N))

Binary search finds an element’s index in a sorted list by repeatedly dividing the search space in half. We check the middle element; if it is too small, we search the right half; if too large, the left half. This technique is much faster than scanning the list linearly, especially for large datasets.

---

## DEEP DIVE - 14.8: Missing Number (Math)

If a list of numbers from 1 to N is missing one number, we can calculate it without scanning the list. The expected sum is N×(N+1)/2. Subtracting the actual sum of the list from the expected sum directly gives the missing number in O(N) time and O(1) space.

---

## DEEP DIVE - 14.9: Grouping Data (Itertools)

To group a list of dictionaries by a key, the data must first be sorted by that key. Using `itertools.groupby`, we can then iterate through each group. This method ensures accurate grouping and is especially useful for categorizing data in reports or analytics.

---

## DEEP DIVE - 14.10: Merge Sorted Lists (Two Pointers)

Merging two sorted lists efficiently can be done with two pointers. We compare elements at both pointers, append the smaller one, and move that pointer forward. After one list is exhausted, we append the remaining elements from the other list. This logic underpins merge sort and other efficient merging algorithms.

---
