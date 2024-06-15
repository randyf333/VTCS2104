
def isLeapYear(value):
    try:
        val = int(value)
    except ValueError:
        print("Not an int")
        return
    if(val % 400 == 0):
        print("leap year")
    elif(val % 4 != 0):
        print("NOT a leap year")
    elif(val % 100 != 0):
        print("leap year")
    else:
        print("NOT a leap year")


if __name__== "__main__":
    year = input("Input Year: ")
    isLeapYear(year)
