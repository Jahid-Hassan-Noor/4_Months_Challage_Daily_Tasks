# Day - 5 - > DEEP DIVE: Theory: Hash Tables
print("Day 5: Deep Dive Exercises")

# DEEP DIVE - 1: Micro-Challenge: The Speed Trap (Lookup)
print("DEEP DIVE - 1: Micro-Challenge: The Speed Trap (Lookup)")

numbers_list = list(range(1000000))
numbers_set = set(numbers_list)
if -1 in numbers_list:
	print("-1 is in the list!")
else:
	print("-1 is NOT in the list.")

if -1 in numbers_set:
	print("-1 is in the set!")
else:
	print("-1 is NOT in the set.")

print("Why is set faster than list?")
print("If you search in a list, Python checks every number one by one. This can be slow if the list is big.")
print("If you search in a set, Python can jump straight to the answer. This is much faster!")





# DEEP DIVE - 2: Micro-Challenge: The Safe Vault
print("\nDEEP DIVE - 2: Micro-Challenge: The Safe Vault")

user = {"id": 1}
email = user.get("email")
print("User email:", email)
email = user.get("email", "No email found")
print("User email (with default):", email)




# DEEP DIVE - 3: Micro-Challenge: The Frequency Counter
print("\nDEEP DIVE - 3: Micro-Challenge: The Frequency Counter")

word = "banana"
letter_count = {}

for letter in word:
	if letter in letter_count:
		letter_count[letter] += 1
	else:
		letter_count[letter] = 1

print("Letter counts:", letter_count)




# DEEP DIVE - 4: Micro-Challenge: The Database Merger
print("\nDEEP DIVE - 4: Micro-Challenge: The Database Merger")


# Using update() to merge dictionaries
defaults = {"theme": "light", "audio": "on"}
user_pref = {"theme": "dark"}

# Make a copy so we don't change the original defaults
merged_settings = defaults.copy()
merged_settings.update(user_pref)
print("Default settings:", defaults)
print("Merged settings:", merged_settings)

print()
print("All Deep Dive programs for day 5 are complete.")
