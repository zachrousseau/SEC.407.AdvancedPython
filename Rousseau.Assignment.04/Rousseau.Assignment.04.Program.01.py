# Program #01:
# Create an object-oriented program that allows you to enter data for customers and
# employees.

# Console:

# Customer/Employee Data Entry
# Customer or employee? (c/e): c
# DATA ENTRY
# First name: Frank
# Last name: Wilson
# Email: frank44@gmail.com
# Number: M10293
# CUSTOMER
# Name: Frank Wilson
# Email: frank44@gmail.com
# Number: M10293
# Continue? (y/n): y
# Customer or employee? (c/e): e
# DATA ENTRY
# First name: joel
# Last name: murach
# Email: joel@murach.com
# SSN: 123-45-6789
# EMPLOYEE
# Name: Joel Murach
# Email: joel@murach.com
# SSN: 123-45-6789
# Continue? (y/n): n
# Bye!

# Specifications
# • Create a Person class that provides attributes for first name, last name, and email address. This
# class should provide a property or method that returns the person’s full name.
# • Create a Customer class that inherits the Person class. This class should add an attribute for a
# customer number.
# • Create an Employee class that inherits the Person class. This class should add an attribute for a
# social security number (SSN).
# • The program should create a Customer or Employee object from the data entered by the user,
# and it should use this object to display the data to the user. To do that, the program can use the
# isinstance() function to check whether an object is a Customer or Employee object. (15-3)

class Person:

    def __init__(self, first_name, last_name, email):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email

    def get_full_name(self):
        return self.first_name + " " + self.last_name
    

    def __str__(self):
        return f"\nName: {self.get_full_name()}\nEmail: {self.email}\n"


class Customer(Person):
    
    def __init__(self, customer_number, first_name, last_name, email):
        super().__init__(first_name, last_name, email)
        self.customer_number = customer_number

    def __str__(self):
        header = "\nCUSTOMER"
        body = super().__str__()
        number = f"{self.customer_number}"

        return header + body + number


class Employee(Person):

    def __init__(self, ssn, first_name, last_name, email):
        super().__init__(first_name, last_name, email)
        self.ssn = ssn

    def __str__(self):
        header = "\nEMPLOYEE"
        body = super().__str__()
        ssn = f"{self.ssn}"
        
        return header + body + ssn


def data_entry():
    person_type = input("Customer or emplyee? (c/e): ")

    first_name = str(input("First name: "))
    last_name = str(input("Last name: "))
    email = str(input("Email: "))

    match person_type:
        case "c":
            customer_number = str(input("Number: "))
            person = Customer(customer_number=customer_number, first_name=first_name, last_name=last_name, email=email)
        case "e":
            ssn = str(input("SSN: "))
            person = Employee(ssn=ssn, first_name=first_name, last_name=last_name, email=email)
        case _:
            person = Person(first_name=first_name, last_name=last_name, email=email)


    print(person)

    again()


def again():
    while(True):
        again = str(input("Continue? (y/n): "))

        match again: 
            case "y":
                data_entry()
            case "n":
                print("Bye!")
                exit()
            case _:
                print("Invalid Entry")
                continue


def main():
    print("Customer/Employee Data Entry")

    data_entry()


if __name__ == "__main__":
    main()