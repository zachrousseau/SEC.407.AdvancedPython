# Program #03:

# Write a Python program to find the largest digit and smallest digit in the input number.

# Console

# Enter a Digit: 3567890
# Original Number: 3567890
# Largest Digit of the said number: 9
# Smallest Digit of the said number: 0
# Try another number? (y/n) y
# Enter a Digit: 435
# Original Number: 435
# Largest Digit of the said number: 5
# Smallest Digit of the said number: 3
# Try another number? (y/n) n
# Bye!

def find_min_max(num):

    max_digit = int()
    min_digit = 10


    while(num // 10 != 0):
        
        digit = num % 10 

        min_digit = min(digit, min_digit)
        max_digit = max(digit, max_digit)
        
        num = num // 10 

    min_digit = min(num, min_digit)
    max_digit = max(num, max_digit)

    return min_digit, max_digit

def main():

    again = "y"

    while(again == "y"):

        num = int(input("Enter a Digit: "))
        print(f"Original Number: {num}")

        min_digit, max_digit = find_min_max(num)

        print(f"Largest Digit of the said number: {max_digit}")
        print(f"Smallest Digit of the said number: {min_digit}")

        again = input("Try another number? (y/n)")

    

if __name__ == "__main__": 
    main()