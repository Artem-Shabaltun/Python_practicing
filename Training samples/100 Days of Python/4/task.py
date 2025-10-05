import random
# import my_module

# random_iteger = random.randint(1, 10)
# print(random_iteger)
#
# print(my_module.my_favorite_number)


# random_nomber_0_to_1 = random.random() * 10
# print(random_nomber_0_to_1)

# random_float = random.uniform(1, 10)
# print(random_float)



# random_heads_or_tails = random.randint(0,1)
# if random_heads_or_tails == 0:
#     print("Heads")
#
# else:
#     print("Tails")


# friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]
#
# bill_name = random.choice(friends)
# print(bill_name)
#
# random_index = random.randint(0,4)
# print(friends[random_index])


# fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
# vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]
#
# dirty_dozen = [fruits, vegetables]
#
# print(dirty_dozen[1][1])
#
# print(dirty_dozen)
#
#
# print(dirty_dozen[0])
# print(dirty_dozen[1])
#
#
# print(dirty_dozen[1][2])
# print(dirty_dozen[1][3])










# print("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.")
#
# my_choise = int(input())
#
# if my_choise == 0:
#     print("""
#         _______
#     ---'   ____)
#           (_____)
#           (_____)
#           (____)
#     ---.__(___)
#     """)
# elif my_choise == 1:
#     print("""
#          _______
#     ---'    ____)____
#                ______)
#               _______)
#              _______)
#     ---.__________)
#     """)
# elif my_choise == 2:
#     print("""
#         _______
#     ---'   ____)____
#               ______)
#            __________)
#           (____)
#     ---.__(___)
#     """)
#
#
# computer_choise = random.randint(0, 3)
#
# if computer_choise == 0:
#     print("""
#         _______
#     ---'   ____)
#           (_____)
#           (_____)
#           (____)
#     ---.__(___)
#     """)
# elif computer_choise == 1:
#     print("""
#          _______
#     ---'    ____)____
#                ______)
#               _______)
#              _______)
#     ---.__________)
#     """)
# elif computer_choise == 2:
#     print("""
#         _______
#     ---'   ____)____
#               ______)
#            __________)
#           (____)
#     ---.__(___)
#     """)
#
# if my_choise == 0 and computer_choise == 2:
#     print("Rock crushes Scissors. \nYou win!")
# elif my_choise == 2 and computer_choise == 1:
#     print("Scissors cuts Paper. \nYou win!")
# elif my_choise == 1 and computer_choise == 0:
#     print("Paper covers Rock. \nYou win!")
# elif my_choise == computer_choise:
#     print("It is a tie. \nReplay round")
# else:
#     print("You lose. \nTry again!")









rock = """
        _______
    ---'   ____)
          (_____)
          (_____)
          (____)
    ---.__(___)
    """
paper = """
         _______
    ---'    ____)____
               ______)
              _______)
             _______)
    ---.__________)
    """
scissors = """
        _______
    ---'   ____)____
              ______)
           __________)
          (____)
    ---.__(___)
    """

game_images = [rock, paper, scissors]

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))
if user_choice >= 0 and user_choice <= 2:
    print(game_images[user_choice])
else:
    print("You typed an invalid number. Repeat again")
    exit()



computer_choice = random.randint(0, 2)
print(f"Computer chose:{computer_choice}")
print(game_images[computer_choice])


if user_choice == 0 and computer_choice == 2:
    print("You wins!")
elif computer_choice == 0 and user_choice ==2:
    print("You win!")
elif computer_choice > user_choice:
    print("You lose!")
elif user_choice > computer_choice:
    print("You win!")
elif computer_choice == user_choice:
    print("It's a draw!")
