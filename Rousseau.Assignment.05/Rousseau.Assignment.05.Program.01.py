# Program #01:

# Using map, write a Python program to triple all numbers in a given list of integers.
# Console
# Original list: [1, 2, 3, 4, 5, 6, 7]
# Triple of said list numbers:
# [3, 6, 9, 12, 15, 18, 21]

def triple(num):
    return num * 3

def main():
    original_list =  [1, 2, 3, 4, 5, 6, 7]

    print(f"Original list: {original_list}\n")

    final_list = map(triple, original_list)

    print(f"Triple of said list numbers:\n{list(final_list)}")


if __name__ == "__main__":
    main()