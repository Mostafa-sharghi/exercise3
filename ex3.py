gender = input("Enter your gender: (female or male)")
value = int(input("Enter hemoglobin value:"))
if value <= 0:
    print("It is wrong value")
else:
    if gender == ("female"):
        if 117 <= value and value<= 155:
            print("It is normal")
        elif 0 < value and value < 117:
            print("It is low")
        elif value > 155:
            print("It is high")
    elif gender == ("male"):
        if 134 <= value and value<= 167:
            print("It is normal")
        elif 0 < value and value < 134:
            print("It is low")
        elif value > 167:
            print("It is high")
    else:
        print("The gender is wrong!")


