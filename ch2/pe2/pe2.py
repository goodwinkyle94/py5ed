#sales prediction

#Profit Margin constant
PROFIT_MARGIN = .23

#main function
def main():

    user_input = get_user_input()
    display_projected_sales(user_input)

#get user input
def get_user_input():

    while True:
        try:
            user_input = float(input("What is the total annual sales? $"))
        except Exception as err:
            print(f'{err}\n No commas or $')
        else:
            return user_input

def display_projected_sales(user_input):
    
    print(f'The total estimated profit is ${PROFIT_MARGIN * user_input:.2f}')

if __name__ == '__main__':
    main()
