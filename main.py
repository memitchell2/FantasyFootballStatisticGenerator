##############################################
##
## Fantasy Football Statistic Generator
##
## Author: Max Mitchell
## Date of Completion: 
##
##############################################

# Import modules

while True:
    print("Welcome to the Fantasy Football Statistic Generator!")
    print("Please select an option:")
    print("1. Generate a random statistic")
    print("2. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        print("Generating a random statistic...")
        
    elif choice == "2":
        print("Exiting the program...")
        break
    else:
        print("Invalid choice. Please try again.")
