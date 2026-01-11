# Day 8: Deep Dive Exercises

# DEEP DIVE - 1: Micro-Challenge: The Linear Scan (O(N))
In the linear scan challenge, we check if -5 is present in a list of one million numbers. This operation requires examining each element one by one, resulting in a time complexity of O(N). For very large lists, this approach is slow because every element must be checked until the target is found or the list ends.



# DEEP DIVE - 2: Micro-Challenge: The Hash Lookup (O(1))
For the hash lookup challenge, we check if -5 is in a set containing one million numbers. Sets in Python use hash tables, so checking for membership is much faster, with an average time complexity of O(1). This makes sets ideal for fast lookups compared to lists.



# DEEP DIVE - 3: Micro-Challenge: The Insertion Trap (O(N))
In the insertion trap challenge, we append and insert elements into a list. Appending to the end of a list is efficient at O(1), but inserting at the beginning is costly at O(N) because all existing elements must be shifted to make room for the new one.



# DEEP DIVE - 4: Micro-Challenge: The Queue Bottleneck (Pop)
The queue bottleneck challenge demonstrates popping elements from both the end and the start of a list. Popping from the end is fast at O(1), but popping from the start is slow at O(N) since all remaining elements need to be shifted forward.




# DEEP DIVE - 5: Micro-Challenge: The String Builder (O(N^2) )
The string builder challenge involves building a string by repeatedly concatenating in a loop. Each concatenation creates a new string, so the total time is O(N^2). For efficiency, it is better to use the join method to combine strings in Python.



# DEEP DIVE - 6: Micro-Challenge: The Lenght Trick (O(1))
In the length trick challenge, we get the length of a list with one billion elements. This operation is O(1) because Python stores the length as an attribute, making it instantly accessible regardless of the list size.



# DEEP DIVE - 7: Micro-Challenge: The Quadratic Nested Loop (O(N^2))
The quadratic nested loop challenge uses two nested loops, each running n times, resulting in n squared total operations. This is an O(N^2) operation, which grows very quickly as n increases and is much slower than linear time for large n.



# DEEP DIVE - 8: Micro-Challenge: The Sorting Cost (O(N log N))
The sorting cost challenge sorts a random list using Python’s built-in sorted function. Python uses Timsort, which has a time complexity of O(N log N). Sorting is much faster than quadratic time but still slower than linear time, and should not be done inside loops.



# DEEP DIVE - 9: Micro-Challenge: The Dictionary Creator (O(1))
In the dictionary creator challenge, we build a dictionary from one million key-value pairs and then search for a key. Building the dictionary is O(N) because each item must be hashed and stored, but searching for a key is O(1) on average due to the hash table structure.



# DEEP DIVE - 10: Micro-Challenge: The Slice Copy (O(k))
The slice copy challenge slices the first 5,000 elements from a list of ten million. Slicing allocates new memory and copies references for each element in the slice, so the time taken is proportional to the slice size, or O(k), where k is the number of elements copied.
