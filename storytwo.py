from colorama import Fore
import time
import random
from prettytable import PrettyTable

RED = Fore.RED
BLUE = Fore.BLUE
GREEN = Fore.GREEN
YELLOW = Fore.YELLOW
RESET = Fore.RESET

def use_bow():
    return random.randint(20, 40)

def craft_item(ingredients):
    if not ingredients:
        print(f"\n{RED}You don't have enough ingredients to craft. Explore more to find them!{RESET}")
        return None, None

    crafting_options = [
        "arrow", "trap", "potion", "sword upgrade", "armor upgrade", "magic amulet", "fire bomb", "ice arrow", "poison dart",
        "teleportation scroll", "stealth cloak", "explosive trap", "invisibility potion", "energy drink", "thunder staff",
        "healing totem", "camouflage potion", "mind control crystal", "laser sword", "time-bending hourglass", "sonic bomb",
        "night vision goggles", "frost nova", "homing missile", "windwalker boots", "magnetic field generator", "lunar charm",
        "chaos orb", "mind-reading helmet", "dimensional rift grenade", "sonic scream device", "illusion mirror", "gravity gauntlets",
        "phoenix feather quill", "galactic map", "sky blaster cannon", "earthquake totem", "angelic wings", "demon's contract",
        "arcane prism", "vampire fang dagger", "elixir of eternal youth", "golem core", "celestial compass", "mermaid's tear",
        "dragon scale shield", "alchemist's flask", "sorcerer's stone"
    ]
    crafted_item = random.choice(crafting_options)
    found_ingredient = random.choice(ingredients)
    return crafted_item, found_ingredient

def display_crafting_options():
    table = PrettyTable()
    table.field_names = ["Option", "Description"]

    crafting_options = [
        "arrow", "trap", "potion", "sword upgrade", "armor upgrade", "magic amulet", "fire bomb", "ice arrow", "poison dart",
        "teleportation scroll", "stealth cloak", "explosive trap", "invisibility potion", "energy drink", "thunder staff",
        "healing totem", "camouflage potion", "mind control crystal", "laser sword", "time-bending hourglass", "sonic bomb",
        "night vision goggles", "frost nova", "homing missile", "windwalker boots", "magnetic field generator", "lunar charm",
        "chaos orb", "mind-reading helmet", "dimensional rift grenade", "sonic scream device", "illusion mirror", "gravity gauntlets",
        "phoenix feather quill", "galactic map", "sky blaster cannon", "earthquake totem", "angelic wings", "demon's contract",
        "arcane prism", "vampire fang dagger", "elixir of eternal youth", "golem core", "celestial compass", "mermaid's tear",
        "dragon scale shield", "alchemist's flask", "sorcerer's stone"
    ]

    for i, option in enumerate(crafting_options, start=1):
        table.add_row([str(i), option])

    return table

def find_ingredients():
    ingredients = [
        "herb", "crystal", "feather", "blood moss", "moonstone", "troll hair", "dragon root", "silverfern leaf", "unicorn horn",
        "phoenix feather", "ghost orchid", "mandrake root", "starlight petals", "wyvern scale", "gorgon eye", "kraken tentacle",
        "basilisk fang", "nymph tears", "shadow essence", "goblin ear", "thunderstrike blossom", "firefly dust", "diamond dust",
        "lunar moth wing", "frost lotus", "sunfire ember", "abyssal seaweed", "stardust crystal", "venomous thorn", "moonlit dew",
        "fairy wing", "banshee scream", "phantom essence", "celestial sand", "wisp lantern", "ancient bark", "chimera scale",
        "demon heart", "spectral silk", "siren scale", "harpy feather", "dwarf beard hair", "silver wolf pelt", "yeti fur",
        "hollow reaper bone", "gryphon talon", "sorcerer's ash", "dark elf shadow", "ogre knucklebone", "centaur hoof",
        "pixie golden dust", "treant leaf"
    ]
    found_ingredient = random.choice(ingredients)
    print(f"\n{GREEN}You found a {found_ingredient} while exploring!{RESET}")
    return found_ingredient

def explore_forest():
    print(f"{YELLOW}You decide to explore the dense forest...{RESET}")
    time.sleep(2)
    exploration_result = random.choice(["success", "failure"])
    if exploration_result == "success":
        print(f"{GREEN}Your exploration was successful!{RESET}")
        return True
    else:
        print(f"{RED}Your exploration yielded no results. Keep searching!{RESET}")
        return False

def explore_mountain():
    print(f"{YELLOW}You decide to climb the towering mountain...{RESET}")
    time.sleep(2)
    exploration_result = random.choice(["success", "failure"])
    if exploration_result == "success":
        print(f"{GREEN}Your ascent was successful!{RESET}")
        return True
    else:
        print(f"{RED}Your climb yielded no results. Keep searching!{RESET}")
        return False

def encounter_enemy(enemy_name):
    print(f"{RED}Oh no! You encountered a {enemy_name} while exploring. Prepare for battle!{RESET}")
    time.sleep(2)
    return random.randint(50, 150)

def bleed_out():
    print(f"{RED}You start to feel weak as you bleed out. Find a way to stop the bleeding!{RESET}")
    time.sleep(2)
    return True


def battle(chosen_weapon, current_health, ingredients):
    enemy_names = [
        "giant spider", "bandit leader", "ancient guardian", "sand elemental", "treasure guardian",
        "nomadic warlock", "swarm of beetles", "cave troll", "enchanted serpent", "lost spirit",
        "forest wraith", "fire drake", "ice golem", "dark sorcerer", "shadow assassin",
        "stone golem", "thunder elemental", "water nymph", "sky sentinel", "lava hound",
        "desert mirage", "swamp monster", "earthshaker", "nightmare steed",
        "ghostly apparition", "mindflayer", "poisonous wyrm", "mechanical golem", "golden golem",
        "dark phoenix", "living storm", "abominable snowman", "time warden", "demonic warlord",
        "cursed banshee", "goblin king", "wicked siren", "frost lich", "shadowy specter",
        "hydra", "electrified serpent", "soul reaper", "vampire lord", "chimera", "kraken",
        "dragon lord", "beholder", "undying lich", "celestial guardian", "astral behemoth",
        "cosmic dragon", "void walker", "dimensional reaper", "timeless sorcerer"
    ]
    enemy_name = random.choice(enemy_names)
    enemy_health = encounter_enemy(enemy_name)
    
    while enemy_health > 0 and current_health > 0:
        print("\nWhat would you like to do in the battle?")
        print(f"{YELLOW}1. Attack with {chosen_weapon}{RESET}")
        print(f"{YELLOW}2. Use an item{RESET}")

        battle_choice = input(f"\n{GREEN}CHOICE: {RESET}")

        if battle_choice == "1":
            if chosen_weapon == "Bow":
                damage_dealt = use_bow()
            else:
                damage_dealt = random.randint(10, 20)
            enemy_health -= damage_dealt
            print(f"{GREEN}You dealt {damage_dealt} damage to the {enemy_name}!{RESET}")
        elif battle_choice == "2":
            if ingredients:
                print(f"\n{YELLOW}Items in your inventory: {', '.join(ingredients)}{RESET}")
            print(f"\n{YELLOW}Crafting Options:{RESET}")
            crafted_item, found_ingredient = craft_item(ingredients)

            if crafted_item:
                print(f"{GREEN}You successfully crafted {crafted_item}!{RESET}")

                if crafted_item == "arrow":
                    print(f"{GREEN}You crafted an arrow!{RESET}")
                elif crafted_item == "trap":
                    print(f"{GREEN}You created a trap! It might come in handy.{RESET}")
                elif crafted_item == "potion":
                    print(f"{GREEN}You brewed a mysterious potion. Its effects are unknown.{RESET}")
                else:
                    print(f"{GREEN}You crafted {crafted_item}! It might prove useful.{RESET}")

                ingredients.remove(found_ingredient)
                print(f"\n{GREEN}You used {found_ingredient} for crafting.{RESET}")

            else:
                print(f"{RED}Invalid input. Please choose a valid crafting option.{RESET}")

        else:
            print(f"\n{RED}You don't have any items to use!{RESET}")

        enemy_damage = random.randint(10, 30)
        current_health -= enemy_damage
        print(f"\n{RED}The {enemy_name} attacked you and dealt {enemy_damage} damage!{RESET}")
        print(f"{RED}Current Health: {current_health}{RESET}")

    if current_health <= 0:
        print(f"\n{RED}You were defeated by the {enemy_name}. GAME OVER!{RESET}")
        exit()

def main_loop(chosen_weapon, current_health, original_health, ingredients):
    for _ in range(10):
        scenarios = [
            "You discover a hidden oasis in the middle of the desert. A wise old sage offers you a quest to fetch water from the oasis. Will you accept?",
            "A group of bandits is spotted in the desert. How will you handle this situation?",
            "You stumble upon an ancient temple in the desert. A mysterious voice challenges you to a trial. Will you accept?",
            "A sandstorm approaches. Where do you choose to take shelter in the desert?",
            "You find a mysterious cave entrance. Do you dare to enter?",
            "You come across an abandoned camp. Investigate or move on?",
            "A rickety bridge crosses a deep chasm. Will you risk crossing it?",
            "You see a glowing light in the distance. Investigate or ignore?",
            "A pack of wolves is spotted. What will you do?",
            "You find an old treasure map. Follow it or continue exploring?"
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

            while current_health > 0:
                print("\nWhat would you like to do now?")
                print(f"{YELLOW}1. Explore{RESET}")
                print(f"{YELLOW}2. Craft{RESET}")
                print(f"{YELLOW}3. End{RESET}")

                choice = input(f"\n{GREEN}CHOICE: {RESET}")

                if choice == "1":
                    exploration_result = explore_forest()
                    if exploration_result:
                        found_ingredient = find_ingredients()
                        if found_ingredient:
                            ingredients.append(found_ingredient)
                            print(f"\n{GREEN}You now have {', '.join(ingredients)} in your inventory.{RESET}")

                            battle(chosen_weapon, current_health, ingredients)

                            if current_health <= 0:
                                print(f"\n{RED}You were defeated. GAME OVER!{RESET}")
                                exit()

                        else:
                            print(f"\n{RED}You didn't find any ingredients. Keep exploring!{RESET}")

                elif choice == "2":
                    if ingredients:
                        print(f"\n{YELLOW}Items in your inventory: {', '.join(ingredients)}{RESET}")
                        print(f"\n{YELLOW}Crafting Options:{RESET}")
                        print(display_crafting_options())
                        crafted_item, found_ingredient = craft_item(ingredients)

                        if crafted_item:
                            print(f"{GREEN}You successfully crafted {crafted_item}!{RESET}")

                            if crafted_item == "arrow":
                                print(f"{GREEN}You crafted an arrow!{RESET}")
                            elif crafted_item == "trap":
                                print(f"{GREEN}You created a trap! It might come in handy.{RESET}")
                            elif crafted_item == "potion":
                                print(f"{GREEN}You brewed a mysterious potion. Its effects are unknown.{RESET}")
                            else:
                                print(f"{GREEN}You crafted {crafted_item}! It might prove useful.{RESET}")

                            ingredients.remove(found_ingredient)
                            print(f"\n{GREEN}You used {found_ingredient} for crafting.{RESET}")

                        else:
                            print(f"{RED}Invalid input. Please choose a valid crafting option.{RESET}")

                    else:
                        print(f"\n{RED}You don't have enough items to craft. Explore more to find them!{RESET}")

                elif choice == "3":
                    print("\nOK, may your story continue at a later stage. Goodbye!")
                    time.sleep(2)
                    exit()

                else:
                    print(f"{RED}Invalid input. Please choose a valid option.{RESET}")

        elif DICE.lower() == "no":
            print("\nYou chose not to throw the dice. Continue with caution!")
        else:
            print(f"{RED}Invalid input. Please choose yes or no.{RESET}")





def begin_start():
    original_health = 230
    current_health = original_health
    ingredients = []

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

        main_loop(chosen_weapon, current_health, original_health, ingredients)

    elif choice.lower() == "settings":
        print(f"\n{BLUE}SETTINGS{RESET}")
    elif choice.lower() == "end":
        print("\nOK, may your story continue at a later stage. Goodbye!")
        time.sleep(2)
        exit()
    else:
        print(f"{RED}Invalid input. Please choose Begin, Settings, or End.{RESET}")

begin_start()
