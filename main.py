def getinput():
    num = int(input())
    return num
    # ******************************
    # Make your Code
    # ******************************


def getsum(userval1, userval2):
    total = userval1 + userval2
    return total
    # ******************************
    # Make your Code
    # ******************************


def printval(userval1, userval2, total):
    print(userval1, userval2, total)
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
