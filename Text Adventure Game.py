import time
import random

inventory = []
responds = []
global item
timeLeft = 5

def title():
    print(" ██ ▄█▀▓█████▓██   ██▓  ██████ ")
    print(" ██▄█▒ ▓█   ▀ ▒██  ██▒▒██    ▒ ")
    print("▓███▄░ ▒███    ▒██ ██░░ ▓██▄   ")
    print("▓██ █▄ ▒▓█  ▄  ░ ▐██▓░  ▒   ██▒")
    print("▒ ▒▒ ▓▒░░ ▒░ ░  ██▒▒▒ ▒ ▒▓▒ ▒ ░")
    print("░ ░▒ ▒░ ░ ░  ░▓██ ░▒░ ░ ░▒  ░ ░")
    print("░ ░░ ░    ░   ▒ ▒ ░░  ░  ░  ░  ")
    print("░  ░      ░  ░░ ░           ░  ")
    print("              ░ ░              ")

def commands():
    print("Commands: yes, no, front, back, left, right, grab, inventory, use. All are lower case.")
    print("To see commands list again, type help.")

def front():
    print("You chose to keep going straight.")

def back():
    print("You chose to go back.")

def left():
    print("You chose to go left.")

def right():
    print("You chose to go right.")

def grab():
    global item
    global inventory
    inventory += [item]

def inventory():
    print("Inventory:", end = " ")
    for item in inventory:
        print(item)
      

def use():
    global item
    global inventory
    print("You used", item + ".")
    inventory -= item

title()
commands()
"""
print("\n")    
print("You woke up in a dark room, with a pounding headache.")
input()
print("You tried to stand up, but a strange heaviness in your limbs made you stagger and fall.")
input()
print("Looking down, you see a thick metal band around each of your wrists and ankles.")
input()
print("Each of the rings have five small, red lights on them, with a key hole in the middle.")
input()
while True:
    print("Try to take them off?")
    answer = input()
    if answer == "help":
        commands()
        continue
    if answer == "yes":
        timeLeft -= 1
        print("You tried to wiggle the rings off. Suddenly, one of the five lights on each of the metal rings went out.")
        input()
        print("Startled, you decided to leave the metal rings alone.")
        break
    else:
        print("You decided to not tinker with the metal bands.")
        break
input()
"""

print("You look around. The room is almost bare, except for a small wooden desk in the corner.")
input()
print("You walk to the desk.")
input()
print("On the desk, you see a small tablet.")
input()
print("Curious, you picked it up.")
input()
print("The tablet lit up, and on it you can see the silhouette of a man sitting on a chair")
input()
print("'Hello.' The man spoke.")
input()
print("'You must be wondering where you are, or why you're here.'")
input()
print("'Well, you see, I'm bored.'")
input()
print("And when a sick man with lots of money to spare is bored, things can happen.")
input()
while True:
    print("Interrupt him?")
    answer = input()
    if answer == "help:
        commands()
        continue
    if answer == "yes":
        timeLeft -= 1
        interrupts = ["'Please let me go. I won't tell anyone.'", "HELP!", ""
        
        break
    else:
        print("")
        break

print("")
input()
print("")













    
