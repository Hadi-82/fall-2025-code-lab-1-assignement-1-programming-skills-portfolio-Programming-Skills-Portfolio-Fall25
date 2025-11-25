Name = ["Jake","Zac", "Ian", "Ron", "Sam", "Dave"]                              # Name List is defined

find = input("Enter the name you want to search : ").capitalize()               # Capitalize() is used since the names are capitalized in the list 

for i in Name:
    if find == i:                                                               # Finding the name using  for loop and if statement 
        print(f"{find} is in the list")