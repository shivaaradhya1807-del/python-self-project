Health_score=100
gold_score=0

def intro():
    print("Welcome to the haunted hotel!")
    print("Find the treasure and escape ")

def choose():
    print("Choose a door 1,2 or 3")
    choice=input("Enter your choice")
    return choice


def result(choice):
    global Health_score, gold_score

    if choice =="1":
        print("The zombies are chasing you!!! Game over")
        Health_score-=20
        
    elif choice == "2":
        print("Yes!! You have reached the end of the world,game over")
        Health_score-=100
        
    elif choice =="3":
        print("Wow!!! u found all the treasure ,u won!!")
        Health_score+=1000
        gold_score+=1000
    else:
        print("INVALID!!")
intro()
door = choose()
result(door)


print("\n===== FINAL SCORES =====")
print("Amount gold =", gold_score)
print("Health score =", Health_score)