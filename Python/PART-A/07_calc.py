ch = input("Select operation:\n1. Add\n2. Subtract\n3. Multiply\n4. Divide\n5. Modulus\n6. Floor Division\nEnter choice: ")
a, b = float(input("Enter first number: ")), float(input("Enter second number: "))

if ch == '1':
    print(f"Result: {a + b}")
elif ch == '2':
    print(f"Result: {a - b}")
elif ch == '3':
    print(f"Result: {a * b}")
elif ch == '4':
    print(f"Result: {a / b}")
elif ch == '5':
    print(f"Result: {a % b}")
elif ch == '6':
    print(f"Result: {a // b}")
else:
    print("Invalid input")