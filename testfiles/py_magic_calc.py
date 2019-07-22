import re

print("Welcome to the Python Magical Calculator")
print(" Anytime you are done enter 'quit' \n")

run = True
previous = 0

def perform_calc():
    global run
    global previous


    #calculation = eval()

    if previous == 0:
        calculation = input("Enter the numbers and the arguments :")
    else:
        calculation = input(str(previous))

    if calculation == ("quit"):
        run = False
        print("Last value is :", previous)
        print("Thank you for using the calculator")
    else:
        calculation = re.sub('[a-zA-Z.,:;()!@" "]', '', calculation)

        if previous == 0:
            previous = eval(calculation)
            print("You have entered the following argument : ", calculation, "and the result is --", previous)
        else:
            previous = eval(str(previous) + calculation)

while run:
    perform_calc()

