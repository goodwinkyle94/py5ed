#assuming there are no accidents or delays, the distance that a car travles down interstate
#can be calculated with the following formula:
#distance = speed * time
#a car is traveling at 70 mph. Write a program thatr displays the following:
#The distnace the car will travel in 6 hours
#The distance thew car will travel in 10 hours
#the distance the car will travel in 15 hours
TIME_IN_HOURS = [6, 10, 15]

def main():

    velocity = get_car_velocity()
    displacement = calculate_displacement(velocity)
    display_displacement(displacement)

def get_car_velocity():

    while True:
        try:
            car_velocity = float(input("What is the car's velocity in MPH? "))
            break
        except Exception as err:
            print(f'---{err}---')
        
    return car_velocity
        

def calculate_displacement(self):

    print('Calculating displacement')
    displacement_list = []
    for element in TIME_IN_HOURS:
        displacement = self * element
        displacement_list.append(displacement)
    return displacement_list

def display_displacement(self):

    time_counter = 0

    for element in self:
        print(f'The displacment for {TIME_IN_HOURS[time_counter]} hours is {element:,.2f} miles')
        time_counter += 1

if __name__ == '__main__':

    while True:
        main()
        input('Press enter to run again or CTRL + Z to exit.')
