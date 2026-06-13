print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ .   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". __|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************
''')
print('''
Welcome to Treasure Island.
Your mission is to find the treasure.''')
print("you\'re at a cross. Where do you want to go?")
choice1=input(" Type left or right\n")
if choice1 =="left":
    choice2=input('you\'ve come to a lake.'
                  'There is an island in the middle of the lake'
                  'type "wait" to wait for a boat'
                  'type "swim" to swim across\n').lower()
    if choice2 =="wait":
        choice3=input("you got attacked at the island unharmed."
                      'There is house wit 3 doors'
                      "one red and one blue.which colour do you choose\n").lower()
        if choice3=="red":
           print ("it's a room full of fire . game over")
        elif choice3=="yellow":
             print("you found the treasure.you win")
              
        elif choice3=="blue":
              print("you enter a room of beast.Game over.")
        else:
            print("you chose  a door that doesn't exist.Game over")
    else: 
        print("you got attacked by an angry trout. game over")
              
 
    
else:
    print("GAME OVER ")
