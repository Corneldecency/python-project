# Building a simple Calculator

# Addition
def add(x, y):
    return x + y

# Subtraction
def subtract(x, y):
    return x - y

# Multiplication
def multiply(x, y):
    return x * y

# Division
def divide(x, y):
    if y == 0:
        return "Error: Cannot divide by zero"
    return x / y

# Choose operation:
print("Select operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

# keep asking until a valid operation is entered
while True:
    operation = input("Enter choice (1/2/3/4): ").strip()
    if operation in ('1', '2', '3', '4'):
        break
    print("Invalid choice. Please select a valid operation.")


# Enter first number:
num1 = float(input("Enter first number: "))

# Enter second number:
num2 = float(input("Enter second number: "))

# Perform calculation
if operation == '1':
    print(f"Result: {add(num1, num2)}")
elif operation == '2':
    print(f"Result: {subtract(num1, num2)}")
elif operation == '3':
    print(f"Result: {multiply(num1, num2)}")
elif operation == '4':
    print(f"Result: {divide(num1, num2)}")
else:
    print("Invalid choice")
