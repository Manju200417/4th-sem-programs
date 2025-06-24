s = "hello world"

print("Length of the string:", len(s))            # Get the length of the string
print("Lowercase:", s.lower())                    # Convert string to lowercase
print("Uppercase:", s.upper())                    # Convert string to uppercase
print("Capitalized:", s.capitalize())             # Capitalize the first character
print("Is alphabetic?:", s.isalpha())             # Check if all characters are alphabets
print("Is digit?:", s.isdigit())                  # Check if all characters are digits
print("Title case:", s.title())                   # Convert string to title case
print("Is alphanumeric?:", s.isalnum())           # Check if all characters are alphabets or digits
print("Sliced (index 0 to 4):", s[:5])            # Get first 5 characters
print("Sliced (from index 6 to 10):", s[6:11])    # Get characters from index 6 to 10