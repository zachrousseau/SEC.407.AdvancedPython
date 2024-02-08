# Program #05:
# Use a map() function to convert a list of color tuples to a list of strings.

# Console

# Original list of tuples:
# [('red', 'green'), ('pink', 'black'), ('orange', 'blue')]
# Convert to a list of strings:
# ['red green', 'pink black', 'orange blue']
# Specifications
# • Use map() function
# • Use join()' to concatenate elements within each tuple using a space as a separator
# • Convert the map object to a list

def tuple_to_string(original_tuple):
    return " ".join(original_tuple)

def main():
    original_list = [('red', 'green'), ('pink', 'black'), ('orange', 'blue')]

    print(f"{list(map(tuple_to_string, original_list))}")


if __name__ == "__main__":
    main()