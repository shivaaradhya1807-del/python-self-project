print ("starting point vijayywada")
print("1 Hyderabad")
print("2 Bengluru")
print("3 Chennai")

choice=int(input("Choose your destination"))
tickets=int(input("How many tickets you want"))

if choice == 1 :
    total=tickets*200
    print("Hyderabad ticket")
    print("cost of one ticket=200")
    print("ticket price=",total)
elif choice == 2 :
    total=tickets*400
    print("Bengluru ticket")
    print("Cost of one ticket =400 ")
    print("Tickets price =",total)
elif choice == 3 :
    total=tickets*550
    print("chennai ticket")
    print("Cost of one ticket =550")
    print("Tickets price =",total)
else:
    print("invalid ticket")
 
 
 