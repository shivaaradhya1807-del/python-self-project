
print("welcome to score game!!!")
score=0
def normalize(text):
    return text.lower().replace(" ", "").replace(",", "")

q1=str(input("What is the capital of Maharashtra"))
if normalize(q1) == normalize("Mumbai"):
    score = score+1
    print("q1 correct")
else:
    score=score+0
    print("wrong!")

q2=str(input("What is the sequence of colours in the indian flag"))
if normalize (q2) == normalize("Orange,White,Green"):
    score=score+1
    print("q2 correct")
else:
    score=score+0
    print("wrong!")

q3=str(input("who wrote the Indian constitution"))
if normalize(q3) == normalize("BR Ambedkar"):
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

