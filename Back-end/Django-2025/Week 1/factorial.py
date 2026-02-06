num=float(input("enter a number:"))

try:
    if num<0:
        raise ValueError("Negative number")
except ValueError as ve:
    print("is negative numbers.")
    exit()

def factorial(num):
   if num==0 or num==1:
       return 1
   else:
       return num*factorial(num-1)
print(f"the factorial is {factorial(num)}")
