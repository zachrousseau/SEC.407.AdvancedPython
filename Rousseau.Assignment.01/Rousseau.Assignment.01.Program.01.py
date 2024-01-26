# Program #01:

# Create a program that checks whether a number is even or odd.

# Console:
# Even or Odd Checker
# Enter an integer: 33
# This is an odd number.

# Specifications
# • Store the code that gets user input and displays output in the main() function.
# • Store the code that checks whether the number is even or odd in a separate function.
# • Assume that the user will enter a valid integer.

def even_or_odd(num):

    if(num%2 == 0):
        return "This is an Even Number"
    else:
        return "This is an Odd Number"


def main():
    print("Even or Odd Checker")

    num = int(input("Enter an integer: "))

    print(even_or_odd(num))

if __name__ == "__main__":
    main()