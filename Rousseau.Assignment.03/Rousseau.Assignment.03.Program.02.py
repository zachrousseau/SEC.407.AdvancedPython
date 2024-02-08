# Program #02:

# Write a Python program to find the students with the maximum and minimum ages in a
# dictionary.

# Console
# Original dictionary elements:
# {'Chris': 18, 'Nicole': 32, 'Doug': 22, 'Betty': 45, 'David':
# 33, 'Lilah': 20}
# Maximum Age is for Betty which is 45
# Minimum Age is for Chris which is 18
# Specifications
# • Use max() and min() with key=<dict_name>.get


def get_dict_max(dict):
    max_name = max(dict, key=dict.get)
    max_age = dict[max_name]

    return max_name, max_age

def get_dict_min(dict):
    min_name = min(dict, key=dict.get)
    min_age = dict[min_name]

    return min_name, min_age

def main():
    dict = {'Chris': 18, 'Nicole': 32, 'Doug': 22, 'Betty': 45, 'David':33, 'Lilah': 20}

    max_name, max_age = get_dict_max(dict)
    min_name, min_age = get_dict_min(dict)

    print(f"Maximum Age is For {max_name} which is {max_age}")
    print(f"Minimum Age is For {min_name} which is {min_age}")

if __name__ == "__main__":
    main()