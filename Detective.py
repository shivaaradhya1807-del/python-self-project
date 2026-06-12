clues = 0

def intro():
    print("Some one stole the diamond 💎 !!!")
    print("We have 3 suspects")
    print(" 1.John")
    print("2.Sarah")
    print("3 .Grace")


def investigate():
    global clues

    print("\nWho do you want to question?")
    print("1. John")
    print("2. Sarah")
    print("3. Grace")

    choice = input("Choose who do you want to ask first (1, 2 or 3): ")

    if choice == "1":
        print("I was just reading 📖.")
        clues += 1

    elif choice == "2":
        print("I was having a walk 🚶.")
        clues += 1

    elif choice == "3":
        print("I was sleeping 😴🥱.")
        clues += 1

    else:
        print("Invalid")


intro()
investigate()
investigate()
investigate()
print("Clues found:", clues)


def accuse():
    guess = input("Who stole the diamond? ")

    if guess == "3":
        print("You solved the case! 👏👏")
    else:
        print(" Wrong suspect! ❌❌")

accuse()