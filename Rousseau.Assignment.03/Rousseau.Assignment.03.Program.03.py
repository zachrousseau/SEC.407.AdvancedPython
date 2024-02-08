# Program #03:

# You have a list of dictionaries that include information about students. Write a Python program
# that displays all the values for each key as a list. Here is the dictionary:
# students = [
#  {'Name': 'Doug', 'Age': 18},
#  {'Name': 'Mathew', 'Age': 22},
#  {'Name': 'Roxanne', 'Age': 20},
#  {'Name': 'Jane', 'Age': 18}
# ]

# Console

# Original list of dictionaries:
# [{'Name': 'Doug', 'Age': 18}, {'Name': 'Mathew', 'Age': 22},
# {'Name': 'Roxanne', 'Age': 20}, {'Name': 'Jane', 'Age': 18}]
# Here are the values of the "Name" key: ['Doug', 'Mathew',
# 'Roxanne', 'Jane']
# Here are the values of the "Age" key: [18, 22, 20, 18]
# Specifications
# • Use a list comprehension to extract the value associated with the specified 'key' from
# each dictionary.

def get_dict_keys(list, key):

    values = []
    
    for dict in list:
        values.append(dict[key])

    return values

def main():
    list = students = [
        {'Name': 'Doug', 'Age': 18},
        {'Name': 'Mathew', 'Age': 22},
        {'Name': 'Roxanne', 'Age': 20},
        {'Name': 'Jane', 'Age': 18}
    ] 

    print(f" Here are the values of the \"Name\" key: {get_dict_keys(list, 'Name')}")
    print(f" Here are the values of the \"Age\" key: {get_dict_keys(list, 'Age')}")


if __name__ == "__main__":
    main()