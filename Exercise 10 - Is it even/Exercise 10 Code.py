def main():                                                         # Declaring the main() function   
    number = int(input("Enter your number : "))                     # Asking the user to input the number to be checked
    checker=oddevenchecker(number)                                  # Checking if its odd or even using the oddevenchecker() function 
    print(checker)                                                  # Printing the message return by the oddevenchecker() function

def oddevenchecker(number):                                         # Declaring the oddevenchecker() function
    if number % 2 == 0:
        return (f"The given number {number} is even")
    else:
        return (f"The given number {number} is odd")
    
if __name__ == "__main__":
    main()                                                          # Calling the main() function