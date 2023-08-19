import random
words = ["based", "cabin", "canal", "eagle", "early", "tiger"]

logo = """
\n .----------------.  .----------------.  .----------------.  .----------------.  .----------------.  .----------------. 
| .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. |
| | _____  _____ | || |     ____     | || |  _______     | || |  ________    | || |   _____      | || |  _________   | |
| ||_   _||_   _|| || |   .'    `.   | || | |_   __ \    | || | |_   ___ `.  | || |  |_   _|     | || | |_   ___  |  | |
| |  | | /\ | |  | || |  /  .--.  \  | || |   | |__) |   | || |   | |   `. \ | || |    | |       | || |   | |_  \_|  | |
| |  | |/  \| |  | || |  | |    | |  | || |   |  __ /    | || |   | |    | | | || |    | |   _   | || |   |  _|  _   | |
| |  |   /\   |  | || |  \  `--'  /  | || |  _| |  \ \_  | || |  _| |___.' / | || |   _| |__/ |  | || |  _| |___/ |  | |
| |  |__/  \__|  | || |   `.____.'   | || | |____| |___| | || | |________.'  | || |  |________|  | || | |_________|  | |
| |              | || |              | || |              | || |              | || |              | || |              | |
| '--------------' || '--------------' || '--------------' || '--------------' || '--------------' || '--------------' |
 '----------------'  '----------------'  '----------------'  '----------------'  '----------------'  '----------------' 
"""
def choose_word():
    return random.choice(words)
def check_guess(secret_word, guessed_word):
    result = []
    for i in range(len(secret_word)):
        if guessed_word[i] == secret_word[i]:
            result.append(guessed_word[i].upper())
        elif guessed_word[i] in secret_word:
            result.append(guessed_word[i])
        else:
            result.append("_")
    return " ".join(result)
def start():
    wordle = choose_word()
    print(logo)
    print("\nWelcome to (Budget) Wordle. Guess the 5 letter word.")
    attempts = 6
    while attempts > 0:
        guess = input("Guess {}: ".format(7 -attempts)).lower()
        if len(guess) != len(wordle):
            print("Please enter a 5 letter word")
            continue
        if guess == wordle:
            print("Congratulations! You guessed the wordle: {}!".format(wordle.capitalize()))
            break
        else:
            attempts -= 1
            feedback = check_guess(wordle, guess)
            print(feedback)
    if attempts == 0:
        print("Out of attempts! The word was {0}.".format(wordle.capitalize()))

start()