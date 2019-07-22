# Writing a simple program for Python Calculator

def add_function(a , b):
    add_num = a + b
    return add_num

def sub_function(a , b):
    if (a > b):
        sub_num = a - b
    else:
        sub_num = b - a
    return sub_num

def multiply_function(a , b):
    product_num = a * b
    return product_num

def div_function(a , b):
    div_num = a / b
    return div_num

print (" Enter the operation that you want to calculate")
print (" 1: For Addition")
print (" 2: For Subtraction")
print (" 3: For Multiplication")
print (" 4: For Division")

opt_choice = int(input("Enter option as 1, 2, 3 or 4"))

num1 = int(input("Enter the First Number:  "))
num2 = int(input("Enter the Second Number: "))

if opt_choice == 1:
    result = add_function(num1, num2)
elif opt_choice == 2:
    result = sub_function(num1, num2)
elif opt_choice == 3:
    result = multiply_function(num1, num2)
elif opt_choice == 4:
    result = div_function(num1, num2)
else:
    print("Please enter a valid choice (1, 2, 3, or 4) for calculator operation")

print("The result from the operation is", result)