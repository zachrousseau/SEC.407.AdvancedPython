# Program #06:
# Create a program that a user can use to manage the primary email address and phone number
# for a contact.

# Console
# Contact Manager
# COMMAND MENU
# list - Display all contacts
# view - View a contact
# add - Add a contact
# del - Delete a contact
# exit - Exit program
# Command: list
# 1. Guido van Rossum
# 2. Eric Idle
# Command: view
# Number: 2
# Name: Eric Idle
# Email: eric@ericidle.com
# Phone: +44 20 7946 0958
# Command: add
# Name: Mike Murach
# Email: mike@murach.com
# Phone: 559-123-4567
# Mike Murach was added.
# Command: del
# Number: 1
# Guido van Rossum was deleted.
# Command: list
# 1. Eric Idle
# 2. Mike Murach
# Command: exit
# Bye!

contacts = [["Name", "Email", "Phone"], ["Guido van Rossum", "guio@guido.com", "991"], ["Eric Idle", "eric@ericidle.com", "+44 20 7946 0958"]]


def list_contacts():
    
    global contacts 

    contact_list = contacts[1:]

    count = 1

    for contact in contact_list:
        print(str(count) + ". " + contact[0])
        count += 1 

    command_menu()

def view_contacts():
    global contacts

    contact_number = int(input("Number: "))

    print( (contacts[0])[0] + ": " + (contacts[contact_number])[0])
    print( (contacts[0])[1] + ": " + (contacts[contact_number])[1])
    print( (contacts[0])[2] + ": " + (contacts[contact_number])[2])

    command_menu()

def add_contacts():
    global contacts 

    name = input("Name: ")
    email = input("Email: ")
    phone = input ("Phone: ")

    contact = [name, email, phone]

    contacts.append(contact)

    command_menu()

def del_contacts():

    global contacts
    contact_number = int(input("Number: "))

    if(contact_number > 0 and contact_number < len(contacts)):
        del contacts[contact_number]

    command_menu()

def exit_contacts():
    print("Bye!")
    exit()

def command_menu():
    print("\nCOMMAND MENU")
    print("list - Display all contacts")
    print("view - View a contact")
    print("add - Add a contact")
    print("del - Delete a contact")
    print("exit - Exit program")
    command = ((input("Command: ")).lower()).strip()

    match command:
        case "list":
            list_contacts()
        case "view":
            view_contacts()
        case "add":
            add_contacts()
        case "del":
            del_contacts()
        case "exit":
            exit_contacts()
        case _:
            print("Invalid option, please select an option from the menu")
            command_menu()



def main():
    print("Contact Manager")
    command_menu()  



if __name__ == "__main__":
    main()