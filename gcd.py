def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# Numbers to find GCD for
num1 = 48
num2 = 18

# Calculate and display the GCD
result = gcd(num1, num2)
print(f"The GCD of {num1} and {num2} is: {result}")
