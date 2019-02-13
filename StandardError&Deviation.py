import math

def main():
    # This code will calculate the Standard Deviation and Standard Error for
    # the speicfied values. Throughout this code example calculations
    # and anaylsis description is provdied.
    # this code takes the user input of the four numbers that will be
    # used to calculate standard deviation and standard error

    num1 = float(input("Enter first piece of data"))
    num2 = float(input("Enter second piece of data"))
    num3 = float(input("Enter third piece of data"))
    num4 = float(input("Enter fourth piece of data"))

    #This calculates the average value

    numsum = num1 + num2 + num3 + num4
    numavg = numsum / 4

    # This prints the average value befroe continuing

    print("This is the avergae of the entered values: ", numavg)

    # This is the 1/(N-1)

    n = 4
    part_one = 1/(n-1)

    # this handles the summation part.

    sum1 = (num1 - numavg) * (num1 - numavg)
    sum2 = (num2 - numavg) * (num2 - numavg)
    sum3 = (num3 - numavg) * (num3 - numavg)
    sum4 = (num4 - numavg) * (num4 - numavg)

    sumtotal = sum1 + sum2 + sum3 + sum4

    # This handles combining part one and the summation then printing the result

    under_rad = part_one * sumtotal

    standdev = math.sqrt(under_rad)

    print("The Standard Deviation is: ", standdev)

    # This code will compute the standard error and print the result.
    # What is happening computationally can be seen by looking at the
    # well named variables.

    numer = standdev
    denumer = math.sqrt(n)

    stanerror = numer/denumer

    print("The standard error is: ", stanerror)

#The Main at the bottom gets the ball rolling and is what starts the program

main()
