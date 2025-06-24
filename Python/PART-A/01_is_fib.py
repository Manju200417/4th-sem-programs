n = int(input("Enter a number: "))  
a, b = 0, 1  
while a < n:  
    a, b = b, a + b #assign respectively 
print("Given number is a Fibonacci number." if a == n else "Given number is NOT a Fibonacci number.")