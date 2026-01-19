# Day 13 -> DEEP DIVE: Persistence (Files & Contexts)
print("Day 13: Deep Dive Exercises")
print()

import json
import csv
import pickle
from pathlib import Path
import time


BASE_DIR = Path("Month1") / "Day13"
BASE_DIR.mkdir(parents=True, exist_ok=True)


# DEEP DIVE - 1: Micro-Challenge: The Safe Open
print("DEEP DIVE - 1: The Safe Open")

with open(BASE_DIR / "safe_open.txt", "w", encoding="utf-8") as f:
    f.write("This file was written safely.\n")
print("File written and automatically closed.")
print()



# DEEP DIVE - 2: Micro-Challenge: Append vs Write
print("DEEP DIVE - 2: Append vs Write")

with open(BASE_DIR / "log.txt", "w", encoding="utf-8") as f:
    f.write("Log start\n")

with open(BASE_DIR / "log.txt", "a", encoding="utf-8") as f:
    f.write("New log entry added\n")

print("Log updated without deleting old content.")
print()



# DEEP DIVE - 3: Micro-Challenge: Binary Mode
print("DEEP DIVE - 3: Binary Mode")

with open(BASE_DIR / "binary_example.bin", "wb") as f:
    f.write(b"\x00\x01\x02\x03")
with open(BASE_DIR / "binary_example.bin", "rb") as f:
    data = f.read()
print("Binary data read:", data)
print()



# DEEP DIVE - 4: Micro-Challenge: Encoding Hell
print("DEEP DIVE - 4: Encoding Hell")

text = "Hello, I am doing Unicode test"
with open(BASE_DIR / "unicode.txt", "w", encoding="utf-8") as f:
    f.write(text)
with open(BASE_DIR / "unicode.txt", "r", encoding="utf-8") as f:
    content = f.read()
print("File content:", content)
print()




# DEEP DIVE - 5: Micro-Challenge: JSON Serialization
print("DEEP DIVE - 5: JSON Serialization")

user_data = {
    "id": 1,
    "name": "Jahid",
    "active": True
}
with open(BASE_DIR / "user.json", "w", encoding="utf-8") as f:
    json.dump(user_data, f)
print("Dictionary saved as JSON.")
print()




# DEEP DIVE - 6: Micro-Challenge: CSV Parsing
print("DEEP DIVE - 6: CSV Parsing")

with open(BASE_DIR / "users.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["id", "name", "age"])
    writer.writerow([1, "Jahid", 22])
    writer.writerow([2, "Muzahid", 21])
users = []
with open(BASE_DIR / "users.csv", "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        users.append(row)
print("CSV loaded as list of dictionaries:")
print(users)
print()




# DEEP DIVE - 7: Micro-Challenge: Buffering
print("DEEP DIVE - 7: Buffering")

with open(BASE_DIR / "big_file.txt", "w", encoding="utf-8") as f:
    for i in range(10000):
        f.write(f"Line {i}\n")
print("Large file written efficiently using buffering.")
print()




# DEEP DIVE - 8: Micro-Challenge: Pathlib
print("DEEP DIVE - 8: Pathlib")


folder = Path(BASE_DIR / "data")
folder.mkdir(exist_ok=True)
file_path = folder / "info.txt"
with open(file_path, "w", encoding="utf-8") as f:
    f.write("Pathlib handled this path safely.")
print("File created using pathlib:", file_path)
print()



# DEEP DIVE - 9: Micro-Challenge: Custom Context Manager
print("DEEP DIVE - 9: Custom Context Manager")

class Timer:
    def __enter__(self):
        self.start = time.time()
        return self
    def __exit__(self, exc_type, exc_value, traceback):
        end = time.time()
        print("Time taken:", end - self.start, "seconds")
with Timer():
    time.sleep(1)
print()


# DEEP DIVE - 10: Micro-Challenge: Pickle (The Warning)
print("DEEP DIVE - 10: Pickle (The Warning)")

class User:
    def __init__(self, name):
        self.name = name
user = User("Jahid")
with open(BASE_DIR / "user.pkl", "wb") as f:
    pickle.dump(user, f)
with open(BASE_DIR / "user.pkl", "rb") as f:
    loaded_user = pickle.load(f)
print("Unpickled user name:", loaded_user.name)
print()




print("Deep Dive Exercises for Day 13 are Finished.")
print()
