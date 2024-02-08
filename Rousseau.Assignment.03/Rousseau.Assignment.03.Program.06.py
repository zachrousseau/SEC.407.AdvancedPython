# Program #06:
# Write a Python program that inputs unsorted string and returns a string sorted alphabetically by
# the first character of each word. Notice the input string has mixed words that start with lower
# and upper characters.

# Console
# Original Word:
# "red Green black White Pink"
# Sorted Word Based On Its First Character:
# "black Green Pink red White"
# Original Word:
# "I am enjoying my Cybersecurity courses at RWU so much"
# Sorted Word Based On Its First Character:
# "am at Cybersecurity courses enjoying I my much RWU so"
# Specifications

# • Note that that sorted() function sorts according to ASCII code order not alphabetically

def sort_word(word):
    return " ".join(sorted((word.lower()).split(" ")))

def main():

    original_word = "I am enjoying my Cybersecurity courses at RWU so much"
    
    sorted_word = sort_word(original_word)

    print(f"Original Word:\n{original_word}")
    print(f"Sorted Word Based on Its First Character:\n{sorted_word}")

if __name__ == "__main__":
    main()