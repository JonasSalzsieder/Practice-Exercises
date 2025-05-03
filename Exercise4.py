print("Please choose from the following dishes")
dishes = ["Fried Rice", "Pizza", "Burger"]

for dish in dishes:
    print(dish)
user_input = input("Which one would you like?: ")

if len(user_input) >=1:
    if len(user_input) <=10:
        if user_input == ("Fried Rice"):
            print("Good Choice")
        elif user_input == ("Pizza"):
            print("Not very healthy but tasty")
        elif user_input == ("Burger"):
            print("Damn son, good choice")
        else:
            print("This item is not on the list")
    else:
        print("Your choice is to long")
else:
     print("Please input a dish")