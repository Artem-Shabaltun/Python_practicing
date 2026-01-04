import random
from hangman_words import word_list
from hangman_arts import stages, logo

# LIVES AREA
lives = 6


print(logo)
chosen_word = random.choice(word_list)
# print(f"for testing: {chosen_word}")

# PLACEHOLDERS FOR THE LETTERS
placeholder = ""

for position in range(len(chosen_word)):
    placeholder += "_"
print(placeholder)

# MAIN LOGIC
game_over = False
right_letters = []

while not game_over:
    print(f"********************** {lives}/6 LIVES LEFT **********************")
    guess = input("Guess a letter: ").lower()

    if guess in right_letters:
        print (f"You've already guessed {guess}")

    display = ""

    for letter in chosen_word:
        if letter == guess:
            display += letter
            right_letters.append(guess)

        elif letter in right_letters:
            display += letter
        else:
            display += "_"
    print("Word to guess: " + display)

    if guess not in chosen_word:
        lives -= 1
        print(f"{guess}, that's not in the word. You lose a life")
        if lives == 0:
            game_over = True

            print(f"********************** {lives}/6 LIVES LEFT **********************")
            print(f"************* THE WORD WAS:{chosen_word}, YOU LOSE! *****************")

    if "_" not in display:
        game_over = True
        print("********************** YOU WIN! **********************")

    print(stages[lives])
