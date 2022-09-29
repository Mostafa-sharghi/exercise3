mah = int(input("Enter number of year :"))
if mah < 0:
    print("It is a wrong number")
else:
    if mah % 4 == 0:
        print("The input year is a leap year")
    else:
        print("The input year is not a leap year")