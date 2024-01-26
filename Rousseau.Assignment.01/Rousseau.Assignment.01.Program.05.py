# The program should roll two six-sided dice.
# • Store the code that rolls a single die in a function.
# • Store the code that gets input and displays output in the main() function. Divide this code into
# functions whenever you think it would make that code easier to read and maintain.
# • The program should display a special message for two ones (snake eyes) and two sixes (boxcars).

def roll_die():
    import random

    return random.randint(1, 6)

def main():

    print("Dice Roller")
    

    roll = input("Roll the dice? (y/n): ")

    while(roll == "y"):

        die1 = roll_die()
        die2 = roll_die()
        total = die1 + die2

        print(f"Die 1: {die1}")
        print(f"Die 2: {die2}")

        if(total == 2):
            print("Snake eyes!")
        if(total == 12):
            print("Boxcars!")

        roll = input("Roll again? (y/n): ")


if __name__ == "__main__":
    main()