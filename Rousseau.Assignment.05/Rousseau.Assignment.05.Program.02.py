# Program #02:

# Using map function, write a Python program to convert all the characters into uppercase and lowercase
# and eliminate duplicate letters from a given sequence.
# Console
# Original Characters:
#  {'b', 'D', 'o', 'g', 'U', 'a', 'i'}
# After converting above characters in upper and lower cases
# and eliminating duplicate letters:
# {('O', 'o'), ('I', 'i'), ('U', 'u'), ('B', 'b'), ('A', 'a'), ('G', 'g'), ('D', 'd')}
# Specifications
# • Write your own function that change cases and returns the upper and low case of the letter. Note
# that if a function returns multiple values, then it returns a tuple.
# • You can define a set to hold the original characters. Note that set will have only unique values. 

# def upper_lower(char):

#     lower = char.lower()
#     upper = char.upper()

#     return upper, lower

def test(string):
    return (string.lower(), string.upper())

def main():

    original_set =  {'b', 'D', 'o', 'g', 'U', 'a', 'i', 'I'}
    print(f"Original Characters:\n{original_set}\n")

    final_set = set(map(test, original_set))

    print("After converting above characters in upper and lower cases and eliminating duplicate letters: ")
    print(f"{final_set}")


if __name__ == "__main__":
    main()