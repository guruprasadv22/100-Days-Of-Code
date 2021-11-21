print("Welcome to Treasure Island.\nYour mission is to find the treasure.\n")

direction = input(
    "You are at a cross road. Where do you want to go? Type 'left' or 'right'\n")

if direction == "left":
    decision = input(
        "You come to a lake. There is an island in the middle of the lake. Type 'wait' to wait for the boat. Type 'swim' to swim across.\n")
    if decision == "wait":
        door = input(
            "You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow, one blue. Which one do you choose?\n")

        def switch(door):
            switcher = {
                "red": "It\'s a room full of fire game over.",
                "yellow": "You found the treasure. You Win!",
                "blue": "You enter a room full of ice and freeze to death."
            }
            return switcher.get(door, "wrong arg")
        print(switch(door))
    elif decision == "swim":
        print("\nYou get eaten by a hungry crocodile. Game over!")
else:
    print("\nYou fall into a hole. Game Over!")
