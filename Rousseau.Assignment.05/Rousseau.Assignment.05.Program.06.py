# Program #06:

# Write a Python program to find the gcd (a,b) for two numbers a and b, and the values of s and t.
# Console
# Enter the first number: 161
# Enter the second number: 28
# Here it is:
# gcd (161,28) = 7
# s (161,28) = -1
# t (161,28) = 6
# Thank you!

def extended_euclidean(r1, r2):

    s1 = 1
    s2 = 0
    t1 = 0 
    t2 = 1
    r = 222222
    s = int()
    t = int()


    while(True):
 
        r = r1 % r2
        q = r1 // r2

        s = s1 - (q * s2)
        t = t1 - (q * t2)

        if(r != 0):
            r1 = r2
            r2 = r
            s1 = s2 
            s2 = s
            t1 = t2 
            t2 = t
        else:
            break
            

    return r2, s2, t2

def main():

    try:
        a = int(input("Enter the first number: "))
        b = int(input("Enter the second number: "))
    except:
        print("Invalid input")
        exit()
        
    r, s, t = extended_euclidean(a, b)

    print(f"Here it is:\ngcd({a},{b}) = {r}")
    print(f"s ({a},{b}) = {s}")
    print(f"t ({a},{b}) = {t}")


if __name__ == "__main__":
    main()