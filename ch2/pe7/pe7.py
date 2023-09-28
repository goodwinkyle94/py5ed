# MPG = Miles driven / Gallons of gas used
# get number of miles driven
# get gallons of gas used
# calculate and display the result


def main():
    user_input = get_user_input()
    mpg = calculate_mpg(user_input)
    display_result(mpg)


def get_user_input():
    user_input = []
    while True:
        try:
            miles = float(input('How many miles did you drive? '))
            break
        except Exception as err:
            print(err)
    while True:
        try:
            gallons = float(input("How many gallons of gas did you use? "))
            break
        except Exception as err:
            print(err)
    user_input.append(miles)
    user_input.append(gallons)
    return user_input


def calculate_mpg(user_input):
    mpg = user_input[0] / user_input[1]
    return mpg


def display_result(mpg):
    print(" -------------------------------")
    print(f" Your fuel economy is: {mpg:,.2f} mpg")
    print(" -------------------------------")


if __name__ == "__main__":
    while True:
        main()
        input("Press ENTER to run again or CTRL + Z to exit.")
