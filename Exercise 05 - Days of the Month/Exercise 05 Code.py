Months = {                                                          # Creating dictionary to map the month numbers (1-12) to the number of days in each month
    1 : 31,
    2 : 28,
    3 : 31,
    4 : 30,
    5 : 31,
    6 : 30,
    7 : 31,
    8 : 31,
    9 : 30,
    10 : 31,
    11 : 30,
    12 : 31
}

leap = ""
monthno = int(input("Enter the month number : "))                   # Asking user to input the month number

if monthno in Months:                                               # Checking if the input is valid
    if monthno == 2:
        leap = input("is it a leap year? (Y/N) : ").upper()         # Checking if its a leap year
    if leap == "Y":
        Months[2] = 29                                              # Updating the days in February since its a leap year
    print(f"There is {Months[monthno]} days in the given month")

else:
    print("Please input a valid month number next time")