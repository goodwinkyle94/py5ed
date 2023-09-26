#get purchase
#compute country and satate sales tax
#sate tax = 5% and county sales tax is 2.5 percent
#should display subtotal, sate sales tax, county sales tax and total
import time, sys

SALES_TAX_RATES = (.025, .05) # county and state tax rate

def main():

    purchase = get_purchase()
    sales_taxes = calculate_sales_tax(purchase)
    display_recipt(purchase, sales_taxes)

def get_purchase():

    while True:
        try:
            purchase = float(input('What was the cost of your purchase? $'))
            return purchase
        except Exception as err:
            print(err)
   
def calculate_sales_tax(purchase):

    sales_taxes = []

    for element in SALES_TAX_RATES:
        product = purchase * element
        sales_taxes.append(product)

    return sales_taxes

def display_recipt(purchase, sales_taxes):

    cool_lines()
    print(f"Purchase: ${purchase:,.2f}")
    print(f"County Sales Tax: ${sales_taxes[0]:,.2f}")
    print(f"State Sales Tax: ${sales_taxes[1]:,.2f}")
    print(f"Tax Total: ${sum(sales_taxes):,.2f}")
    total_cost = purchase + sum(sales_taxes)
    print(f"Total Sale: ${total_cost:,.2f}")
    cool_lines()

def cool_lines():

    for i in range(27):
        time.sleep(.01)
        sys.stdout.write('-')
        sys.stdout.flush()
    print("")

if __name__ == '__main__':

    while True:
        main()
        input("Press enter to continue or CTRL + Z to exit.")

