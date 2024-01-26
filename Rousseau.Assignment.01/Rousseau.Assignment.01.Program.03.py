# Program #03:

# Create a program that uses a separate module to convert feet to meters and vice versa.

# Console
# Feet and Meters Converter
# Conversions Menu:
# a. Feet to Meters
# b. Meters to Feet
# Select a conversion (a/b): a
# Enter feet: 100
# 30.48 meters
# Would you like to perform another conversion? (y/n): y
# Conversions Menu:
# a. Feet to Meters
# b. Meters to Feet
# Select a conversion (a/b): b
# Enter meters: 100
# 328.08 feet
# Would you like to perform another conversion? (y/n): n
# Thanks, bye!
# Specifications
# • The formula for converting feet to meters is:
# feet = meters / 0.3048
# • The formula for converting meters to feet is:
# meters = feet * 0.3048
# • Store the code that performs the feet to meters and meters to feet conversions in functions
# within a module.
# • Store the code that displays the title in its own function, and store the code that displays the
# menu in its own function, but store the rest of the code that gets input and displays output in the
# main() function.
# • Assume the user will enter valid data.
# • The program should round results to a maximum of two decimal places.


def display_tile():
    print("Feet and Meters Converter")

def display_menu():
    print("Conversions Menu: \n a. Feet to Meters \n b. Meters to Feet")


def main():
    import unit_conversion

    display_tile()
    display_menu()

    run = ""

    while(run != "n"):
        conversion_type = input("Select a conversion (a/b): ")

        if(conversion_type == "a"):
            feet = input("Enter feet: ")
            conversion = unit_conversion.feet_to_meters(feet)
        elif(conversion_type == "b"):
            meters = input("Enter meters: ")
            conversion = unit_conversion.meters_to_feet(meters)
        else:
            print("Invalid Response")

        print(conversion)

        run = input("Would you like to perform another conversion? (y/n): ")

    print("Thanks, bye!")

if __name__ == "__main__":
    main()