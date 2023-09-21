#one acres is 43560 sq ft write a program that asks the user to enter the total square feet in a tract of land
#and calculates the number of acres in the tract
import time, sys
def main(): 

    square_footage = get_user_input()
    acres = calculate_acres(square_footage)
    display_data(acres)

def get_user_input():
    while True: 
        try:
            square_footage = float(input('What is the land\'s square footage? '))
        except Exception as err:
            print(err)
        else:
            return square_footage

def calculate_acres(self):
    
    SQUARE_FEET_IN_ONE_ACRE = 43560
    acres = self/SQUARE_FEET_IN_ONE_ACRE

    return acres

def display_data(self):

    display_info = f'That is {self:.3f} acre(s).'

    for elemnet in display_info:
        sys.stdout.write(elemnet)
        sys.stdout.flush()
        time.sleep(.075)

if __name__ == '__main__':
    
    while True:
        print('\nPress "CTRL + Z" to exit')
        main()
        input('\nPress enter to run program again.')

