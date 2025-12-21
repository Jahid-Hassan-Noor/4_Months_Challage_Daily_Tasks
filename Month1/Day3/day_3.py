print("Day 3: Deep Dive Exercises")


# DEEP DIVE - 1: Theory: The Iterator Protocol
print("DEEP DIVE - 1: Theory: The Iterator Protocol")
print("This 1st program will continue asking for your password until you enter \"stop\".")
while True:
    user_pass = input("Enter your password (or type 'stop' to end): ")
    if user_pass == "stop":
        print("1st Program is stopping.")
        break
    else:
        print("The password you entered:", user_pass)




# DEEP DIVE - 2: Micro-Challenge: The Accumulator Pattern
print("DEEP DIVE - 2: Micro-Challenge: The Accumulator Pattern")
total = 0
range_limit = int(input("Enter the range of numbers to sum: "))
for num in range(range_limit + 1):
    total += num
print("The total sum from 0 to", range_limit, "is:", total)
print("2nd Program is complete.")



# DEEP DIVE - 3: Micro-Challenge: The Efficient Skipper
print("DEEP DIVE - 3: Micro-Challenge: The Efficient Skipper")
for num in range(1, 10):
    if num == 5:
        continue
    print(num)
print("3rd Program is complete.")




# DEEP DIVE - 4: Micro-Challenge: The String Walker
print("DEEP DIVE - 4: Micro-Challenge: The String Walker")
word = "DATA"
for char in word:
    print(char)
print("4th Program is complete.")



print("All Deep Dive programs for day 3 are complete.")
