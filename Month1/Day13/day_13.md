# Day 13: Deep Dive Exercises

## Theory: Persistence (Files & Contexts)

---

## DEEP DIVE - 1: The Safe Open
When working with files, forgetting to close them can cause data loss or corruption. Python solves this problem using the `with open(...) as f` structure. This is called a **context manager**. It guarantees that the file is closed automatically when the block finishes, even if the program crashes due to an error.

---

## DEEP DIVE - 2: Append vs Write
Files support different modes depending on how we want to use them. Write mode (`w`) clears the file before writing new data, which can destroy old information. Append mode (`a`) safely adds new content to the end of the file without deleting anything. Exclusive mode (`x`) prevents overwriting by failing if the file already exists.

---

## DEEP DIVE - 3: Binary Mode
Not all files are made of readable text. Images, videos, PDFs, and executables store raw bytes. Binary mode (`rb` or `wb`) allows Python to read and write these bytes directly. Using text mode on binary files can corrupt the data because Python tries to decode bytes into characters.

---

## DEEP DIVE - 4: Encoding Hell
Text files are stored as bytes and must be decoded into characters. If Python uses the wrong encoding, it raises a `UnicodeDecodeError`. This issue is common on Windows systems that default to `cp1252`. By explicitly using `encoding="utf-8"`, Python can safely handle emojis and international characters.

---

## DEEP DIVE - 5: JSON Serialization
Serialization is the process of converting data into a format that can be saved or shared. JSON is the most widely used format for this purpose. When Python saves a dictionary as JSON, it converts it into plain text. JSON only supports string keys, so non-string keys are automatically converted.

---

## DEEP DIVE - 6: CSV Parsing
CSV files may look simple, but they can contain commas and quoted values that break manual parsing. Using `csv.DictReader` allows Python to correctly read each row as a dictionary. Column headers become keys, making the data easier to understand and safer to process.

---

## DEEP DIVE - 7: Buffering
Writing data directly to disk is slow, so Python uses **buffering** to improve performance. Data is first stored in memory and written to disk in large chunks instead of line by line. This reduces disk usage and makes programs much faster when handling large files.

---

## DEEP DIVE - 8: Pathlib
Different operating systems use different file path separators. Manually combining paths with strings can cause bugs. The `pathlib` module handles paths correctly across Windows, macOS, and Linux. It makes file handling safer, cleaner, and more readable.

---

## DEEP DIVE - 9: Custom Context Manager
Context managers are not limited to files. By implementing `__enter__` and `__exit__`, we can define our own managed blocks. This allows automatic setup and cleanup. A timer context manager is a good example, as it measures execution time without extra code.

---

## DEEP DIVE - 10: Pickle (The Warning)
Pickle allows Python to save and restore entire objects exactly as they are. While powerful, it is dangerous because loading a pickle file can execute hidden code. For security reasons, pickle should only be used with trusted data and never with files from unknown sources.

---
