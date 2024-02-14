# Program #02:

# Create an object-oriented program that uses a custom list object to automatically generate
# and work with a series of random integers.

# Console
# Random Integer List
# How many random integers should the list contain?: 12
# Random Integers
# ===============
# Integers: 17, 34, 34, 15, 71, 44, 97, 48, 19, 12, 83, 42
# Count: 12
# Total: 516
# Average: 43.0
# Continue? (y/n): y
# Random Integers
# ===============
# Integers: 52, 88, 10, 77, 56, 91, 17, 51, 22, 14, 48, 37
# Count: 12
# Total: 563
# Average: 46.917
# Continue? (y/n): n
# Bye!
# Specifications
# • Create a RandomIntList class that inherits the list class. This class should allow a programmer to
# create a list of random integers from 1 to 100 by writing a single line of code. For example, a
# programmer should be able to create a custom list that stores 12 random integers with this line
# of code:
# int_list = RandomIntList(12)
# • To do that, you can use the self keyword to access the list superclass like this:
# self.append(rand_int)
# • The RandomIntList class should contain methods or properties for getting the count, average, and
# total of the numbers in the list. In addition, it should contain a __str__ method for displaying a
# comma-separated list of integers as shown above.
# • The program should use the RandomIntList class to generate the list of random integers, display
# the list, and get the summary data (count, total, and average).
# • The program should make sure the integer entered by the user is valid. (15-4)

class RandomIntList(list):
    
    def __init__ (self, count):
        import random 

        while(count != 0):
            rand_int = random.randint(1, 100)

            self.append(rand_int)
            count = count - 1
    
    def count(self):
        return len(self)

    
    def total(self):
        total = 0
        for num in self:
            total += num

        return total


    def average(self):
        return self.total() / self.count()


    def __str__(self):
        return str((super().__str__()))[1:-1]
        


def display_rand_list(rand_list):
    print("\nRandom Integers")
    print("================")
    print(f"Integers: {rand_list}")
    print(f"Count: {rand_list.count()}")
    print(f"Total: {rand_list.total()}")
    print(f"Average: {rand_list.average()}")


    
def again():
    while(True):
        again = str(input("Continue? (y/n): "))

        match again: 
            case "y":
                generate_rand_list()
            case "n":
                print("Bye!")
                exit()
            case _:
                print("Invalid Entry")
                continue



def generate_rand_list():

    count = 0
    try:
        count = int(input("\nHow many random integers should the list contain?: "))
    except KeyboardInterrupt:
        exit()
    except:
        print("Invalid Entry, input must be an integer")
        generate_rand_list()

    if validate_pos_int(count) == False:
        print("Invalid Entry, integer must be positive")
        generate_rand_list()

    rand_list = RandomIntList(count)


    display_rand_list(rand_list)
    again()


def validate_pos_int(num):
    if(num < 1):
        return False


def main():
    print("\nRandom Integer List")
    
    generate_rand_list()
    


if __name__ == "__main__":
    main()