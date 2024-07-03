def getinput():
    num = int(input("Number: "))
    return num
    # ******************************
    # Make your Code
    # ******************************


def getsum(v1, v2):
    total = v1 + v2
    return total
    # ******************************
    # Make your Code
    # ******************************


def printval(v1, v2, total):
    print(f"{v1}, {v2}, {total}")
    # ******************************
    # Make your Code
    # ******************************


def main():
    userval1 = getinput()
    userval2 = getinput()
    total = getsum(userval1, userval2)
    printval(userval1, userval2, total)


if __name__ == '__main__':
    main()
