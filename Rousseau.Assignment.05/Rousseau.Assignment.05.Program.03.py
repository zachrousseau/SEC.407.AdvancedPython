# Program #03:

# Write a Python program to find numbers divisible by fifteen or thirteen from a list of numbers using
# Lambda and filter function.
# Console
# Orginal list:
# [19, 65, 57, 39, 45, 152, 639, 121, 44, 90, 190, 200, 26, 130]
# Numbers of the above list divisible by nineteen or thirteen:
# [65, 39, 45, 90, 26, 130]
# Specifications
# • User filter function. 


def main():
    original_list = [19, 65, 57, 39, 45, 152, 639, 121, 44, 90, 190, 200, 26, 130]

    divisible_by_13_or_15 = lambda num: num % 15 == 0 or num % 13 == 0
    filtered_list = list(filter(divisible_by_13_or_15, original_list))

    print(f"Numbers of the above list divisible by nineteen or thirteen:\n{filtered_list}")

if __name__ == "__main__":
    main()