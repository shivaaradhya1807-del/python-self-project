mood=str(input("Enter your mood today:  angry/ tired /happy / scared /sad?"))
def normalize(text):
    return text.lower().replace(" ", "").replace(",", "")
mood_score=0
if normalize (mood) == normalize("Sad"):
    print ("advise=You need to cheer up your mind")
    print ("advise= Do or make something you like")
elif normalize(mood) == normalize("Tired"):
    print ("advice=Take some rest")
    print ("advise=Or play something you like")
elif normalize (mood) == normalize("Scared"):
    print (" advise=Think of happy things or something you like")
    print ("advise=Get distracted with something that makes you happy")
elif normalize (mood) == normalize ("Anger"):
    print ("advise= calm down ")
    print ("advise= do not think about it ")
else :
    print (" I guess you are in a happy mood today")
    print(" do something more happy and enjoy")


improve= str(input("did your mood improve with this yes or no"))
if normalize (improve) ==normalize ("Yes"):
    mood_score=mood_score+100
    print("Glad I can help")
    print("mood score =", mood_score)
else :
    mood_score=mood_score+10
    print ("sorry I cannot help")
    print("mood score=", mood_score)
print ("final mood score =", mood_score)
def normalize(text):
    return text.lower().replace(" ", "").replace(",", "")

print("Try out the energy check adviser")
energy_score=0
energy=int(input("enter your energy 1-5"))

if  (energy) ==1:
    print("advise= do some excersise or yoga")
    print ("advise= hype up your brain by playing chess or brain games")
    print (" Dont feel sad ")
elif  (energy) == 2:
    print ("get some phisical excersise")
    print("Your energy must be low today")
elif  (energy) == 3:
    print (" take some rest if needed")
elif  (energy) ==4:
    print("You have enough energy to do something you like or fun")
else :
    print ("you have so much energy try doing something exiting")

energy_improve=str(input("Did it improve enter in yes or no"))

if normalize (energy_improve) == normalize("Yes"):
    energy_score = energy_score+ 100
    print(" glad I can help")
else :
    energy_score=energy_score+ 10
    print("SORRY")
print("final energy score=", energy_score)