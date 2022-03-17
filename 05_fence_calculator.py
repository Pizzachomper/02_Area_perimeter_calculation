
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
print("**** Fence cost calculator ****")
print()

# Start of calculator loop

keep_going = ""
while keep_going == "":

    width = num_check("Width: ")
    length = num_check("Length: ")
    cost_per_m = num_check ("Cost per meter: ")

    # calculate area and perimeter
    area = width * length
    perimeter = 2 * (width + length)
    cost_per_m = cost_per_m * perimeter

    # output area and perimeter
    print("Perimeter: {:.2f} units" .format(perimeter))
    print("Total cost: ${:.2f}" .format(cost_per_m))
    print()

    keep_going = input("Press <enter> to keep going or any key to quit: ")

print()
print("Thanks for using my fence cost calculator")