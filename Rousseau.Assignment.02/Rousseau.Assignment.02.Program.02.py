# Program #02:

# Write a Python program that takes a positive integer and returns the sum of the cube of all
# positive integers smaller than the entered number.

# Console
# Enter a Positive Number: 3
# Sum of cubes smaller than the specified number: 9
# Specifications
# • EX. If n = 5 the sum will be 4^3 + 3^3 + 2^3 + 1^3 = 100

def validate_entry(num):
    if(num > 0):
        return True
    return False

def main():
    num = int(input("Enter a Positive number: "))

    if(validate_entry(num) != True):
        print("Invalid entry")
        exit()

    num = num - 1
    result = 0 
    while(num > 0):
        result = result + pow(num, 3)
        num -= 1

    print(f"Sum of cubes smaller than the specified number: {result}")

if __name__ == "__main__":
    main()