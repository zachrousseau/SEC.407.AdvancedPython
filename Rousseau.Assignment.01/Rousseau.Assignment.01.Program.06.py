# Create a program that checks whether a number is a prime number and displays the total
# number of factors if it is not a prime number.

# Console Prime Number Checker
# Please enter an integer between 1 and 5000: 1
# Invalid integer. Please try again.
# Please enter an integer between 1 and 5000: 2
# 2 is a prime number.
# Try again? (y/n): y
# Please enter an integer between 1 and 5000: 3
# 3 is a prime number.
# Try again? (y/n): y
# Please enter an integer between 1 and 5000: 4
# 4 is NOT a prime number.
# It has 3 factors.
# Try again? (y/n): y
# Please enter an integer between 1 and 5000: 6
# 6 is NOT a prime number.
# It has 4 factors.
# Try again? (y/n): n
# Bye!

# Specifications
# • A prime number is only divisible by two factors (1 and itself). For example, 7 is a prime number
# because it is only divisible by 1 and 7.
# • If the number is not a prime number, the program should display its number of factors. For
# example, 6 has four factors (1, 2, 3, and 6).
# • Store the code that gets a valid integer for this program in its own function.
# • Store the code that calculates the number of factors for a number in its own function.
# • Store the rest of the code that gets input and displays output in the main() function. Divide this
# code into functions whenever you think it would make that code easier to read and maintain.

def valid_int(num):
    if(num > 1 and num < 5000):
        return True 

    return False

def factors(num):

    factor = num - 1 
    count = 0 

    while(factor != 1 ):

        if(num % factor == 0):
            count += 1

        factor -= 1

    return count 

def main():

    print("Prime Number Checker")

    again = str()
    
    while(again != "n"):

        num = int(input("Please enter an integer between 1 and 5000: "))

        if(valid_int(num) == False):
            print("Invalid Integer. Please try again.")
            continue

        factor = factors(num)

        if(factor == 0):
            print(f"{num} is a prime number.")
        else:
            print(f"{num} is NOT a prime number.")
            print(f"It has {factor} factor(s)")

        again = input("Try again? (y/n): ")

    print("Bye!")

if __name__ == "__main__":
    main()