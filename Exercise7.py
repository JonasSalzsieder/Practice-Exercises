tasks = []

def add_to_list():
    user_input = input("What would you like to add to the list?: ")
    tasks.append(user_input)

def remove_from_list():
    user_input = input("Which item would you like to remove? Enter the index of the item please: ")
    if user_input.isdigit():
        index = int(user_input) - 1
        if int(index) >= len(tasks):
            print("There is no item at that index in the list.")
            print("You can only choose " + str(len(tasks)))
        else:
            if 0 <= int(index) <= len(tasks):
                tasks.pop(int(index))
            else:
                print("This is not a valid input")
                user_input = input("Please enter a number: ")

    else:
        print("This is not a valid input")
        user_input = input("Please enter a number: ")

def show_list():
    if len(tasks) >= 1:
        for index,item in enumerate(tasks):
            human_index = index + 1
            print(str(human_index) + ". " + item)
    else:
        print("The list is empty.")

actions = ["add", "Add", "remove", "Remove", "show", "Show", "Exit", "exit"]

#Application Loop

while True:
    print("What would you like to do? 'add', 'remove', 'show' or 'exit'?")
    action_input = input("> ")
    if action_input == "add":
        add_to_list()
    elif action_input == "remove":
        remove_from_list()
    elif action_input == "show":
        show_list()
    elif action_input == "exit":
        print(tasks)
        break
    else:
        print ("This is not a valid command. Please enter 'add', 'remove', 'show' or 'exit'")

    show_list()
    
  
