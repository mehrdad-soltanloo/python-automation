# Simple Log Scanner

## Project Overview

This project is a simple file scanner that scans and prints specified logs based on user input. It allows users to specify keywords (e.g., `INFO`, `WARNING`, `ERROR`) and efficiently extracts matching lines from a log file. The extracted results are also saved to a new log file for later reference.

---

## Code Breakdown

### **1. Import Required Modules**

```python
import re
import os
```

**Why?**

- `re`: Required for pattern matching using regular expressions.
- `os`: Needed to handle file paths and create directories if necessary.

---

### **2. Define the Function**

```python
def scan_log_file():
    """Scans a log file for a user-specified keyword (INFO, WARNING, ERROR) and saves results."""
```

**Why?**

- Using a function makes the code reusable and modular.
- The docstring explains the function's purpose.

---

### **3. Get User Input**

```python
    employee_name = input("What is your name? ").strip()
    log_path = input("Enter the log file path: ").strip()
    keyword = input("What type of log you are searching for (INFO, WARNING, or ERROR)? ").upper()
```

**Why?**

- `.strip()` removes unnecessary spaces that users might enter.
- `.upper()` ensures uniform case for matching (avoiding case-sensitive issues).

---

### **4. Greet the User**

```python
    print(f"\nHello {employee_name.title()}! Searching for '{keyword}' logs in '{log_path}'...\n")
```

**Why?**

- `.title()` ensures proper capitalization of names.
- `f-string` provides a user-friendly message.

---

### **5. Open Log File with Exception Handling**

```python
    try:
        with open(log_path, "r", encoding="utf-8") as file:
```

**Why?**

- `try:` prevents script crashes if the file is missing or unreadable.
- `"r"` mode ensures we are reading the file.
- `encoding="utf-8"` ensures compatibility with different character sets.

---

### **6. Initialize Tracking Variables**

```python
            found = False
            match_count = 0
            matched_lines = []
```

**Why?**

- `found = False`: Tracks whether at least one match exists.
- `match_count = 0`: Counts occurrences of the keyword.
- `matched_lines = []`: Stores matched lines for later saving.

---

### **7. Process File Line by Line**

```python
            for line in file:
                if re.search(keyword, line, re.IGNORECASE):
```

**Why?**

- Reading line by line is **memory efficient**, avoiding unnecessary large file loads.
- `re.search()` performs a case-insensitive search.

---

### **8. Print Matches and Store Results**

```python
                    if not found:
                        print("-" * 80)  # Prints separator before the first match

                    print(f"Found {keyword} in log: {line.strip()}")
                    found = True
                    match_count += 1
                    matched_lines.append(line)
```

**Why?**

- `if not found:` ensures the separator prints **only once** before the first match.
- `.strip()` removes trailing spaces for cleaner output.
- `found = True`: Marks that at least one match was found.
- `match_count += 1`: Tracks the number of matches.
- `matched_lines.append(line)`: Stores results for later saving.

---

### **9. Create Logs Folder**

```python
            os.makedirs("logs", exist_ok=True)
```

**Why?**

- Ensures the "logs" folder exists before saving results.
- `exist_ok=True`: Prevents `FileExistsError` if the folder already exists.

---

### **10. Display Summary & Save Results**

```python
            if found:
                print("-" * 80)
                print(f"\nTotal '{keyword}' occurrences found: {match_count}")

                with open("logs/filtered_logs.txt", "w", encoding="utf-8") as output_file:
                    output_file.writelines(matched_lines)

                print("\nResults saved to 'logs/filtered_logs.txt'. Check for full results.")
```

**Why?**

- The summary prints **only if at least one match was found**.
- `open("logs/filtered_logs.txt", "w", encoding="utf-8")` ensures results are saved with proper encoding.
- `.writelines(matched_lines)`: Writes all matched lines efficiently.

---

### **11. Handle Case When No Matches Are Found**

```python
            else:
                print(f"\nNo '{keyword}' logs were found in the file.")
```

**Why?**

- Provides feedback to the user if no matches are found.
- Prevents confusion when the script runs but finds nothing.

---

### **12. Exception Handling**

```python
    except FileNotFoundError:
        print(f"\nError: The file '{log_path}' was not found.")
        print("Make sure the file exists and the path is correct.")
    except PermissionError:
        print(f"\nError: You don't have permission to read '{log_path}'. Try running as administrator.")
    except UnicodeDecodeError:
        print(f"\nError: The file '{log_path}' contains characters that can't be read with UTF-8 encoding.")
    except Exception as e:
        print(f"\nAn unexpected error occurred: {type(e).__name__}: {e}")
```

**Why?**

- **`FileNotFoundError`**: Handles cases where the user enters an invalid file path.
- **`PermissionError`**: Warns users if they lack permission to read the file.
- **`UnicodeDecodeError`**: Prevents crashes due to incompatible character encoding.
- **Generic `Exception`**: Ensures all other unexpected errors are handled and displayed clearly.

---

### **13. Execute the Function**

```python
scan_log_file()
```

**Why?**

- This ensures the function runs when the script is executed.
- Without this, the script would do nothing.

---

## **Final Thoughts**

This script efficiently scans a log file, extracts relevant entries, and saves them for later review. The design ensures:

- **Efficiency**: Reads one line at a time (scalable for large logs).
- **Robustness**: Exception handling prevents crashes.
- **User-friendliness**: Clear prompts and error messages.
- **Data Preservation**: Saves results for future analysis.

This script can be further extended to:

1. **Support multiple keyword searches (e.g., `ERROR|WARNING`)**.
2. **Highlight matches using color libraries like `colorama`**.
3. **Filter logs by specific date ranges**.

---

## **Usage Instructions**

1. Run the script in a Python environment.
2. Enter your name, log file path, and the keyword to search for.
3. Review the output on the console or check `logs/filtered_logs.txt` for saved results.
