'''

Project A  : Escape Room

Author     : Shawn Mitchell

Description:

'''
from time import strftime
play = True

openBox  = False
lockDoor = True
takeKey  = False

welcome = "Welcome to 'The Escape Room!'\nCurrent Level: Easy\nRating: *"

roomDescription = "You see a box, a clock hanging on the wall and a door with an exit sign on it\nEnter help for a menu"

print(welcome)
print(roomDescription)

while(play):
    command = input("--> ")

    if(command == "quit"):
        play = False
    elif(command == "help"):
        print("*"*39)
        print("** Available Commands                **")
        print("**-----------------------------------**")
        print("** help - this menu                  **")
        print("** open - open something (prompt)    **")
        print("** take - take something (prompt)    **")
        print("** look - look at something (prompt) **")
        print("** use  - use something (prompt)     **")
        print("** pack - view contents of pack      **")
        print("*"*39)
    elif(command == "pack"):
        print("*"*17)
        print("* Pack Contents *")
        print("-----------------")
        pack = 0
        ## check items here and increase pack by 1 per item
        if(takeKey):
            pack += 1
            print("* key           *")
        if(pack == 0):
            print("* - Empty-      *")
        print("*"*17)
    elif(command == "open"):
        cmdOpen = input("Open what -->")
        if(cmdOpen == "box"):
            if(openBox):
                print("Box is already open!")
            else:
                print("You open the box!")
                openBox = True
        elif(cmdOpen == "door"):
            if(lockDoor):
                print("Door is locked!")
            else:
                print("You open the Door. You win!")
                play = False
            print("")
        else:
            print("What are you trying to open?")
        
    elif(command == "take"):
        cmdTake = input("Take what -->")
        if(cmdTake == "box"):
            print("Box is too large to take.")
        elif(cmdTake == "clock"):
            print("Clock looks like it is secured to the wall")
        elif(cmdTake == "key"):
            takeKey = True
            print("You take the key!")
        else:
            print("You want to take what?")
        
    elif(command == "look"):
        cmdLook = input("Look at what -->")
        if(cmdLook == "clock"):

            clockHour = int(strftime("%H"))
            clockMin  = int(strftime("%M"))
            clockTag  = "AM"

            if(clockMin < 10):
                clockMin = "0"+str(clockMin)

            if(clockHour > 11):
                clockTag = "PM"

            if(clockHour > 12):
                clockHour -= 12

            if(clockHour == 0):
                clockHour = 12
            
            print("The time is "+str(clockHour)+":"+str(clockMin)+" "+clockTag)
        elif(cmdLook == "box"):
            if(openBox):
                print("The box is open")
                if(takeKey):
                    print("and empty")
                else:
                    print("Inside the box is a shiny key")
            else:
                print("You see a sealed box")
        
    elif(command == "use"):
        cmdUse = input("Use what -->")
        if(cmdUse == "key"):
            if(lockDoor):
                print("You unlock the door!")
                lockDoor = False
            else:
                print("Door is already unlocked")    
    else:
        print("What did you want to do?")
    

print("Exiting Game")
