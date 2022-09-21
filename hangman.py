import string
import random
file = open('words_copy.txt', "r")
alphabet = list(string.ascii_lowercase) + ["-"]
count = 0
word_list = []
for i in file:
    i = i.strip()
    word_list.append(i)

for j in range(len(word_list)):
    for letter in word_list[j]:
        if len(word_list[j]) <= 4:
            word_list[j] = "empty-not-working-string"
        if letter.lower() not in alphabet:
            word_list[j] = "empty-not-working-string"

while True:
    choice = random.choice(word_list)
    if choice != "empty-not-working-string":
        game_word = choice
        break

show_case = "_ " * len(game_word)


while True:
    difficulty_level = input("Choose your difficulty level: EASY, HARD, MEDIUM\n")
    if difficulty_level.lower() == "easy":
        guesses = len(game_word) * 2.7
        break
    elif difficulty_level.lower() == "medium":
        guesses = len(game_word) * 1.9
        break
    elif difficulty_level.lower() == "hard":
        guesses = len(game_word) * 1.5
        break
    else:
        print("That's not a valid difficulty level. Please try again.")

round_number = 0
letter_guess_list = []
game_word_list = list(game_word)
show_case_list = list(show_case)
for i in show_case_list:
    if i == " ":
        show_case_list.remove(" ")


while round_number < guesses and not show_case == game_word:
    print(show_case)
    given_letter = input("Your letter:")
    if given_letter in alphabet:
        if given_letter not in letter_guess_list:
            while given_letter in game_word_list:
                for index, letter in enumerate(game_word):
                    if given_letter == letter:
                        show_case_list[index] = given_letter
                        game_word_list.remove(given_letter)
                letter_guess_list.append(given_letter)
                show_case = "".join(show_case_list)
                round_number += 1
        else:
            print("You already got this letter! Try another letter.")
    else:
        print("That's not valid. Please enter a LETTER.")

if show_case == game_word:
    print("Congratulations! You won!")
else:
    print("You lost! Better luck next time.")

















