
# checks input is a number more than zero
def num_check(question):

    valid = False
    while not valid:

        error = "please insert a number that is more than zero."

        try:

            response = float(input(question))
            if response > 0:
                return response

            else:
                print(error)
                print()

        except ValueError:
            print(error)

# Main routine goes here
# Introduction / heading print statements

print()
print("**** Area Perimiter Calculator")
print()

# Start of calculator loop

keep_going = ""
while keep_going == "":

    width = num_check("Width: ")
    height = num_check("Height: ")

    # calculate area and perimeter
    area = width * height
    perimeter = 2 * (width + height)

    # output area and perimeter
    print("perimeter: {:.2f} units" .format(perimeter))
    print("area: {:.2f} square units" .format(area))
    print()

    keep_going = input("Press <enter> to keep going or any key to quit: ")

print()
print("thanks for using my area/perimeter calculator")