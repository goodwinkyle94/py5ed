#A customer in a store is purchasing five items. Write a program that asks for the price of each item, then
#displays the subtotal of the sale, the amount of sales tax, and the total.
#Assume the sales tax is 7 percent
import time

def main():
    
    price_of_items = get_price()
    recepit(price_of_items)

def get_price():
    
    price_of_items = []

    for i in range(5):
        while True:
            try:
                price = float(input(f'What is the price of item #{i + 1}: $'))
            except Exception as err:
                print(f'***{err}***\n***NO COMMAS***')
            else:
                break
        price_of_items.append(price)
    return price_of_items


def recepit(self):
        
    for element in self:
        print(f"${element:,.2f}")
        time.sleep(.075)

if __name__ == '__main__':

    main()

