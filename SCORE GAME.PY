print("welcome to score game!!!")
score=0

q1=str(input("What is the capital of Maharashtra"))
if q1 == "Mumbai":
    score = score+1
    print("q1 correct")
else:
    score=score+0
    print("wrong!")

q2=str(input("What is the colours of the indian flag"))
if q2 == "Orange,White,Green":
    score=score+1
    print("q2 correct")
else:
    score=score+0
    print("wrong!")

q3=str(input("who wrote the Indian constitution"))
if q3 == "BR Ambetkar":
    score=score+1
    print("q3 correct")
else:
    score=score+0
    print("wrong")

print("final score =",score)
if score =="3":
    print("You won !!")
else:
    print("try again")