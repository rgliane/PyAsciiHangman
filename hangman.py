import random
import os
import hangman_ascii as man
#Step 1

def split(word):
    return [char for char in word]

def clear(): os.system('cls')

def initguess(word):
    return ["_" for _ in word]

word_list = ["aardvark", "baboon", "camel"]

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word
# chosen_word = word_list[random.randint(0, len(word_list) - 1)]
chosen_word = random.choice(word_list)
guess_tracker = initguess(chosen_word)

is_game_running = True
num_lives = 6
num_wrong = 0
while is_game_running:
    clear()
    #TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
    print(f"Psst, the word is {chosen_word}")
    print(guess_tracker)
    print(man.hanging[num_wrong])
    guess = input("Guess a letter: ")

    #TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word
    letter_found = False
    for x in range(len(chosen_word)):
        if chosen_word[x] == guess:
            guess_tracker[x] = chosen_word[x]
            letter_found = True

    is_empty_space_found = False
    #TODO: Use 'in' instead of below
    for x in range(len(guess_tracker)):
        if guess_tracker[x] == '_':
            is_empty_space_found = True

    if not is_empty_space_found:
        is_game_running = False
        clear()
        print(guess_tracker)
        print("You Win!")
    
    if not letter_found:
        num_wrong += 1
    
    if num_wrong == num_lives:
        is_game_running = False
        clear()
        print(guess_tracker)
        print(man.hanging[num_wrong])
        print("You ded bru! Lose!")