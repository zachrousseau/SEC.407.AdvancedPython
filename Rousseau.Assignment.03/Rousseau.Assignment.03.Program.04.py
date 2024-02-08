# Program #04:
# You are provided a list of tuples, write a Python program to convert it to a list of sorted lists.
# [(14, 12), (24, 73, 59), (43, 4), (23, 33, 94, 12)]

# Console

# Original list of tuples:
# [(14, 12), (24, 73, 59), (43, 4), (23, 33, 94, 12)]
# Convert to a list of lists:
# [[12, 14], [24, 59, 73], [4, 43], [12, 23, 33, 94]]
# Specifications
# • Use a list comprehension to convert a tuple to a list.
# • Used sorted() function
# • Use list() function


def main():
    original_list = [(14, 12), (24, 73, 59), (43, 4), (23, 33, 94, 12)]

    final_list = []

    for original_tuple in original_list:
        final_list.append(sorted(list(original_tuple)))
    
    print(f"Original list of tuples: \n{original_list}")
    print(f"Convert to a list of lsits: \n{final_list}")

if __name__ == "__main__":
    main()
