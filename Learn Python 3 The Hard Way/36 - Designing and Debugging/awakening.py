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

def living_room(interact=True):
    print("You exit the pantry and enter a big living room with")

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
