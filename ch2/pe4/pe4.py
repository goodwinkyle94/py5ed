#A customer in a store is purchasing five items. Write a program that asks for the price of each item, then
#displays the subtotal of the sale, the amount of sales tax, and the total.
#Assume the sales tax is 7 percent
import time, sys

def main():
    
    price_of_items = get_price()
    sub_total = calculate_sub_total(price_of_items)
    sales_tax = calculate_sales_tax(price_of_items)
    total = calculate_total(sub_total, sales_tax)
    recepit(sub_total, sales_tax, total)

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

def calculate_sales_tax(self):

    SALES_TAX_RATE = .07
    sales_tax = SALES_TAX_RATE * sum(self)
    
    return sales_tax

def calculate_sub_total(self):

    sub_total = sum(self)

    return sub_total

def calculate_total(sub_total, sales_tax):

    total = sub_total + sales_tax

    return total

def cool_lines():

    for i in range(27):
        time.sleep(.01)
        sys.stdout.write('-')
        sys.stdout.flush()
        
def recepit(sub_total, sales_tax, total):

    
    cool_lines()

    time.sleep(.075)    
    print(f'\nSUB TOTAL: ${sub_total:,.2f}')
    time.sleep(.075)
    print(f'SALES TAX: ${sales_tax:,.2f}')
    time.sleep(.075)
    print(f'TOTAL: ${total:,.2f}')

    cool_lines()
    print('')

if __name__ == '__main__':

    main()

