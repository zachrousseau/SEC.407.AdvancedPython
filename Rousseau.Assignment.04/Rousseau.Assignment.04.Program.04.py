# Program #04:
# Create an object-oriented program that reads a list of Customer objects from a CSV file
# and allows the user to display the data for a customer by specifying the customer’s ID.

# Console

# Customer Viewer
# Enter customer ID: 103
# Art Venere
# 8 W Cerritos Ave #54
# Bridgeport, NJ 08014
# Continue? (y/n): y
# Enter customer ID: 104
# Lenna Paprocki
# Feltz Printing
# 639 Main St
# Anchorage, AK 99501
# Continue? (y/n): y
# Enter customer ID: 99
# No customer with that ID.
# Continue? (y/n): n
# Bye!
# Specifications
# • Use a CSV file named customers.csv that contains customer data.
# • Use a Customer class to store the customer data. This class should include these attributes: id,
# firstName, lastName, company, address, city, state, zip.
# • In addition, this class should include a property or method that returns the full name and the full
# address. The address should have two lines if the company attribute is empty or three lines if the
# company attribute is not empty.
# • Create a function that reads the customer data from the CSV file and creates Customer objects
# from it.
# • To find the customer with the specified ID, you need to loop through each Customer object in the
# list of Customer objects and check whether the specified ID matches the ID stored in the
# Customer object.
# • If the specified ID isn’t found, display an appropriate message. (14-3)

class Customer():

    def __init__(self, customer_id, first_name, last_name, company, address, city, state, zip_code):
        self.customer_id = customer_id
        self.first_name = first_name
        self.last_name = last_name
        self.company = company
        self.address = address
        self.city = city
        self.state = state  
        self.zip_code = zip_code

    def get_full_name(self):
        return self.first_name + " " + self.last_name
    
    def get_full_address(self):

        line1 = self.address + "\n"
        line2 = self.city + " " + self.state + " " + self.zip_code + "\n"
        
        if(self.company != ''):
            company = self.company + "\n"
            return company + line1 + line2
        
        return line1 + line2
    
    def id(self):
        return self.customer_id
    
    def __str__(self):
        full_name = self.get_full_name()
        full_address = self.get_full_address()

        return "\n" + full_name + "\n" + full_address




def load_customers(file_path):
    import csv

    customer_list = []

    with open(file_path, newline='') as csvfile:
        customers = csv.reader(csvfile)
        next(customers, None) # Skip header


        for cust_id, first_name, last_name, company_name, address, city, state, zip in customers:
            customer_list.append(Customer(cust_id, first_name, last_name, company_name, address, city, state, zip))

    return customer_list

def get_customer_id(customer_list):

    customer_id = input("Enter customer ID: ")

    for customer in customer_list:
        if(customer.id() == customer_id):
            return customer.__str__()

    return "No customer with that ID."


def again(customer_list):
    while(True):
        again = str(input("Continue? (y/n): "))

        match again: 
            case "y":
                print(get_customer_id(customer_list))
            case "n":
                print("Come back soon!")
                exit()
            case _:
                print("Invalid Entry")
                continue

def main():
    import os 


    script_directory = os.path.dirname(os.path.abspath(__file__))
    file_path = script_directory + "\\" + "customers.csv"

    print("Customer Viewer")

    customer_list = load_customers(file_path)
    print(get_customer_id(customer_list))
    again(customer_list)


if __name__ == "__main__":
    main()


