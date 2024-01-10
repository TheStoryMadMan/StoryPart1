from colorama import Fore
import time
import random

RED = Fore.RED
BLUE = Fore.BLUE
GREEN = Fore.GREEN
YELLOW = Fore.YELLOW
RESET = Fore.RESET

print(f"{GREEN}WELCOME MY FRIEND{RESET}")

def begin_start():
    original_health = 230
    current_health = original_health

    print(f"\n{BLUE}What would you like to choose:{RESET}\n")

    print(f"{RED}Begin{RESET}")
    print(f"{RED}Settings{RESET}")
    print(f"{RED}End{RESET}")

    choice = input(f"\n{GREEN}CHOICE:{RESET} ")

    if choice.lower() == "begin":
        print(f"\n{RED}May thy story be foretold")

        Story = input("\nWhat would you like to call your story? ")
        print(f"{BLUE}{Story} shall now commence! Travel safe, fellow being.")
        print("\nFirstly, you must name your traveler that you control on your quest that the Great Elves\nhave given to you.")
        Character_first = input("\nFirst name: ")
        Character_Last = input("Last name: ")
        Character = f"{Character_first} {Character_Last}"

        weapons = ["Sword", "Battle-Axe", "Knife", "Bow"]
        biomes = ["Grass-Lands", "Desert", "Woods"]
        companions = ["Hound", "Felidae", "Parrot"]

        chosen_weapon = random.choice(weapons)
        chosen_biome = random.choice(biomes)
        chosen_companion = random.choice(companions)

        print(f"\n{Character} has arrived at....")
        time.sleep(1)
        print(f"Biome: {chosen_biome}")

        character_info = {
            "Name": Character,
            "Weapon": chosen_weapon,
            "Biome": chosen_biome,
            "Companion": chosen_companion
        }
        print("\nCharacter Information:")
        for key, value in character_info.items():
            print(f"{key}: {value}")

        scenarios = [
            "You discover a hidden oasis in the middle of the desert. A wise old sage offers you a quest to fetch water from the oasis. Will you accept?",
            "A group of bandits is spotted in the desert. How will you handle this situation?",
            "You stumble upon an ancient temple in the desert. A mysterious voice challenges you to a trial. Will you accept?",
            "A sandstorm approaches. Where do you choose to take shelter in the desert?"
        ]
        random_scenario = random.choice(scenarios)
        print(f"\nScenario: {random_scenario}")
        print(f"{GREEN}Now that details have been shown, what would you like to do? {RESET}")

        DICE = input(f"\n{YELLOW}Throw the dice? (yes/no): {RESET}")
        if DICE.lower() == "yes":
            dice_result = random.randint(1, 5)
            print(f"{GREEN}You rolled the dice and got: {dice_result}{RESET}")

            damage_taken = dice_result * 10
            current_health -= damage_taken

            if current_health < original_health:
                potion_list = ["canned oil", "health potion", "damage", "disappear"]
                random_potion = random.choice(potion_list)
                print(f"\n{RED}Your journey through the desert is treacherous. A sandstorm hits, causing you to take {damage_taken} damage!{RESET}")
                print(f"{GREEN}You discovered a potion hidden in the sand: {random_potion}{RESET}")


                if random_potion == "health potion":
                    health_regen = random.randint(20, 50)
                    current_health += health_regen
                    print(f"{GREEN}You consumed the health potion and regained {health_regen} health!{RESET}")

            print(f"\n{RED}Damage Stats:")
            print(f"Original Health: {original_health}")
            print(f"Current Health: {current_health}")
            print(f"Damage Taken: {damage_taken}{RESET}")
        
    elif choice.lower() == "settings":
        print(f"\n{BLUE}SETTINGS{RESET}")
        

    elif choice.lower() == "end":
        print("\nOK, may your story continue at a later stage. Goodbye!")
        time.sleep(2)
        exit()

begin_start()
