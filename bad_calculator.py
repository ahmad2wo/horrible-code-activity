"""
By: Ahmad Idris
"""


x = 0  
y = 0

def doStuff():  # vague name, huge function, mixes everything
    global x, y
    print("WELCOME TO CALC (bad)")
    print("Pick: 1 add, 2 sub, 3 mul, 4 div, 5 power, 6 avg, 7 quit")
    z = input("choice? ")
    if z == "7":
        print("bye")
        return

    # no validation; crashes easily
    x = float(input("number 1: "))
    y = float(input("number 2: "))

    # Lots of copy/paste (DRY violation)
    if z == "1":
        r = x + y
        print("RESULT IS:", r)
        print("done\n")
    elif z == "2":
        r = x - y
        print("RESULT IS:", r)
        print("done\n")
    elif z == "3":
        r = x * y
        print("RESULT IS:", r)
        print("done\n")
    elif z == "4":
        # weird “fix”: magic number instead of proper check
        if y == 0:
            print("cant divide by 0 so i'll just divide by 0.00001 lol")
            r = x / 0.00001
            print("RESULT IS:", r)
        else:
            r = x / y
            print("RESULT IS:", r)
        print("done\n")
    elif z == "5":
        # power: still duplicates everything
        r = x ** y
        print("RESULT IS:", r)
        print("done\n")
    elif z == "6":
        # average: random extra math, weird formatting
        r = (x + y) / 2
        print("AVG:", r, " (", x, "+", y, ")/2")
        print("done\n")
    else:
        print("unknown option... i guess try again")

    # recursive call instead of loop (bad idea)
    doStuff()


def helper(a, b, op):  # still mixes logic + text decisions
    # not even used consistently
    if op == 1:
        return a + b
    if op == 2:
        return a - b
    if op == 3:
        return a * b
    if op == 4:
        return a / b
    return 0


def main():
    # pointless repeated printing
    print("====================")
    print(" BAD CALCULATOR APP ")
    print("====================")
    doStuff()


if __name__ == "__main__":
    main()
