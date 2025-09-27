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


print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S,M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")

bill = 0

if size == "S":
    bill = 15
elif size == "M":
    bill = 20
elif size == "L":
    bill = 25

if pepperoni == "y":
    bill += 3

if extra_cheese == "y":
    bill += 1

print(f"Your final bill is: ${bill}")