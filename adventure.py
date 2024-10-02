# Task 1

place = input("Choose a place: forest or cave? ")

if place == "forest":
    action = input("climb a tree or cross a river? ")
    if action == "climb a tree":
        print("You found a bird's nest!")
    elif action == "cross a river":
        print("You found a boat!")
elif place == "cave":
    print("You find a hidden treasure!")


# Task 2

place = input("Choose a place: forest or cave? ")

if place == "forest":
    action = input("climb a tree or cross a river? ")
    if action == "climb a tree":
        print("You found a bird's nest!")
    elif action == "cross a river":
        print("You found a boat!")
elif place == "cave":
    cave_action = input("light a torch or proceed in the dark?")
    if cave_action == "light a torch":
        print("You found a hidden treasure!")
    elif cave_action == "proceed in the dark":
        print("You fell to your untimely death!")


# Task 3

place = input("Choose a place: forest or cave? ")

if place == "forest":
    action = input("climb a tree or cross a river? ")
    if action == "climb a tree":
        print("You found a bird's nest!")
    elif action == "cross a river":
        print("You found a boat!")
    else:
        print("Invalid choice.")
        pass
elif place == "cave":
    cave_action = input("light a torch or proceed in the dark? ")
    if cave_action == "light a torch":
        print("You found a hidden treasure!")
    elif cave_action == "proceed in the dark":
        print("You fell to your untimely death!")
    else:
        print("Invalid choice.")
        pass
else:
    print("Invalid choice.")
    pass