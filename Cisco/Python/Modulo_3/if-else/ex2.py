year = int(input("Enter a year: "))

if year <= 1585:
    print("Not within the Gregorian calendar period")
elif (year % 4 ) == 0:
    print("Leap year")
elif (year % 4) != 0:
    print("Commmon year")