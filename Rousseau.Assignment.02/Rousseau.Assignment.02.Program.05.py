# Program #05:
# Add exception handling to a Tip Calculator program.

# Console

# Tip Calculator
# INPUT
# Cost of meal: ten
# Must be valid decimal number. Please try again.
# Cost of meal: -10
# Must be greater than 0. Please try again.
# Cost of meal: 52.31
# Tip percent: 17.5
# Must be valid integer. Please try again.
# Tip percent: 20
# OUTPUT
# Cost of meal: 52.31
# Tip percent: 20%
# Tip amount: 10.46
# Total amount: 62.77
# Specifications
# • The program should accept decimal entries like 52.31 and 15.5 for the cost of the meal.
# • The program should accept integer entries like 15, 20, and 25 for the tip percent.
# • The program should validate both user entries. That way, the user can’t crash the
# program by entering invalid data.
# • The program should only accept numbers that are greater than 0.
# • The program should round results to a maximum of two decimal places {8-1}.

def input_meal():

    print("INPUT")

    while True:
        try: 
            cost = float(input("Cost of Meal: "))
        except:
            print("Must be a valid decimal number. Please try again")
            continue
        if(cost <= 0):
            print("Must be greater than 0. Please try again.")
            continue
        break

    while True:
        try: 
            tip = int(input("Tip precent: "))
        except:
            print("Must be a valid integer. Please try again")
            continue
        if(tip <= 0):
            print("Must be greater than 0. Please try again.")
            continue
        break

    return cost, tip

def output_meal(cost, tip):
    
    print("\n OUTPUT")

    print(f"Cost of meal {cost}")
    print(f"Tip percent: {tip}%")
    
    tip_amount = round(float(cost) * float( tip / 100 ), 2)
    print(f"Tip amount: {tip_amount}")

    total = float(cost) + tip_amount
    print(f"Total amount: {total}")


def main():
    print("Tip Calulator")

    
    cost, tip = input_meal()
    output_meal(cost, tip)


if __name__ == "__main__":
    main()