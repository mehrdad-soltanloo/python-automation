import re
import os

def scan_log_file():
    """Scans a log file for a user-specified keyword (INFO, WARNING, ERROR) and saves results."""
    # Ask for user inputs
    employee_name = input("What is your name? ").strip()
    log_path = input("Enter the log file path: ").strip()
    keyword = input("What type of log you are searching for (INFO, WARNING, or ERROR)? ").upper()

    # Greet the user
    print(f"\nHello {employee_name.title()}! Searching for '{keyword}' logs in '{log_path}'...\n")

    try:
        with open(log_path, "r", encoding="utf-8") as file:  # Fixed formatting
            found = False
            match_count = 0
            matched_lines = []

            for line in file:
                if re.search(keyword, line, re.IGNORECASE):
                    if not found:
                        print("-" * 80)  # Prints separator **before the first match**

                    print(f"Found {keyword} in log: {line.strip()}")

                    found = True
                    match_count += 1
                    matched_lines.append(line)
            # Create "logs" folder **before checking if matches were found**
            os.makedirs("logs", exist_ok=True)
        

            if found:
                print("-" * 80)  # Now correctly placed inside `if found` block
                print(f"\nTotal '{keyword}' occurrences found: {match_count}")

               

                # Ensure UTF-8 encoding when saving results
                with open("logs/filtered_logs.txt", "w", encoding="utf-8") as output_file:
                    output_file.writelines(matched_lines)

                print("\nResults saved to 'logs/filtered_logs.txt'. Check for full results.")    
            else:
                print(f"\nNo '{keyword}' logs were found in the file.")

    except FileNotFoundError:
        print(f"\nError: The file '{log_path}' was not found.")
        print("Make sure the file exists and the path is correct.")
    except PermissionError:
        print(f"\nError: You don't have permission to read '{log_path}'. Try running as administrator.")
    except UnicodeDecodeError:
        print(f"\nError: The file '{log_path}' contains characters that can't be read with UTF-8 encoding.")
    except Exception as e:
        print(f"\nAn unexpected error occurred: {type(e).__name__}: {e}")  # Added `type(e).__name__` for better debugging

# Run the function
scan_log_file()
