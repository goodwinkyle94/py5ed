# Write a program that displays the following information:
# Your name
# Your address,wth city, state, and zip
# your telephone number
# your college major

# main function takes input from first function and passes-
# it as an argument to the second
def main():
    user_info = get_user_info()
    display_info(user_info)


# promts user for input and stores it in a list
def get_user_info():
    user_info = ['']
    name = input("What is your name? ")
    street_address = input('What is your street address? ')
    city = input('What is your city? ')
    state = input('What is your state? ')
    zipcode = input('What is your zip? ')
    telephone_number = input("What is your phone number? ")
    college_major = input("What is your major? ")
    user_info.append(name)
    user_info.append(street_address)
    user_info.append(city)
    user_info.append(state)
    user_info.append(zipcode)
    user_info.append(telephone_number)
    user_info.append(college_major)
    return user_info


# for loop itertes over the list and prints it to the screen
def display_info(user_info):
    print('-----INFORMATION YOU ENTERED-----')
    for data in user_info:
        print(f'{data}')


if __name__ == '__main__':
    main()
