print("Hi Shishupal")

if (5 == 5):
    print('True')
else:
    print('False')

if 5 is 5:
    print ('String is true')
else:
    print('String is False')

#testing with a user defined function

def my_first_function():
    print("Testing the fuNCTION")

my_first_function()


def my_second_function(str1, str2):
    print(str1)
    print(str2)

my_second_function("Test the first string", " Test the Second string")

def my_third_function(*folks):
    for folk in folks:
        print (" The person name is ", folk)

my_third_function("Shanaya", "Rudrakshi", "Ruchita", " Santosh", "Shishupal")

def my_fourth_function(num1, num2, num3):
    return (num1 * num3 + num2)

num4 = my_fourth_function(4,2,6)
print()