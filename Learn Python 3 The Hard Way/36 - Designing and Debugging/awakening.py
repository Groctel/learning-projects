from sys import exit

inventory = []
pantry_objects = ['boxes', 'door', 'key']

def examine(room, item):
    if item in inventory or item in room:
        if item == 'box' or item == 'boxes':
            print("A putrid stench comes from them. Yuck!")
        elif item == 'door':
            print("A narrow door with a lock.")
        elif item == 'key':
            print("A small key with an ornate head.")
    else:
        not_in_room(item)

def living_room():
    player_life   = 100
    troll_life    = 100
    troll_counter = 3

    print("You exit the pantry and enter a big living room with a troll...")
    print("IT ENGAGES YOU IN DEADLY COMBAT! IT'S TIME TO FIGHT FOR YOUR LIFE!")

    while troll_life > 0 and player_life > 0:
        print("\n[PLAYER: {} HP]", player_life)
        print("[TROLL: {} HP]", troll_life)
        print("What would you like to do?")
        print("- 1: Attack!")
        print("- 2: Defend!")
        print("- 3: Flee!")

        choice = input("> ")

        print()

        if choice == "1":
            troll_life -= 10
            print("You deal 10 damage to the troll")
        elif choice == "2":
            print("You defend yourself against the troll's attacks...")
        elif choice == "3":
            print("You try to flee but there's nowhere to hide!")
        else:
            print("Invalid option...")

        if troll_life > 0:
            if troll_counter == 3 or troll_counter == 2:
                print("The troll prepares an attack...")
            elif troll_counter == 1:
                print("The troll's attack is imminent!")
            else:
                print("The troll discharges its anger against your bones!")

                if choice == "2":
                    print("But you manage to resis its strength!")
                else:
                    player_life -= 50

        if troll_counter == 0:
            troll_counter = 3
        else:
            troll_counter -= 1

    if troll_life <= 0:
        print("You managed to defeat the troll. Congratulations!")
        print("Thanks for playing!")
    else:
        print("The troll managed to crush you.")
        print("Better luck next time!")

    exit(0)

def missing_noun(query):
    print(f"I only understood as far as you wanting to {query}.")

def one_word_commands(action, room_fn):
    if 'exit' in action or 'quit' in action:
        print("Terminating the game...")
        exit(0)
    elif 'look' in action:
        room_fn(False)
    else:
        print("I sincerely didn't understand that.")

def not_in_room(item):
    print(f"You can see no {item} here!")

def pantry(interact=True):
    """Initial room where the player appears"""

    print("You wake up in a small dark smelly room full with tens of boxes")
    print("piled up to the ceiling. As you stand up with great difficulty due")
    print("to the pain in your head, you feel what seems to be a small key.")

    while interact:
        action = input("> ")

        if 'examine' in action:
            if 'box' in action or 'boxes' in action:
                examine(pantry_objects, 'boxes')
            elif 'door' in action:
                examine(pantry_objects, 'door')
            elif 'key' in action:
                examine(pantry_objects, 'key')
            else:
                not_in_room('such thing')

        elif 'open' in action or 'unlock' in action:
            if 'door' in action:
                if 'key' in inventory:
                    inventory.remove('key')
                    print("You unlock the door with the key as it dissolves in")
                    print("the lock. You open it and leave the pantry.")
                    living_room()
                else:
                    print("You don't have anything to unlock the door with!")
            else:
                if 'open' in action:
                    missing_noun("open something")
                elif 'unlock' in action:
                    missing_noun("unlock someting")

        elif 'take' in action:
            if 'key' in action:
                if 'key' in pantry_objects:
                    pantry_objects.remove('key')
                    inventory.append('key')
                    print("You take the key and put it in your pocket.")
                else:
                    not_in_room('key')
            else:
                missing_noun("take something")

        else:
            one_word_commands(action, pantry)

def start():
    """Main function. Prints the game info and starts it."""

    print("Awakening: A very limited text adventure by Groctel.\n\n")
    pantry()

start()
