"""
Python Strings: Indexing, Slicing, Concatenation, Splitting & Trimming
----------------------------------------------------------------------
Key Takeaways:
1. Indexing (`str[1]`): Strings are zero-indexed arrays of characters.
2. Slicing (`str[start:end]`): Extracts a substring from `start` up to
   (but NOT including) `end`.
3. Concatenation (`+`): Joins two or more strings together.
4. Membership Check (`in`): Returns `True` if a substring exists inside another string.
5. Splitting (`.split(delimiter)`): Breaks a string into a `list` based on a separator.
6. Trimming Whitespace:
   - `.strip()`  -> removes leading and trailing spaces
   - `.lstrip()` -> removes leading (left) spaces only
   - `.rstrip()` -> removes trailing (right) spaces only
"""

str = "vijayantgaikwad.com"

str1 = "roche employee"

str2 = "vijayantgaikwad"

print(str[1])

print(str[0:5])  # Substring

print(str + str1)  # Concatenation

print(str2 in str)  # Substring check

var = str.split(".")
print(var)  # Splitting of string


str3 = " great "
print(str3.strip())
print(str3.lstrip())
print(str3.rstrip())