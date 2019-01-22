import time
import random

inventory = []
responses = []
rooms = []
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
    
def checkInput():
    global answer
    if answer == "left":
        left()
    elif answer == "right":
        right()
    elif answer == "front":
        front()
    elif answer == "back":
        back()
    elif answer == "help":
        commands()
    elif answer == "grab":
        grab()
    elif answer == "inventory":
        inventory()
    elif answer == "use":
        use()
     

title()
commands()

print("\n")    
print("You woke up in a dark room, with a pounding headache.")
input()
print("You tried to stand up, but a strange heaviness in your limbs made you stagger and fall.")
input()
print("Looking down, you see a thick metal band around each of your wrists and ankles.")
input()
print("Each of the rings have five small, red lights on them, with a key hole in the middle.")
input()
print("Try to take them off?")
answer = input()
if answer == "help":
    commands()
if answer == "yes":
    timeLeft -= 1
    responses += ["tinker"]
    print("You tried to wiggle the rings off. Suddenly, one of the five lights on each of the metal rings went out.")
    input()
    print("Startled, you decided to leave the metal rings alone.")
else:
    print("You decided to not tinker with the metal bands.")
input()

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
print("'And when a sick man with lots of money to spare is bored, things can happen.'")
input()
print("Say something?")
answer = input()
checkInput()
if answer == "yes":
    timeLeft -= 1
    responses += ["interrupt"]
    interrupts = ["'Please let me go. I won't tell anyone.' You pleaded.", "'HELP!' You screamed out.", "'Please don't hurt me.' You pleaded."]
    respond = random.choice(interrupts)
    print(respond)
    input()
    if timeLeft == 5:
        print("Just as you spoke out, one of the red lights on each of the rings went out.")
        input()
    else:
        print("Just as you spoke out, another one of the red lights on each of the rings went out.")
        input()
    print("'I don't like to be interrupted.' The man frowned in displeasure.")
    input()
    print("'That is a small warning. Next time I won't be so nice.'")
    input()
    print("'As I was saying, I wanted to play a game.'")
    input()
    
elif answer == "no":
    print("'Since I'm bored, I've decided that I want to play a game.'")
    input()
print("'You see those metal bands? They have tiny time bombs planted inside. Each red dot represent an hour left before the bombs go off.'")
input()
    if timeLeft == 3:
        print("'Due to your mistakes from earlier, you now only have 3 hours left. Before the bombs go... boom.'")
        input()
    elif timeLeft == 4:
        if "tinker" in responses:
            print("'Since you tried to mess with the rings, I had to take an hour off. Now you have 4 hours left, before the bombs go... boom.'")
            input()
        elif "interrupt" in responses:
            print("'Since I was so rudely interrupted, I had to take an hour off. Now you have 4 hours left, before the bombs go... boom.'")
            input()
    elif timeLeft == 5:
        print("'You have 5 hours left, before the bombs go... boom.'")
        input()
print("The man chuckled, his laughter resonating throughout the empty room. The eerie sound sends a chill down your spines.")
input()
print("'If you don't want to die here, you'll have to find 5 keys. 4 for the rings, and 1 for the front door.'")
input()
print("'")

            

print("")
input()
print("")













    
