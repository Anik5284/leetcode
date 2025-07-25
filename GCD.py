def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# Take input from the user
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

result = gcd(num1, num2)
print(f"The GCD of {num1} and {num2} is {result}")
