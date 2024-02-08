# Program #01:

# Write a Python program to get every 2nd, 3rd, and 4th element in a list.

# Console:
# Here is the full list: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Numbers every 2 [2, 4, 6, 8, 10]
# Numbers every 3 [3, 6, 9]
# Numbers every 4 [4, 8]

# Specifications
# • You can create any list such as [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# • Use list slicing to return elements. Make sure you select proper [star:end:step]

def nth_element(list, n):
    return list[n-1:len(list):n]

def main ():
    list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    print(f"Here is the full list: {list}")
    print(f"Numbers every 2 {nth_element(list, 2)}")
    print(f"Numbers every 3 {nth_element(list, 3)}")
    print(f"Numbers every 2 {nth_element(list, 4)}")

if __name__ == "__main__":
    main()