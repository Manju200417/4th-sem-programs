# Program to check if a number is prime
num = int(input("Enter a number: "))

# Prime number is greater than 1
if num > 1:
    is_prime = True
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break

    print(f"{num} is a prime number." if is_prime else f"{num} is not a prime number.")

else:
    print(num, "is not a prime number.")