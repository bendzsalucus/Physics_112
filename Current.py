import math

def main():

    volt = float(input("Enter voltage"))
    rest = float(input("Enter resistance"))

    volterr = float(input("enter volterr"))

    resterr = .05 * rest

    current = volt / rest
    didv = 1 / rest
    didr = -1 * volt / (rest * rest)

    partone = didv * volterr * didv * volterr

    parttwo = didr * resterr *didr * resterr

    underrad = partone + parttwo

    final = math.sqrt(underrad)


    print("the current is", current)
    print("error prop", final)


main()