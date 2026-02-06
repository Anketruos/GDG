
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

def add(num1, num2):
    return num1 + num2
def subtract(num1, num2):
    return num1 - num2
def multiply(num1, num2):
    return num1 * num2
def divide(num1, num2):
    if num2 != 0:
        return num1 / num2
    else:
        return "Error! Division by zero."
    
print("Select operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
operation = input("Enter operation (1/2/3/4): ")


if operation == '1':
    print(f"The result is : {add(num1, num2)}")
elif operation =='2':
    print(f"The result is : {subtract(num1, num2)}")
elif operation =='3':
    print(f"The result is : {multiply(num1, num2)}")
elif operation =='4':
    print(f"the result is:{ divide(num1 , num2)}")

else:
    print("Invalid operation selected.")



