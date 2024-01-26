# Program #02:

# Create a program that converts the number of miles that you walked on a hike to the
# number of feet that you walked.

# Console
# Hike Calculator
# How many miles did you walk?: 4.5
# You walked 23760 feet

# Specifications
# • The program should accept a float value for the number of miles.
# • Store the code that displays the title in a separate function.
# • Store the code that converts miles to feet in a separate function. This function should return an
# int value for the number of feet.
# • There are 5280 feet in a mile.
# • Store the code that gets user input and displays output in the main() function.
# • Assume that the user will enter a valid number of miles

def miles_to_feet(miles):
    return int((miles*5280))


def display_title():
    print("Hike Calculator")


def main():
    
    display_title()

    miles = float(input("How many miles did you walk?: "))

    feet = miles_to_feet(miles)

    print(f"You walked {feet} feet.")

if __name__ == "__main__":
    main()