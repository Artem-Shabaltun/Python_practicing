# fruits = ["Apple", "Peach", "Pear"]
# for fruit in fruits:
#     print(fruit)
#     print(fruit + " pie")
# print(fruits)



# students_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86, 55, 91, 64, 89]


# total_exam_score = sum(students_scores)
#
# sum = 0
# for score in students_scores:
#     sum += score
#
#
# print(sum)

# print(max(students_scores))

# max_score = 0
# for score in students_scores:
#     if score > max_score:
#         max_score = score
#     else:
#         continue
#
# print(max_score)


# Range function


# sum = 0
# for number in range (1, 101):
#     sum += number
# print(sum)

for number in range (1, 101):
    if number %3 == 0 and number %5 ==0:
        print("FizzBuzz")
    elif number % 5 ==0:
        print("Buzz")
    elif number % 3 == 0:
        print("Fizz")
    else:
        print(number)
