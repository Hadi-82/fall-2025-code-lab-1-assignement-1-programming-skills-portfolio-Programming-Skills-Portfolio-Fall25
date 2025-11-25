correctpass = "12345"                                          # Defining the correct password

max = 5                                                        # Maximum amount of attempts given

attempts = 0                                                   

while attempts < max:
    password = input("Enter your password : ")
    attempts += 1
    if password == correctpass:                                                     
        print("You have been logged in")
        break
    else:
        print("Access denied. The password you have entered is incorrect.")
        remainingattempts = max - attempts
        if remainingattempts > 0:                                                               
            print(f"You have {remainingattempts} attempts remaining")               
        else:
            print("You have reached the maximum number of attempts.\nYour account has been locked and the authorities have been alerted.")     # Alerting the authorities since maximum number of attempts reached
