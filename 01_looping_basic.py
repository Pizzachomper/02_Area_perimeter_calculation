valid = False
while not valid:

    response = float(input("Enter a number: "))
    if response > 0:
        valid = True

    else:
        print("please insert a number that is more than zero")
        print()