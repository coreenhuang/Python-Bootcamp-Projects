#Interactive treasure island game

print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

left_or_right = input('You reach a cross road with two paths. Would you like to go left or right? Type "left" or "right".\n')

if left_or_right.lower() == "left":

    wait_or_swim = input('You travel on this path with no problem and reach a dock by a lake. You see there is an island in the middle of the lake. There is a boat that will leave the dock in one hour. Would you like to wait or swim to the island? Type "wait" or "swim".\n')

    if wait_or_swim.lower() == "wait":

        which_door = input('You reach the island safely. There is a haunted mansion up ahead with three different doors: red, yellow, and blue. Which colour do you choose?\n')

        if which_door.lower() == "yellow":

            print("You see the treasure. You win!")

        elif which_door.lower() == "red":

            print("You enter the room and the door swings shut behind you. Flames erupt all around you and you burn to death. Game Over.")

        elif which_door.lower() == "blue":

            print("The room is dark and you can't see a thing. The door behind you swings shut and the lights turn on. There are beasts all around you waking from the loud noise. They tackle and eat you. Game Over.")
            
        else:
            print("You enter the room. The door swings shut. You can never open the door again to escape. You starve to death. Game Over.")

    else:
        print("You jump into the lake and start swimming towards the island. You see a mermaid coming towards you, but you continue swimming. The mermaid catches up to you and then pulls you into the depths of the deep water. You drown. Game Over.")

else:
    print("You trip on a stone and roll down to your doom. Game Over.")