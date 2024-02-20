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

        print(f"{t2}")
            

    return r2, s2, t2


def main():
    try:
        a = int(input("Enter a: "))
        b = int(input("Enter b: "))
    except:
        print("Invalid input")
        exit()


    r, s, t = extended_euclidean(a, b)

    if(r != 1):
        print("There is NO multiplicative inverse")
    else:
        print(f"There is a multiplicative inverse for {a} which is t = {t}")

if __name__ == "__main__":
    main()