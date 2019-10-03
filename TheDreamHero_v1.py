#Python Text RPG#
#The Dream Hero#
#Imports#
import os
import sys
import time
import random
import textwrap
screen_width = 100
## Player Setup ##
class player:
    def __init__(self):
        self.name = ''
        self.location = 'b2'
        self.hp = 0
        self.mp = 0
        self.role = ' '
        self.inventory = ''
        #self.stm = 0
        #self.attack = 0
        #self.defense = 0
        #self.int = 0
        #self.luck = 0
        self.game_over = False
myPlayer = player()
## Title Screen ##
def title_screen_selections():
    option = input("> ")
    if option.lower() == ("play"):
        start_game()
    elif option.lower() == ("help"):
        help_menu()
    elif option.lower() ==("home"):
        title_screen()
    elif option.lower() == ("quit"):
        sys.exit()
    while option.lower() not in ['play', 'help', 'quit']:
        print("Please enter a valid command.")
        option = input("> ")
        if option.lower() == ("play"):
            start_game()
        elif option.lower() ==("home"):
            title_screen()
        elif option.lower() == ("help"):
            help_menu()
        elif option.lower() == ("quit"):
            sys.exit()
def title_screen():
    os.system("cls")
    os.system("mode con cols=100 lines=11")
    title = "The Dream Hero".upper()
    welcome = "Welcome to '{}' a TextRPG!".format(title)
    print("#" * 100)
    print(title.center(100))
    print("#" * 100)
    print("=" * 100)
    print(welcome.center(100))
    print("=" * 100)
    print(("- Play -".upper()).center(100))
    print(("- Help -".upper()).center(100))
    print(("- Quit -".upper()).center(100))
    print("lachance.n copyright2018".rjust(100))
    title_screen_selections()
## Help Menu ##
def help_menu():
    os.system("cls")
    os.system("mode con cols=100 lines=8")
    welcome = "#Help Menu!#".upper()
    print("#" * 100)
    print(welcome.center(100))
    print("#" * 100)
    print(("-Type the commands to perform them-".upper()).center(100))
    print(("-Use 'up', 'down', 'left', 'right', to move around.-".upper()).center(100))
    print(("-Use 'look' to inspect things-".upper()).center(100))
    print(("-Type 'home' to go back-".upper()).center(100))
    title_screen_selections()
## Game Over ##
def game_over():
    os.system("cls")
    os.system("mode con cols=100 lines=8")
    welcome = "#You beat the game!#".upper()
    print("#" * 100)
    print(welcome.center(100))
    print("#" * 100)
    print(("-Congratulations!-".upper()).center(100))
    print(("-You are now The Dream Hero!-".upper()).center(100))
    print(("-I hope you enjoyed this basic game I made :)-".upper()).center(100))
    print(("-Type 'home' to go play again-".upper()).center(100))
    print("lachance.n copyright2018".rjust(100))
    title_screen_selections()
#Inventory
INVENTORY = []
ITEMS = []
home_Item = "A note: 'A place where those seeking adventure depart from.' 'Just don't fall in.'"
harbor_Item = "A note: 'Why would everyone leave without me?' 'I guess I will go for a walk in the woods..'"
forest_Item =  "A note: 'The sacred Volcano to the East might be the perfect place to be alone.'"
volcano_Item = "A burnt note: 'This looks like a perfect spot to rest my head and think.'"
### MAP ###
#|1|2|3|4|5|##Player starts at b2
#------------
#| | | | | |a
#-----------
#| | | | | |b
#------------
#| | | | | |c
#-----------
#| | | | | |d
#-----------
############
ZONENAME = ''
DESCRIPTION = 'description'
EXAMINATION = 'inspect'
ITEM = 'pick up'
SOLVED = False
UP = 'up', 'north'
DOWN = 'down','south'
LEFT = 'left', 'west'
RIGHT = 'right', 'east'
#For Puzzles if I add them
solved_places = {'a1': False, 'a2': False, 'a3': False, 'a4': False, 'a5': False,
                 'b1': False, 'b2': False, 'b3': False, 'b4': False, 'b5': False,
                 'c1': False, 'c2': False, 'c3': False, 'c4': False, 'c5': False,
                 'd1': False, 'd2': False, 'd3': False, 'd4': False, 'd5': False}
#Actual Map#
zonemap = {
    'a1': {
            ZONENAME: "Town Market",
            DESCRIPTION: 'This is where the Town folk come to get their food.',
            EXAMINATION: 'The market seems to only have food.'
                         ' All the merchants are gone.',
            SOLVED: False,
            ITEM: '',
            UP: '',
            DOWN: 'b1',
            LEFT: '',
            RIGHT: 'a2',
    },
    'a2': {
            ZONENAME: "Town Hall",
            DESCRIPTION: 'A place where Town decsions are made.',
            EXAMINATION: 'It seems to be unusually empty.\n'
                         'Where did everyone go?',
            SOLVED: False,
            ITEM: '',
            UP: '',
            DOWN: 'b2',
            LEFT: 'a1',
            RIGHT: 'a3',
        },
    'a3': {
            ZONENAME: "Town North Gate",
            DESCRIPTION: 'The Northern Entrance of the Town',
            EXAMINATION: 'There is no need to leave from this gate.\n'
                         'It leads to nothing.',
            SOLVED: False,
            ITEM: '',
            UP: '',
            DOWN: 'b3',
            LEFT: 'a2',
            RIGHT: 'a4',
        },
    'a4': {
            ZONENAME: "Town Pub",
            DESCRIPTION: 'A place to get some grub and an ale.',
            EXAMINATION: 'The Barkeep seems to be missing.',
            SOLVED: False,
            ITEM: '',
            UP: '',
            DOWN: 'b4',
            LEFT: 'a3',
            RIGHT: 'a5',
        },
    'a5': {
            ZONENAME: "Town Library",
            DESCRIPTION: 'Where the nerds hang out.',
            EXAMINATION: 'The librarian is missing.\n'
                         'The books still remain.\n'
                         'There seems to be a book left open.',
            SOLVED: False,
            ITEM: '',
            UP: '',
            DOWN: 'b5',
            LEFT: 'a4',
            RIGHT: '',
        },
    'b1': {
            ZONENAME: "Neighbor",
            DESCRIPTION: 'Your bestfriend lives here',
            EXAMINATION: 'Your friend seems to not be home right now.\n'
                         'A candle is burning, they may be close by.',
            SOLVED: False,
            ITEM: '',
            UP: 'a1',
            DOWN: 'c1',
            LEFT: '',
            RIGHT: 'b2',
        },
    'b2': {
            ZONENAME: 'Home',
            DESCRIPTION: 'This is your home.',
            EXAMINATION: 'Nothing has changed.',
            SOLVED: False,
            ITEM: home_Item,
            UP: 'a2',
            DOWN: 'c2',
            LEFT: 'b1',
            RIGHT: 'b3',
        },
    'b3': {
            ZONENAME: "Town South Gate",
            DESCRIPTION: 'The Southern Gate of the Town',
            EXAMINATION: 'This will be you to un-explored territories.',
            SOLVED: False,
            ITEM: '',
            UP: 'a3',
            DOWN: 'c3',
            LEFT: 'b2',
            RIGHT: 'b4',
        },
    'b4': {
            ZONENAME: "Town Square",
            DESCRIPTION: 'A gathering place for the Town Folk',
            EXAMINATION: 'It appears to be empty.\n'
                         'There are a few dogs walking around.\n'
                         'Maybe the dogs know where the Town Folk went.',
            SOLVED: False,
            ITEM: '',
            UP: 'a4',
            DOWN: 'c4',
            LEFT: 'b3',
            RIGHT: 'b5',
        },
    'b5': {
            ZONENAME: "Town Church",
            DESCRIPTION: 'A place of prayer.',
            EXAMINATION: 'There appears texted painted across the wall'
                         "'The end is upon us...'\n"
                         "'If only there was someone to save us.'",
            SOLVED: False,
            ITEM: '',
            UP: 'a5',
            DOWN: 'c5',
            LEFT: 'b4',
            RIGHT: '',
        },
    'c1': {
            ZONENAME: "Foggy Forest",
            DESCRIPTION: 'A creepy wooded area',
            EXAMINATION: 'This place seems like it might be important later.',
            SOLVED: False,
            ITEM: forest_Item,
            UP: 'b1',
            DOWN: 'd1',
            LEFT: '',
            RIGHT: 'c2',
        },
    'c2': {
            ZONENAME: "Soul Swamp",
            DESCRIPTION: 'The resting place of souls',
            EXAMINATION: 'The swamp appears to not have any souls in it.\n'
                         'This very unsual...',
            SOLVED: False,
            ITEM: '',
            UP: 'b2',
            DOWN: 'd2',
            LEFT: 'c1',
            RIGHT: 'c3',
        },
    'c3': {
            ZONENAME: "Grassy Field",
            DESCRIPTION: 'description',
            EXAMINATION: 'inspect',
            SOLVED: False,
            ITEM: '',
            UP: 'b3',
            DOWN: 'd3',
            LEFT: 'c2',
            RIGHT: 'c4',
        },
    'c4': {
            ZONENAME: "Dry Desert",
            DESCRIPTION: 'description',
            EXAMINATION: 'inspect',
            SOLVED: False,
            ITEM: '',
            UP: 'b4',
            DOWN: 'd4',
            LEFT: 'c3',
            RIGHT: 'c5',
        },
    'c5': {
            ZONENAME: "Hot Volcano",
            DESCRIPTION: 'description',
            EXAMINATION: 'inspect',
            SOLVED: False,
            ITEM: volcano_Item,
            UP: 'b5',
            DOWN: 'd5',
            LEFT: 'c4',
            RIGHT: '',
        },
    'd1': {
            ZONENAME: "Light House",
            DESCRIPTION: 'description',
            EXAMINATION: 'inspect',
            SOLVED: False,
            ITEM: '',
            UP: 'c1',
            DOWN: '',
            LEFT: '',
            RIGHT: 'd2',
        },
    'd2': {
            ZONENAME: "Broken Bridge",
            DESCRIPTION: 'description',
            EXAMINATION: 'inspect',
            SOLVED: False,
            ITEM: '',
            UP: 'c2',
            DOWN: '',
            LEFT: 'd1',
            RIGHT: 'd3',
        },
    'd3': {
            ZONENAME: "Rocky Beach",
            DESCRIPTION: 'description',
            EXAMINATION: 'inspect',
            SOLVED: False,
            ITEM: '',
            UP: 'c3',
            DOWN: '',
            LEFT: 'd2',
            RIGHT: 'd4',
        },
    'd4': {
            ZONENAME: "Harbor",
            DESCRIPTION: 'description',
            EXAMINATION: 'inspect',
            SOLVED: False,
            ITEM: harbor_Item,
            UP: 'c4',
            DOWN: '',
            LEFT: 'd3',
            RIGHT: 'd5',
        },
    'd5': {
            ZONENAME: "Tall Cliff",
            DESCRIPTION: 'description',
            EXAMINATION: 'inspect',
            SOLVED: False,
            ITEM: '',
            UP: 'c5',
            DOWN: '',
            LEFT: 'd4',
            RIGHT: '',
        }
}
## Game Interactivity ##
def print_map():
    os.system("cls")
    os.system("mode con cols=100 lines=20")
    print("\n")
    print(" ### MAP! ### ".center(100))
    print("#|1|2|3|4|5|##".center(100))
    print("#------------#".center(100))
    print("#| | | | | |a#".center(100))
    print("#------------#".center(100))
    print("#| | | | | |b#".center(100))
    print("#------------#".center(100))
    print("#| | | | | |c#".center(100))
    print("#------------#".center(100))
    print("#| | | | | |d#".center(100))
    print("#------------#".center(100))
    print("##############".center(100))
    print("\n")
def print_character_inventory():
    class_stats1 = "Warrior: HP=150, MP=50\n"
    class_stats2 = "Mage: HP=50, MP=150\n"
    class_stats3 = "Paladin: HP=75, MP=75\n"
    os.system("cls")
    os.system("mode con cols=100 lines=20")
    print("=" * 100)
    if myPlayer.role == 'warrior':
        for character in class_stats1:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(0.03)
    elif myPlayer.role == 'mage':
        for character in class_stats2:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(0.03)
    elif myPlayer.role == 'paladin':
        for character in class_stats2:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(0.03)
    print("Inventory: \n")
    if home_Item in INVENTORY:
        print("\n".join(str(x) for x in INVENTORY))
    elif INVENTORY == []:
        print("You have no items in your inventory.")
    print("=" * 100)
    time.sleep(.5)
    print("Type 'exit' to leave your inventory\n")
    exit = input("> ")
    if exit == 'exit':
        os.system("cls")
        os.system("mode con cols=100 lines=20")
    while exit != 'exit':
        print("That wasn't 'exit'")
        print("Type 'exit' to leave your inventory\n")
        exit = input("> ")
        if exit == 'exit':
            os.system("cls")
            os.system("mode con cols=100 lines=10")
def print_location():
    location = zonemap[myPlayer.location][ZONENAME]
    print('\n' + ("#" * (4 + len(location))))
    print("# " + str(location) + " #")
    print("# " + zonemap[myPlayer.location][DESCRIPTION] + " #")
    print("# " + myPlayer.location + " #")
    print("#" * (4 + len(location)))
def print_character_stats():
    class_stats1 = "Warrior: HP=150, MP=50\n"
    class_stats2 = "Mage: HP=50, MP=150\n"
    class_stats3 = "Paladin: HP=75, MP=75\n"
    class_def1 = "The Warrior is battle hardened and always ready for blood\n"
    class_def2 = "The Mage has seen many conflicts, but approaches with an intellectual strategy.\n"
    class_def3 = "The Paladin is a protector of many, and will let noting stand in his way in being such.\n"
    print("-" * 100)
    for character in class_stats1:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.03)
    for character in class_stats2:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.03)
    for character in class_stats3:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.03)
    for character in class_def1:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.06)
    for character in class_def2:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.06)
    for character in class_def3:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.06)
    print("-" * 100)
def prompt():
    acceptable_actions = ['move', 'go', 'walk', 'quit', 'examine', 'inspect', 'search', 'look', 'location', 'title', 'home', 'map', 'inventory', 'bag', 'self', 'pick up', 'item']
    print("\n" + "=" * 100)
    print("What would you like to do?")
    print("Type 'options' for what you can do.")
    action = input("> ")
    if action.lower() == 'options':
        print(acceptable_actions)
        action = input("> ")
    while action.lower() not in acceptable_actions and not 'options':
        print("Unknown action, try again.\n")
        action = input("> ")
    if action.lower() == 'quit':
        sys.exit()
    elif action.lower() in acceptable_actions[:2]:
        player_move(action.lower())
    elif action.lower() in acceptable_actions[4:7]:
        player_examine(action.lower())
    elif action.lower() in acceptable_actions[8]:
        print_location()
    elif action.lower() in acceptable_actions[9:10]:
        title_screen_selections()
    elif action.lower() in acceptable_actions[11]:
        print_map()
    elif action.lower() in acceptable_actions[12:14]:
        print_character_inventory()
    elif action.lower() in acceptable_actions[15:16]:
        item_pick_up()
def player_move(myAction):
    ask = "Where would you like to move to?\n"
    dest = input(ask)
    if dest.lower() in ['up', 'north']:
        destination = zonemap[myPlayer.location][UP]
        if destination == '':
            print("I am sorry, but you cannot go that way.")
            dest = input(ask)
        else:
            movement_handler(destination)
    elif dest.lower() in ['down', 'south']:
        destination = zonemap[myPlayer.location][DOWN]
        if destination == '':
            print("I am sorry, but you cannot go that way.")
            dest = input(ask)
        else:
            movement_handler(destination)
    elif dest.lower() in ['right', 'east']:
        destination = zonemap[myPlayer.location][RIGHT]
        if destination == '':
            print("I am sorry, but you cannot go that way.")
            dest = input(ask)
        else:
            movement_handler(destination)
    elif dest.lower() in ['left', 'west']:
        destination = zonemap[myPlayer.location][LEFT]
        if destination == '':
            print("I am sorry, but you cannot go that way.")
            dest = input(ask)
        else:
            movement_handler(destination)
def movement_handler(destination):
    print("\n" + "you've arrived at the, {}.".format(destination))
    myPlayer.location = destination
    print_location()
def player_examine(action):
    examination = zonemap[myPlayer.location][EXAMINATION]
    if zonemap[myPlayer.location][SOLVED]:
        print("You have already exhausted this zone")
    else:
        print('\n' + ("#" * (4 + len(examination))))
        print(zonemap[myPlayer.location][EXAMINATION])
        print("#" * (4 + len(examination)))
def item_pick_up():
    item = zonemap[myPlayer.location][ITEM]
    if item != '':
        INVENTORY.append(item)
        myPlayer.inventory = INVENTORY
        print('\n' + ("#" * (4 + len(item))))
        print(zonemap[myPlayer.location][ITEM])
        print("#" * (4 + len(item)))
    else:
        print("There does not appear to be an item here.")
#Game functionality#
def start_game():
    character_create()
    intro()
    welcome_home()
    while myPlayer.game_over is False:
        prompt()
        if home_Item and harbor_Item and forest_Item and volcano_Item in INVENTORY:
            myPlayer.game_over = True
    time.sleep(2)
    os.system("cls")
    os.system("mode con cols=100 lines=5")
    print("It was all just a dream..")
    time.sleep(2)
    game_over()
def character_create():
    self = myPlayer
    warriorStatement1 = 'A warrior huh? I guess it is true what they say, you do enjoy killing.\n'
    warriorStatement2 = 'I guess in a time like now that is a good thing.\n'
    mageStatement1 = 'I should have expected you to train to be a mage.\n'
    mageStatement2 = 'The role that intellect plays in your life has always been obvious.\n'
    paladinStatement1 = 'A mix between battle ready and intellect?\n'
    paladinStatement2 = 'This does seem like the perfect mix for you.\n'
    valid_class = ["warrior", "mage", "paladin"]
    os.system("mode con cols=100 lines=20")
    os.system('cls')
    #What is your name
    question1 = "Tell me?\n"
    question1added = "What is your name?\n"
    for character in question1:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    for character in question1added:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.04)
    player_name = input("> ")
    myPlayer.name = player_name
    statement1 = 'I am glad you still remember who you are.'

    #Assign class
    question2 = "Forgive me {},\nWhat class did you train to become during your time away?\n".format(myPlayer.name)
    question2added = "(You can choose 'warrior', 'mage', 'paladin')\n"
    for character in question2:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    for character in question2added:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.01)
    print_character_stats()
    player_role = input("> ")
    if player_role.lower() in valid_class:
        myPlayer.role = player_role.lower()
    while player_role.lower() not in valid_class:
        player_role = input("> ")
        if player_role in valid_class:
            myPlayer.role = player_role.lower()
    #Class Stats
    if myPlayer.role == 'warrior':
        for character in warriorStatement1:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(0.05)
        for character in warriorStatement2:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(0.05)
        time.sleep(1.0)
        self.hp = 150
        self.mp = 50
    elif myPlayer.role == 'mage':
        for character in mageStatement1:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(0.05)
        for character in mageStatement2:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(0.05)
        time.sleep(1.0)
        self.hp = 50
        self.mp = 150
    elif myPlayer.role == 'paladin':
        for character in paladinStatement1:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(0.05)
        for character in paladinStatement2:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(0.05)
        time.sleep(1.0)
        self.hp = 75
        self.mp = 75
def welcome_home():
    os.system('cls')
    os.system("mode con cols=100 lines=7")
    statement1 = "Welcome back home, {} the {}.\n".format(myPlayer.name, myPlayer.role)
    statement2 = 'Hopefully your time away from The Town has served you well.\n'
    for character in statement1:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    for character in statement2:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.07)
    speech1 = "You haven't changed a bit.\n"
    speech2 = "I know it has been quite sometime..\n"
    speech3 = "Hopefully you remember your way...\n"
    for character in speech1:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    for character in speech2:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    for character in speech3:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.06)
    speech4 = "Good luck {}, this place needs you now more than ever.".format(myPlayer.name)
    for character in speech4:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.06)
    time.sleep(0.85)
    os.system("mode con cols=100 lines=20")
    os.system('cls')
    print("#" * 100)
    print("You awaken in your bed.".center(100))
    print("It was all just a dream.".center(100))
    print("#" * 100)
def intro():
    #Intro to the universe
    os.system('cls')
    os.system("mode con cols=100 lines=10")
    lore1 = 'The Town was once a lively place and home to many.\n'
    lore2 = 'Now there seems to have been something that caused eveyone to disappear.\n'
    lore3 = 'The Town is a nexus and has always been such.\n'
    lore4 = 'It is possible that something wanted to dismantle the uptopia.\n'
    lore5 = 'It is your destiny {} to save The Town, your home.\n'.format(myPlayer.name)
    lore6 = 'There is no need to worry {} this is why you trained to be a {}'.format(myPlayer.name, myPlayer.role)
    for character in lore1:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    for character in lore2:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    for character in lore3:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    for character in lore4:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    for character in lore5:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    time.sleep(.8)
    for character in lore6:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.08)
    time.sleep(1.2)
#Start Game
title_screen()
