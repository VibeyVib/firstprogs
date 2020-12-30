command=""
while command!= "empty":
    command= input("> ").lower()
    if command=="start":
        print("Car started")
    elif command=="stop":
        print("Car has stopped")
    elif command=="left":
        print("car has turned left")
    elif command =="right":
        print("Car has turned right")
    elif command=="help":
        print("""Start- to start the car 
Stop- stop the car
help- to obtain help 
left- to turn left
right-turn right
quit- to quit the game """)
    elif command=="quit":
        print("Quit the game ")
        break
else:
    print("I don't understand that")




