# number_to_check = int(input("What is the number you want to check? "))
#
# if number_to_check % 2 == 0:
#     print("Even")
# else:
#     print("Odd")





# print("Welcome to the rollercoaster!")
# height = int(input("What is your height in cm?"))
# bill = 0
#
# if height >= 120:
#     print("You can ride the rollercoaster")
#     age = int(input("What is your age?"))
#     if age <= 12:
#         print("Child tickets are $5.")
#         bill = 5
#     elif age <= 18:
#         print("Youth tickets are $7.")
#         bill = 7
#     elif age >= 45 and age <= 55:
#         print("Ride for you is free")
#         bill = 0
#     else:
#         print("Adult tickets are $12.")
#         bill = 12
#
#     wants_photo = input("Do you want to have a photo take? Type y for Yes and n for No.")
#     if wants_photo =="y":
#         bill += 3
#
#     print(f"Your final bill is ${bill}")
#
# else:
#     print("Sorry you have to grow taller before you can ride")






# print("Welcome to Python Pizza Deliveries!")
# size = input("What size pizza do you want? S,M or L: ")
# pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
# extra_cheese = input("Do you want extra cheese? Y or N: ")
#
# bill = 0
#
# if size == "S":
#     bill = 15
# elif size == "M":
#     bill = 20
# elif size == "L":
#     bill = 25
#
# else:
#     print("You typed the wrong inputs")
#
# if pepperoni == "y":
#     if size == "S":
#         bill += 2
#     else:
#         bill +=3
#
# if extra_cheese == "y":
#     bill += 1
# else:
#     pass
#
# print(f"Your final bill is: ${bill}")




print(r'''
                    ____...------------...____
               _.-"` /o/__ ____ __ __  __ \o\_`"-._
             .'     / /                    \ \     '.
             |=====/o/======================\o\=====|
             |____/_/________..____..________\_\____|
             /   _/ \_     <_o#\__/#o_>     _/ \_   \
             \_________\####/_________/
              |===\!/========================\!/===|
              |   |=|          .---.         |=|   |
              |===|o|=========/     \========|o|===|
              |   | |         \() ()/        | |   |
              |===|o|======{'-.) A (.-'}=====|o|===|
              | __/ \__     '-.\uuu/.-'    __/ \__ |
              |==== .'.'^'.'.====|
              |  _\o/   __  {.' __  '.} _   _\o/  _|
              `""""-""""""""""""""""""""""""""-""""`
''')

print("Welcome to Treasure Island. \nYour mission is to find the treasure.")

side = input("What side do you choose to go: left or right?").lower()
if side == "left":
    action = input("You have find the cave lake. What do you choose: swin or wait?").lower()
    if action == "wait":
        door = input("The water was out, and you seem the three doors. Which door do you choose : Red, Yellow or Blue?").lower()
        if door == "red":
            print("Burned by fire. \nGame Over")
        elif door == "blue":
            print("Eaten be beasts. \nGame Over.")
        elif door == "yellow":
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
/______/______/______/______/______/______/______/______/______/______/______/
*******************************************************************************

----------------------------YOU WIN!-------------------------------------------
            ''')
        else:
            print("Wrong choise. Game Over.")
    else :
        print("Attacked by trout. \nGame Over.")

else:
    print("Fall into a hole. \nGame Over.")


