#Python Text RPG#
#The Dream Hero#
#Imports#
import os
import sys
import time
import random
import textwrap
SCREEN_WIDHT = 150
SCREEN_HEIGHT = 20
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
#Classes
##Base Game Character
class Character:
    def __init__(self, name, hp, mp, stm, thaco, ac, location, inventory, exp, level):
        self.name = name
        self.hp = hp
        self.mp = mp
        self.stm = stm
        self.thaco = thaco
        self.ac = ac
        self.location = location
        self.inventory = inventory
        self.exp = exp
        self.level = level
#Main Player
class Player(Character):
    LEVEL_UP = 25
    def __init__(self, hp, mp, stm, game_over):
        print("What is your name?".center(SCREEN_WIDHT))
        super().__init__(input("\n>"), hp, mp, stm, 20, 10, 'b2', {}, 0, 1)
        self.game_over = False
#Hero Classes
class Knight(Player):
    PROF = "knight"
    MAX_HP = 150
    MAX_MP = 25
    MAX_STM = 125
    MAX_DMG = 60
    def __init__(self):
        super().__init__(150, 25, 125, False)
class Mage(Player):
    PROF = "mage"
    MAX_HP = 75
    MAX_MP = 150
    MAX_STM = 75
    MAX_DMG = 75
    def __init__(self):
        super().__init__(50, 150, 100, False)
class Paladin(Player):
    PROF = "paladin"
    MAX_HP = 100
    MAX_MP = 100
    MAX_STM = 100
    MAX_DMG = 50
    def __init__(self):
        super().__init__(100, 100, 100, False)
#Enemy Classes
class BaseEnemy(Character):
    MAX_DMG = 10
    MAX_HP = 75
    def __init__(self):
        location = ['a1', 'a2', 'a3', 'a4', 'a5',
                                  'b1', 'b3', 'b4', 'b5'
                                  'c1', 'c2', 'c3', 'c4', 'c5'
                                  'd1', 'd2', 'd3', 'd4', 'd5']
        super().__init__("Dream Watchers", 75, 0, 200, 10, 4, location, {}, 5, 1)
class MediumEnemy(Character):
    MAX_DMG = 20
    MAX_HP = 125
    def __init__(self):
        location = ['a1', 'a2', 'a3', 'a4', 'a5',
                                  'b1', 'b3', 'b4', 'b5'
                                  'c1', 'c2', 'c3', 'c4', 'c5'
                                  'd1', 'd2', 'd3', 'd4', 'd5']
        super().__init__("Dream Keepers", 125, 50, 225, 13, 6, location, {}, 10, 2)
class HardEnemy(Character):
    MAX_DMG = 40
    def __init__(self):
        location = ['c1', 'c5',
                                  'd1', 'd4']
        super().__init__("Dream Guardians", 175, 125, 300, 16, 8, location, {}, 20, 3)
def enemy_spawn():
    roll = die(100)
    if roll <= 60:
        ranmob = BaseEnemy()
        return ranmob
    elif roll >= 66:
        ranmob = MediumEnemy()
        return ranmob
    elif roll >= 61 and roll <= 65:
        ranmob = HardEnemy()
        return ranmob
## Functions ##
def start_game():
    while myPlayer.game_over == False:
        check_game_over()
        prompt()
        check_game_over()
    if myPlayer.game_over == True:
        game_over()
def check_game_over():
    if myPlayer.hp <= 0:
        myPlayer.game_over = True
def die(sides=6):
    return random.randint(1,sides)
def set_screen():
    os.system("cls")
    os.system("mode con cols=150 lines=25")
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
    set_screen()
    title = "The Dream Hero".upper()
    welcome = "Welcome to '{}' a TextRPG!".format(title)
    print("#" * SCREEN_WIDHT)
    print(title.center(SCREEN_WIDHT))
    print("#" * SCREEN_WIDHT)
    print("=" * SCREEN_WIDHT)
    print(welcome.center(SCREEN_WIDHT))
    print("=" * SCREEN_WIDHT)
    print(("- Play -".upper()).center(SCREEN_WIDHT))
    print(("- Help -".upper()).center(SCREEN_WIDHT))
    print(("- Quit -".upper()).center(SCREEN_WIDHT))
    print("lachance.n copyright2018".rjust(SCREEN_WIDHT))
    title_screen_selections()
## Help Menu ##
def help_menu():
    set_screen()
    welcome = "#Help Menu!#".upper()
    print("#" * SCREEN_WIDHT)
    print(welcome.center(SCREEN_WIDHT))
    print("#" * SCREEN_WIDHT)
    print(("-Type the commands to perform them-".upper()).center(SCREEN_WIDHT))
    print(("-Use 'up', 'down', 'left', 'right', to move around.-".upper()).center(SCREEN_WIDHT))
    print(("-Use 'look' to inspect things-".upper()).center(SCREEN_WIDHT))
    print(("-Type 'home' to go back-".upper()).center(SCREEN_WIDHT))
    title_screen_selections()
## Game Over ##
def game_over():
    set_screen()
    welcome = "#You beat the game!#".upper()
    print("#" * SCREEN_WIDHT)
    print(welcome.center(SCREEN_WIDHT))
    print("#" * SCREEN_WIDHT)
    print(("-Congratulations!-".upper()).center(SCREEN_WIDHT))
    print(("-You are now The Dream Hero!-".upper()).center(SCREEN_WIDHT))
    print(("-I hope you enjoyed this basic game I made :)-".upper()).center(SCREEN_WIDHT))
    print(("-Type 'home' to go play again-".upper()).center(SCREEN_WIDHT))
    print("lachance.n copyright2018".rjust(SCREEN_WIDHT))
    title_screen_selections()
## Game functionality ##
def print_character_stats():
    set_screen()
    name = str(myPlayer.name)
    hp = str(myPlayer.hp)
    mp = str(myPlayer.mp)
    stm = str(myPlayer.stm)
    thaco = str(myPlayer.thaco)
    ac = str(myPlayer.ac)
    dmg = str(myPlayer.MAX_DMG)
    exp = str(myPlayer.exp)
    level = str(myPlayer.level)
    print("-" * 150)
    print(("Name: {}".format(name)).rjust(int(SCREEN_WIDHT / 4)).upper())
    print(("HP: {}".format(hp)).rjust(int(SCREEN_WIDHT / 4)).upper())
    print(("MP: {}".format(mp)).rjust(int(SCREEN_WIDHT / 4)).upper())
    print(("STM: {}".format(stm)).rjust(int(SCREEN_WIDHT / 4)).upper())
    print(("THACO: {}".format(thaco)).rjust(int(SCREEN_WIDHT / 4)).upper())
    print(("AC: {}".format(ac)).rjust(int(SCREEN_WIDHT / 4)).upper())
    print(("MAX DMG: {}".format(dmg)).rjust(int(SCREEN_WIDHT / 4)).upper())
    print(("EXP: {}".format(exp)).rjust(int(SCREEN_WIDHT / 4)).upper())
    print(("LEVEL: {}".format(level)).rjust(int(SCREEN_WIDHT / 4)).upper())
    print("-" * 150)
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
def print_location():
        location = zonemap[myPlayer.location][ZONENAME]
        print('\n' + ("#" * (4 + len(location))))
        print("# " + str(location) + " #")
        print("# " + zonemap[myPlayer.location][DESCRIPTION] + " #")
        print("# " + myPlayer.location + " #")
        print("#" * (4 + len(location)))
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
    location = zonemap[myPlayer.location][ZONENAME]
    print("\n" + "you've arrived at, {}.".format(location))
    print("There is a {} that you need to try and fight!".format(randEnemy.name))
    myPlayer.location = destination
    print_location()
def player_Attack():
    print("Type 'roll' to attack")
    attack = input(">")
    if attack.lower() == 'roll':
        roll = die(24)
        if roll >= myPlayer.thaco - randEnemy.ac:
            print("You hit!")
            rollD = die(myPlayer.MAX_DMG)
            print("For", rollD, "damage")
            randEnemy.hp = randEnemy.hp - rollD
            print("the", randEnemy.name, "has", randEnemy.hp, "hp left.")
        else:
            print("You missed!")
    while attack != 'roll':
        print("Type 'roll' to attack")
        attack = input(">")
        roll = die(20)
        if roll >= myPlayer.thaco - randEnemy.ac:
            print("You hit!")
            rollD = die(myPlayer.MAX_DMG)
            print("For", rollD, "damage")
            randEnemy.hp = randEnemy.hp - rollD
            print("the", randEnemy.name, "has", randEnemy.hp, "hp left.")
        else:
            print("You missed!")
def monster_Attack():
    roll = die(20)
    if roll >= randEnemy.thaco - myPlayer.ac:
        print("Monster hit!")
        rollD = die(randEnemy.MAX_DMG)
        print("For", rollD, "damage")
        myPlayer.hp = myPlayer.hp - rollD
        print("the", myPlayer.name, "has", myPlayer.hp, "hp left.")
    else:
        print("The monster missed!")
def battle():
    set_screen()
    while myPlayer.hp > 0 and randEnemy.hp > 0:
        player_Attack()
        monster_Attack()
    if myPlayer.hp <= 0:
        print("You died!")
        time.sleep(1.5)
    elif randEnemy.hp <= 0:
        print("You killed the {}".format(randEnemy.name))
        myPlayer.hp = myPlayer.hp + int(randEnemy.exp * 1.25)
        randEnemy.hp = randEnemy.MAX_HP
        exp_Gain()
def exp_Gain():
    randEnemy = enemy_spawn()
    myPlayer.exp = randEnemy.exp + myPlayer.exp
    level_Up()
    randEnemy = enemy_spawn()
def level_Up():
    LEVEL_UP = 10
    if myPlayer.exp >= LEVEL_UP:
        myPlayer.level = myPlayer.level + 1
        LEVEL_UP = LEVEL_UP * 1.25
        LEVEL_UP = int(LEVEL_UP)
        myPlayer.exp = 0
        myPlayer.MAX_HP = int(myPlayer.MAX_HP * 1.25)
        myPlayer.MAX_MP = int(myPlayer.MAX_MP * 1.25)
        myPlayer.MAX_STM = int(myPlayer.MAX_STM * 1.25)
        myPlayer.MAX_DMG = int(myPlayer.MAX_DMG * 1.25)
        myPlayer.hp = myPlayer.MAX_HP
        myPlayer.mp = myPlayer.MAX_MP
        myPlayer.stm = myPlayer.MAX_STM
def prompt():
    acceptable_actions = ['move', 'go', 'walk', 'quit', 'examine', 'inspect', 'search', 'look', 'location', 'title', 'home', 'map', 'inventory', 'bag', 'stats', 'pick up', 'item', 'battle',
    'attack', 'kill', 'fight']
    print("\n" + "=" * 150)
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
        print_character_stats()
    elif action.lower() in acceptable_actions[15:16]:
        item_pick_up()
    elif action.lower() in acceptable_actions[17:21]:
        battle()
def character_create():
    set_screen()
    valid_choice = {
    'knight': Knight,
    'mage': Mage,
    'paladin': Paladin
    }
    valid_class = ['knight', 'mage', 'paladin']
    welcome = "#Character Select!#".upper()
    print("#" * SCREEN_WIDHT)
    print(welcome.center(SCREEN_WIDHT))
    print("#" * SCREEN_WIDHT, "\n")
    print(("Type 'knight', 'mage', 'paladin' to choose your class\n").center(SCREEN_WIDHT))
    print(("Knight: HP=150, MP=25, STM=125\n").center(SCREEN_WIDHT))
    print(("Mage: HP=75, MP=150, STM=75\n").center(SCREEN_WIDHT))
    print(("Paladin: HP=100, MP=100, STM=100\n").center(SCREEN_WIDHT))
    print(("Choose your class wisely\n".upper()).center(SCREEN_WIDHT))
    pclass = input("> ")
    while pclass.lower() not in valid_class:
        print("That wasn't a proper option.")
        pclass = input("> ")
    return valid_choice[pclass.lower()]()
title_screen()
