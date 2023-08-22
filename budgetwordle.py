import random
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)
from os import environ
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
import pygame
from pygame import mixer

pygame.init()
# cmd ( pip install colorama)
# file --> settings --> project --> python interpreter --> + icon and install 'colorama'
mixer.music.load('background2.wav')
mixer.music.play(-1)
# UN
class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

""" 
https://stackoverflow.com/questions/8924173/how-can-i-print-bold-text-in-python#:~:text=In%20Python%2C%20escape%20sequences%20are,want%20to%20represent%20in%20bold.
    Originally looked up how to use bolder text to have the letters pop out more
    Initially used the Fore.(COLOR) command
    Figured setting this to a class and not using Fore would make it less confusing
    Didn't want to go through the hassle of looking up the codes for the colors so this was convenient
"""

# Word List
words = ['which', 'there', 'their', 'about', 'would', 'these', 'other', 'words', 'could', 'write', 'first', 'water', 'after',
          'where', 'right', 'think', 'three', 'years', 'place', 'sound', 'great', 'again', 'still', 'every', 'small', 'found',
         'those', 'never', 'under', 'might', 'while', 'house', 'world', 'below', 'asked', 'going', 'large', 'until', 'along',
         'shall', 'being', 'often', 'earth', 'began', 'since', 'study', 'night', 'light', 'above', 'paper', 'parts', 'young',
         'story', 'point', 'times', 'heard', 'whole', 'white', 'given', 'means', 'music', 'miles', 'thing', 'today', 'later',
         'using', 'money', 'lines', 'order', 'group', 'among', 'learn', 'known', 'space', 'table', 'early', 'trees', 'short',
         'hands', 'state', 'black', 'shown', 'stood', 'front', 'voice', 'kinds', 'makes', 'comes', 'close', 'power', 'lived',
         'vowel', 'taken', 'built', 'heart', 'ready', 'quite', 'class', 'bring', 'round', 'horse', 'shows', 'piece', 'green',
         'stand', 'birds', 'start', 'river', 'tried', 'least', 'field', 'whose', 'girls', 'leave', 'added', 'color', 'third',
         'hours', 'moved', 'plant', 'doing', 'names', 'forms', 'heavy', 'ideas', 'cried', 'check', 'floor', 'begin', 'woman',
         'alone', 'plane', 'spell', 'watch', 'carry', 'wrote', 'clear', 'named', 'books', 'child', 'glass', 'human', 'takes',
         'party', 'build', 'seems', 'blood', 'sides', 'seven', 'mouth', 'solve', 'north', 'value', 'death', 'maybe', 'happy',
         'tells', 'gives', 'looks', 'shape', 'lives', 'steps', 'areas', 'sense', 'speak', 'force', 'ocean', 'speed', 'women',
         'metal', 'south', 'grass', 'scale', 'cells', 'lower', 'sleep', 'wrong', 'pages', 'ships', 'needs', 'rocks', 'eight',
         'major', 'level', 'total', 'ahead', 'reach', 'stars', 'store', 'sight', 'terms', 'catch', 'works', 'board', 'cover',
         'songs', 'equal', 'stone', 'waves', 'guess', 'dance', 'spoke', 'break', 'cause', 'radio', 'weeks', 'lands', 'basic',
         'liked', 'trade', 'fresh', 'final', 'fight', 'meant', 'drive', 'spent', 'local', 'waxes', 'knows', 'train', 'bread',
         'homes', 'teeth', 'coast', 'thick', 'brown', 'clean', 'quiet', 'sugar', 'facts', 'steel', 'forth', 'rules', 'notes',
         'units', 'peace', 'month', 'verbs', 'seeds', 'helps', 'sharp', 'visit', 'woods', 'chief', 'walls', 'cross', 'wings',
         'grown', 'cases', 'foods', 'crops', 'fruit', 'stick', 'wants', 'stage', 'sheep', 'nouns', 'plain', 'drink', 'bones',
         'apart', 'turns', 'moves', 'touch', 'angle', 'based', 'range', 'marks', 'tired', 'older', 'farms', 'spend', 'shoes',
         'goods', 'chair', 'twice', 'cents', 'empty', 'alike', 'style', 'broke', 'pairs', 'count', 'enjoy', 'score', 'shore',
         'roots', 'paint', 'heads', 'shook', 'serve', 'angry', 'crowd', 'wheel', 'quick', 'dress', 'share', 'alive', 'noise',
         'solid', 'cloth', 'signs', 'hills', 'types', 'drawn', 'worth', 'truck', 'piano', 'upper', 'loved', 'usual', 'faces',
         'drove', 'cabin', 'boats', 'towns', 'proud', 'court', 'model', 'prime', 'fifty', 'plans', 'yards', 'prove', 'tools',
         'price', 'sheet', 'smell', 'boxes', 'raise', 'match', 'truth', 'roads', 'threw', 'enemy', 'lunch', 'chart', 'scene',
         'graph', 'doubt', 'guide', 'winds', 'block', 'grain', 'smoke', 'mixed', 'games', 'wagon', 'sweet', 'topic', 'extra',
         'plate', 'title', 'knife', 'fence', 'falls', 'cloud', 'wheat', 'plays', 'enter', 'broad', 'steam', 'atoms', 'press',
         'lying', 'basis', 'clock', 'taste', 'grows', 'thank', 'storm', 'agree', 'brain', 'track', 'smile', 'funny', 'beach',
         'stock', 'hurry', 'saved', 'sorry', 'giant', 'trail', 'offer', 'ought', 'rough', 'daily', 'avoid', 'keeps', 'throw',
         'allow', 'cream', 'laugh', 'edges', 'teach', 'frame', 'bells', 'dream', 'magic', 'occur', 'ended', 'chord', 'false']

# Logo for startup
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

# Function that chooses the word
def choose_word():
    return random.choice(words)

# Function that takes the guess and the wordle and compares them using string indexing. Returns the feedback so the player knows what letters they got
def check_guess(secret_word, guessed_word):
    result = []
    for i in range(len(secret_word)):
        if guessed_word[i] == secret_word[i]:
            result.append(color.BOLD + color.GREEN + guessed_word[i].upper())
        elif guessed_word[i] in secret_word:
            result.append(color.BOLD + color.YELLOW + guessed_word[i].upper())
        else:
            result.append(Fore.WHITE + "_")
    return " ".join(result)

# Function that takes an input and restarts the game depending if the player says yes or no
def replay_ask():
    ask = input("Would you like to restart? Y/N \n").lower()
    if ask == "y":
        start()
    elif ask == "n":
        quit

# Function that runs the game
def start():
    # Sets up base variables as well as introduces the player
    wordle = choose_word()
    print(logo)
    print("\nWelcome to (Budget) Wordle. Guess the 5 letter word.")
    attempts = 6
    # while loop for attempts
    while attempts > 0:
        guess = input("Guess {}: ".format(7 -attempts)).lower()
        # Base cases: if the word is not the same length or if the user correctly guessed the word. Continues the loop or breaks depending on which one
        if len(guess) != len(wordle):
            print("Please enter a 5 letter word")
            continue
        if guess == wordle:
            print("Congratulations! You guessed the wordle: {}!".format(color.BOLD + color.GREEN + wordle.upper()))
            break
        # Only takes place if both base cases are not fulfilled, takes away an attempt and prints the feedback generated by check_guess()
        else:
            attempts -= 1
            feedback = check_guess(wordle, guess)
            print(feedback)
    if attempts == 0:
        print("Out of attempts! The word was {0}.".format(wordle.capitalize()))
    replay_ask()


start()
