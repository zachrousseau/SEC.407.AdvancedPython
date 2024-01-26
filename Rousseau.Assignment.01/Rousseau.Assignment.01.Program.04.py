# Program #04:
# Create a program that uses a separate module to calculate sales tax and total after tax.

# Console Sales Tax Calculator
# ENTER ITEMS (ENTER 0 TO END)
# Cost of item: 35.99
# Cost of item: 27.50
# Cost of item: 19.59
# Cost of item: 0
# Total: 83.08
# Sales tax: 4.98
# Total after tax: 88.06
# Again? (y/n): y
# ENTER ITEMS (ENTER 0 TO END)
# Cost of item: 152.50
# Cost of item: 59.80
# Cost of item: 0
# Total: 212.3
# Sales tax: 12.74
# Total after tax: 225.04
# Again? (y/n): n
# Thanks, bye!

# Specifications
# • The sales tax rate should be 6% of the total.
# • Store the sales tax rate in a module. This module should also contain functions that calculate the
# sales tax and the total after tax. These functions should round the results to a maximum of two
# decimal places.
# • Store the code that gets input and displays output in the main() function. Divide this code into
# functions whenever you think it would make that code easier to read and maintain.
# • Assume the user will enter valid data.

def main():
    import tax

    print("Sales Tax Calculator")
    

    run = ""
    
    while(run != "n"):
        print("ENTER ITEMS (ENTER 0 TO END)")

        total = int()

        while(True):
            cost =  float(input("Cost of Item: "))

            if(cost == 0):
                break

            total = total + cost

        
        print(f"Total: {round(total, 2)}")

        sales_tax = tax.sales_tax(total)
        after_tax = tax.after_tax(total)

        print(f"Sales tax: {sales_tax}")
        print(f"Total: {after_tax}")
        
        run = input("Again? (y/n): ")

    print("Thanks, bye!")

if __name__ == "__main__":
    main()