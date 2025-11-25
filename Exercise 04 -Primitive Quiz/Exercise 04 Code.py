print("----- Capital Guesser -----")                                            # Headline
                                                                                
print("Welcome to the Capital Guesser Quiz")                                    # Introduction
print("You will be asked to guess the capitals of 10 countries")                

Score = 0                                                                       # Creating a variable called Score to keep track of how many questions user gets right 

L = {
    "france" : "paris",
    "spain" : "madrid",
    "italy" : "rome",
    "united kingdom" : "london",
    "germany" : "berlin",                                                       # Making a dictionary with the european countries and their capitals
    "greece" : "athens",
    "austria" : "vienna",
    "portugal" : "lisbon",
    "netherlands" : "amsterdam",
    "croatia" : "zagreb"
} 

def Checker(Country,Capital):                                                   # Function to check if the given answer is correct or not 
    if L[Country] == Capital:
        print(f"Your answer {Capital} is absolutely right")
        global Score                                                            # Global score to update the Score variable 
        Score += 1                                                              
    else:                                                                   
        print(f"I am sorry but your answer {Capital} is wrong")

for i in L:                                                                     # Loop to ask the user capital of each country
    Answer = input(f"What is the capital of {i}? : ")
    Answer = Answer.lower()                                                     # .lower() has been used to ignore capitalization of the answer
    Answer = Answer.strip()                                                     # .strip() to remove any extra spaces
    Checker(i,Answer)                                                           # calling the function
    print("Onto the next question!")

print("Oh nevermind! The quiz is already over. Congratulations!")
print(f"You got {Score} out of 10 Countries correct good job!")                  # Quiz feedback



    