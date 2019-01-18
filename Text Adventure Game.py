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
        print(item + ",", end = " ")
    print("\n")

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
time.sleep(2)
print("You tried to stand up, but a strange heaviness in your limbs made you stagger and fall.")
time.sleep(3)
print("Looking down, you see a thick metal band around each of your wrists and ankles.")
time.sleep(3)
print("Each of the rings have five small, red lights on them, with a key hole in the middle.")
time.sleep(3)

while True:
    print("Try to take them off?")
    answer = input()
    if answer == "help":
        commands()
        continue
    if answer == "yes":
        timeLeft -= 1
        print("You tried to wiggle the rings off. Suddenly, one of the five lights on each of the metal rings went out.")
        time.sleep(2)
        print("Startled, you decided to leave the metal rings alone.")
        break
    else:
        print("You decided to not tinker with the metal bands.")
        break
time.sleep(1)
"""

print("You look around. The room is almost bare, except for a small wooden desk in the corner.")
time.sleep(3)
print("You walk to the desk.")
time.sleep(1)
print("On the desk, you see a small tablet.")
time.sleep(2)
print("Curious, you picked it up.")
time.sleep(1)
print("The tablet lit up, and on it you can see the silhouette of a man sitting on a chair")
time.sleep(3)
print("'Hello.' The man spoke.")
time.sleep(1)
print("'You must be wondering where you are, or why you're here.'")
time.sleep(2)
print("'Well, you see, I'm bored.'")
time.sleep(1)
print("And when a sick and twisted man with money to spare is boredasasdf")
time.sleep(1)

print("")
time.sleep(1)
print("")














    
