# Phone Number Finder in Python

## Overview

This is a simple Python script that does two things:

1. Checks if a given text matches the format of a phone number.
2. Scans a larger text to find phone numbers that match this format.

The phone number format we are looking for is:

```
XXX-XXX-XXXX
```

where `X` is a digit (0-9) and dashes `-` separate the groups.

---

## Code Breakdown

### **Part 1: Checking If a String is a Phone Number**

The function `is_phone_number(text)` checks whether a given string follows the expected phone number pattern.

```python
def is_phone_number(text):
    if len(text) != 12:
        return False
    for i in range(0,3):
        if not text[i].isdecimal():
            return False
    if text[3] != '-':
        return False
    for i in range(4,7):
        if not text[i].isdecimal():
            return False
    if text[7] != '-':
        return False
    for i in range(8,12):
        if not text[i].isdecimal():
            return False
    return True
```

#### **Step-by-Step Explanation:**

1. **Check Length:** If `text` is not exactly 12 characters long, return `False`. A valid phone number must be 12 characters (10 digits + 2 dashes).
2. **Validate First Three Digits:** Loop through the first three characters (`text[0:3]`) and check if they are digits.
3. **Check First Dash:** Ensure `text[3]` is a dash (`-`). If not, return `False`.
4. **Validate Second Three Digits:** Loop through `text[4:7]` and check if they are digits.
5. **Check Second Dash:** Ensure `text[7]` is a dash (`-`). If not, return `False`.
6. **Validate Last Four Digits:** Loop through `text[8:12]` and check if they are digits.
7. **If all checks pass, return `True`.**

#### **Testing the Function:**

```python
print('Is 415-555-4242 a phone number?')
print(is_phone_number('415-555-4242'))   # Expected: True

print('Is shark shark a phone number?')
print(is_phone_number('shark shark'))      # Expected: False
```

---

### **Part 2: Finding Phone Numbers in a Larger Text**

Now, we want to **search for phone numbers** inside a larger text.

```python
message = 'Call me at 415-555-1011 tomorrow. 415-555-9999 is my office.'
for i in range(len(message)):
    chunk = message[i:i+12]
    if is_phone_number(chunk):
        print(f'Phone number found: {chunk}')
print('Done')
```

#### **Step-by-Step Explanation:**

1. **Define a text message** (`message`) that contains phone numbers. But note that this text can come from a user, an API, a form, or a database. This text can be a string of any length, no matter what. It can be thousands of characters long. While the phone number follows the same pattern we want, it works.
2. **Loop through each character in `message`** to extract a 12-character chunk at each step.
   - Example: `message[i:i+12]` extracts `message[0:12]`, `message[1:13]`, and so on.
3. **Check if the chunk is a valid phone number** using `is_phone_number(chunk)`.
4. **Print the phone number if found**.
5. **Continue the loop until the end of the message**.
6. **Print 'Done'** when all numbers have been found.

#### **How This Works Iteratively:**

- First iteration: `chunk = message[0:12]` → "Call me at 4" → Not a number.
- Second iteration: `chunk = message[1:13]` → "all me at 41" → Not a number.
- …
- Eventually: `chunk = message[11:23]` → "415-555-1011" → Valid number → Print it.
- The loop continues, finds `415-555-9999`, and prints it as well.

#### **Expected Output:**

```
Phone number found: 415-555-1011
Phone number found: 415-555-9999
Done
```

---

## **Key Takeaways**

- The function `is_phone_number()` checks if a given string follows the `XXX-XXX-XXXX` format.
- We use `len()` to iterate through a larger string and extract 12-character chunks to find phone numbers.
- The script **does not use regular expressions**, making it a **basic but clear** implementation of pattern matching.

This is a **simple but effective approach** to detecting phone numbers in a text without using regex.
