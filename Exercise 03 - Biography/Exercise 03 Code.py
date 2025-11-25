Info = {}                                                               # Creating a dictionary

userfirstname = input("Please enter your first name : ")                       
userlastname = input("Please enter your last name : ")                  
username = userfirstname + " " + userlastname                           # Making a variable adding the users first name and last name
Info["Name"] = username                                                 # Updating the dictionary

userhometown = input("Please enter the name of your hometown : ")       
Info["Hometown"] = userhometown                                         # Updating the dictionary

try:                                                                    
    userage = int(input("Please enter your age : "))                    # Handling ValueError when you enter a string value rather than an integer         
    Info["Age"] = userage                                               # Updating the dictionary
except ValueError:                                                      
    print("Please enter a valid number for your age")                   
                                                                        
print(f"{Info["Name"]}\n{Info["Hometown"]}\n{Info["Age"]}")             # Printing the values on seperate lines using a single print() statement 