# Program #04:
# Write a Python program to find the common string at the end of two given words.

# Console

# Enter the first String: loving
# Enter the second String: living
# Original strings: loving living
# Common ending between said two strings: ving
# Try again? (y/n) y
# Enter the first String: Hello
# Enter the second String: hello
# Original strings: Hello hello
# Common ending between said two strings: ello
# Try again? (y/n) y
# Enter the first String: Bye
# Enter the second String: Hello
# Original strings: Bye Hello
# Common ending between said two strings:
# Try again? (y/n) n
# Bye!

def common_ending(str1, str2):

    while(len(str1) > 0):

        if(str2.endswith(str1)):
            return str1
        str1 = str1[1:]

    return ""

def main():

    again = "y"

    while(again == "y"):
        str1 = input("Enter the first String: ") 
        str2 = input("Enter the second String: ")

        print(f"Original strings: {str1}  {str2}")

        ending = common_ending(str1, str2)
        print(f"Common ending between said two strings: {ending}")

        again = input("Try again? (y/n) ")

    print("Bye!")

if __name__ == "__main__":
    main()