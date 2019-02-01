import time
import random
import sys

inventory = []
responses = []
roomsEntered = ["room8"]
global room
global item
timeLeft = 5
global timeSpent
keys = 0

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
    print("Commands: yes, no, north, south, east, west, grab, inventory, use. All are lower case.")
    print("To see commands list again, type help.")

def north():
    print("You chose to go north.")

def south():
    print("You chose to go south.")

def west():
    print("You chose to go west.")

def east():
    print("You chose to go east.")

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
    if answer == "help":
        commands()
    elif answer == "inventory":
        inventory()

        
def checkTime():
    if timeSpent >= 6:
    	timeLeft -= 1
        print("You now have", timeLeft "hours left.")
    if timeLeft == 0 and keys != 5:
        if keys !=5:
            print("Suddenly, a voice sounded over your head.")
            input()
            print("'Tic toc. You're out of time.'")
            input()
            print("'How very unfortunate.' The voice laughed.")
            input()
            print("'Goodbye.'")
            input()
	    	print("As soon as the voice finished talking, the last red light went out.")
	    	input()
            print("Boom. Everything went black.")
            input()
            print("You died.")
            sys.exit()
        elif keys == 5 and room != "room2":
            print("Suddenly, a voice sounded over your head.")
            input()
            print("'Tic toc. You're out of time.'")
            input()
            print("'How very unfortunate.' The voice laughed.")
            input()
            print("'You were so close too. You just needed to make it to the door.'")
            input()
            print("'However, rules are rules.'")
            input()
            print("'Goodbye.'")
            input()
	    	print("As soon as the voice finished talking, the last red light went out.")
	    	input()
            print("Boom. Everything went black.")
            input()
            print("You died.")
            sys.exit()
        

def room1():
    timeSpent += 1
    global room
    global keys
    checkTime()
    if "key1" in inventory:
        print("You've already gotten everything from this room.")
        input()
        while True:
            print("Where would you like to go?")
            answer = input()
            checkInput()
            if answer == "south":
                exit
            else:
                print("You cannot go that way.")
                continue
        south()
        return room = "room4"   
    
    elif "keyForChest1" in inventory and "room1" in roomsEntered:
        print("After entering the room, you immediately went to the chest.")
        input()
        print("You took out the red key, and inserted it into the lock.")
        inventory -= ["keyForChest1"]
        input()
        print("Upon opening the chest, you found two keys for the rings.")
        inventory += ["key1", "key2"]
        keys += 2
        input()
        print("You have obtained 2 keys.")
        input()
		print("You now have", keys, "keys.")
		input()
        while True:
            print("Where would you like to go next?")
            answer = input()
            checkInput()
            if answer == "south":
                exit
            else:
                print("You cannot go that way.")
                continue
        south()
        return room = "room4"
    
    elif "room1" in roomsEntered:
        print("You need to find the key for the red chest.")
        input()
        while True:
            print("Where would you like to go?")
            answer = input()
            checkInput()
            if answer == "south":
                exit
            else:
                print("You cannot go that way.")
                continue
        south()
        return room = "room4"
    
    else:
        print("You walked into an empty room with a large, red chest in the center.")
        input()
        print("You walked to the chest.")
        input()
        print("Kneeling down, you noticed that there is a lock locking the chest.")
        input()
        print("You would need a key.")
        input()
        print("Search room for key?")
        answer = input()
        checkInput()
        if answer == "yes":
	    timeSpent += 1
            print("You walk around the room, peering into the corners.")
            input()
            print("There is no key in sight.")
            input()
            print("It seems you'll have to look for the key for the chest elsewhere.")
            input()
        elif answer == "no":
            print("You decide to not search for the key in this empty room.")
            input()
        while True:
            print("Where would you like to go?")
            answer = input()
            checkInput()
            if answer == "south":
                exit
            else:
                print("You cannot go that way.")
                continue
        south()
        return room = "room4"
    
    if "room1" not in roomsEntered:
        roomsEntered += ["room1"]

        
def room2():
    timeSpent += 1
    global room
    global keys
    checkTime()
    if "room2" not in roomsEntered:
        if keys == 5:
            print("A large metal door greets you as soon as you entered the room.")
            input()
            print("You looked down, and in your hands you held 5 keys.")
            input()
            print("One by one, you unlocked the metal rings on your wrists and ankles, until only one key is left.")
            input()
            print("Slowly, you inserted the final key into the lock on the door, and turn the key.")
            input()
            print("You opened the door.")
            sys.exit()
        elif keys != 5:
            print("A large metal door greets you as soon as you entered the room.")
            input()
            print("'This must be the exit.' You thought to yourself.")
            input()
            if keys == 0:
                print("However, you do not have any keys.")
                input()
                print("You would need to go else where to search for the keys.")
                input()
            else:
                print("However, you do not have enough keys.")
                input()
                print("You would need to go elsewhere to search for more keys.")
                input()
            while True:
                print("Where would you like to go?")
                answer = input()
                checkInput()
                if answer == "south" or answer == "east":
                    exit
                else:
                    print("You cannot go that way.")
                    continue
                    
            if answer == "south":
                south()
                return room = "room5"
            elif answer == "east":
                east()
                return room = "room3"
				
	elif "room2" in roomsEntered:
		if keys == 5:
			print("You walked into the room with the exit.")
			input()
			print("You looked down, and in your hands you held 5 keys.")
            		input()
            		print("One by one, you unlocked the metal rings on your wrists and ankles, until only one key is left.")
            		input()
            		print("Slowly, you inserted the final key into the lock on the door, and turn the key.")
            		input()
            		print("You opened the door.")
            		sys.exit()
		elif keys != 5:
			print("You walked into the room with the exit.")
			input()
			print("However, you do not have enough keys.")
			input()
		while True:
                	print("Where would you like to go to search for more keys?")
                	answer = input()
                	checkInput()
                	if answer == "south" or answer == "east":
                		exit
                	else:
                    		print("You cannot go that way.")
                    		continue
                    
            	if answer == "south":
                	south()
                	return room = "room5"
            	elif answer == "east":
                	east()
                	return room = "room3"

    if "room2" not in roomsEntered:
        roomsEntered.append("room2")
        
		
		
def room3():
	timeSpent += 1
    global room
    global keys
    checkTime()
	if "key3" in inventory:
		print("You've already gotten everything from this room.")
        input()
        while True:
            print("Where would you like to go?")
            answer = input()
            checkInput()
            if answer == "west":
                exit
            else:
                print("You cannot go that way.")
                continue
        west()
        return room = "room2"
	elif "room3" in roomsEntered:
		print("You walked into the room with the lone drawer", random.choice("again", "once more", "once again") + ".")
		input()
		print("Search the drawer?")
		answer = input()
		checkInput()
		if answer == "yes":
			timeSpent += 1
			print("You decided to look through the drawer once more.")
			input()
			print("Unfortunately, there is no key in sight.")
			input()
			print("Just as you're about to give up, you noticed something shiny in a dark corner of the room.")
			input()
			print("Curious, you went to check it out.")
			input()
			print("Walking closer, you can see that the shiny object is a key.")
			input()
			inventory += ["key3"]
			keys += 1
			print("You have obtained a key.")
			input()
			print("You now have", keys, "keys.")
			input()
		elif answer == "no":
			print("You decided to search elsewhere.")
		while True:
            		print("Where would you like to go?")
            		answer = input()
            		checkInput()
            		if answer == "west":
                		exit
            		else:
                		print("You cannot go that way.")
                		continue
        	west()
        	return room = "room2"
		
		
		
		
		
		
	
	elif "room3" not in roomsEntered:
		print("As you walked into the room, you noticed that there is a lone drawer at the left side of the wall.")
		input()
		print("Search the drawer?")
		input()
		answer = input()
		checkInput()
		if answer == "yes":
			timeSpent += 1
			print("You started searching the drawer, opening each compartment, looking carefully for any sign of the key.")
			input()
			print("However, after combing through the drawer twice, you still couldn't any keys.")
			input()
			print("Search some more?")
			answer = input()
			checkInput()
			if answer == "yes":
				timeSpent += 1
				print("You decided to look through the drawer once more.")
				input()
				print("Unfortunately, there is no key in sight.")
				input()
				print("Just as you're about to give up, you noticed something shiny in a dark corner of the room.")
				input()
				print("Curious, you went to check it out.")
				input()
				print("Walking closer, you can see that the shiny object is a key.")
				input()
				inventory += ["key3"]
				keys += 1
				print("You have obtained a key.")
				input()
				print("You now have", keys, "keys.")
				input()
			elif answer == "no":
				print("You decided to search elsewhere.")
				input()
		elif answer == "no":
			print("You decided to search elsewhere.")
			input()
		while True:
            		print("Where would you like to go?")
            		answer = input()
            		checkInput()
            		if answer == "west":
                		exit
            		else:
                		print("You cannot go that way.")
                		continue
        	west()
        	return room = "room2"
		
def room4():
	timeSpent += 1
	global room
	global keys
	checkTime()
	if "room4" in roomsEntered:
		print("You walked into the room with the envelopes.")
		input()
		print("Would you like to search them again?")
		answer = input()
		checkInput()
		if answer == "yes":
			timeSpent += 3
			print("You spend a long time painstakingly looking through each and every one of the envelopes.")
			input()
			print("Unfortunately, luck doesn't seem to be on your side this time, as no key is found.")
			input()
			print("You decided to go elsewhere.")
		elif answer == "no":
			print("You decided not to waste time searching.")
			input()
		while True:
            print("Where would you like to go?")
            answer = input()
         	checkInput()
            if answer == "north" or answer == "south" or answer == "east":
                exit
            else:
                print("You cannot go that way.")
                continue
       if answer == "north":
			north()
			return room = "room1"
		elif answer == "south":"
			south()
			return room = "room7"
		elif answer == "east":
			east()
			return room = "room5"
			
			
	
	
	
	elif "room4" not in roomsEntered:
		roomsEntered += ["room4']
		print("")
						 
						 
				
	
	
	



title()
commands()

room = "room8"
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
checkInput()
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
				 
				 
				 
while True:
	if room == "room1":
		room1()
	elif room == "room2":
		room2()
	elif room == "room3":
		room2()
	elif room == "room4":
		room2()
		
				 
			













    
