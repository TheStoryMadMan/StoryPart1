from rich.console import Console
from rich.panel import Panel
from rich.text import Text
import os
import time
import random
from colorama import Fore
from rich.console import Console
from rich.table import Table
from rich.text import Text
RED = Fore.RED
GREEN = Fore.GREEN
RESET = Fore.RESET

console = Console()

class Player:
    def __init__(self, first_name, last_name):
        self.name = f"{first_name} {last_name}"
        self.health = 100
        self.inventory = []
        self.crafting_materials = []
        self.healing_counter = 3 

player = None 

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def display_player_info():
    player_info = Panel.fit(
        Text(f"{player.name}\nHealth: {player.health}\nInventory: {', '.join(player.inventory)}\nCrafting Materials: {', '.join(player.crafting_materials)}"),
        title="Player Info"
    )
    console.print(player_info)

def get_user_input(prompt):
    user_input = input(prompt + " ").strip()
    return user_input
def generate_items():
    items = [
        "Key", "Potion", "Map", "Gem", "Artifact", "Sword", "Shield", "Helmet", "Ring", "Amulet",
        "Scroll", "Book", "Crystal Ball", "Dagger", "Bow", "Arrow", "Staff", "Wand", "Rune", "Orb",
        "Cloak", "Gloves", "Boots", "Robe", "Chainmail", "Plate Armor", "Leather Armor", "Quiver", "Scepter", "Torch",
        "Compass", "Hourglass", "Coin", "Crown", "Bracelet", "Necklace", "Elixir", "Feather", "Mirror", "Flute",
        "Gemstone", "Talisman", "Chalice", "Lantern", "Candle", "Bottle", "Hourglass", "Goblet", "Mug", "Statuette",
        "Horn", "Rope", "Saddle", "Lute", "Painting", "Mask", "Cloth", "Feather Quill", "Ink Bottle", "Spyglass",
        "Pocket Watch", "Lockpick", "Telescope", "Goggles", "Candelabrum", "Fishing Rod", "Treasure Map", "Bag of Gems", "Locket", "Brass Key",
        "Silver Key", "Golden Key", "Bronze Coin", "Silver Coin", "Gold Coin", "Crystal Vial", "Rose", "Crown Jewel", "Crystal Dagger", "Emerald",
        "Ruby", "Sapphire", "Diamond", "Pearl", "Enchanted Feather", "Mystic Rune", "Dragon Scale", "Phoenix Feather", "Unicorn Horn", "Star Crystal",
        "Obsidian Shard", "Cursed Amulet", "Fairy Wing", "Basilisk Eye", "Mermaid Scale", "Phoenix Egg", "Spider Silk", "Troll Tooth", "Werewolf Fur", "Vampire Fang",
        "Witch's Broomstick", "Ghostly Chain", "Zombie Hand", "Giant's Club", "Gorgon Head", "Minotaur Horn", "Harpy Feather", "Centaur Arrow", "Cyclops Eye", "Chimera Tail",
        "Banshee Wail", "Griffin Feather", "Hydra Scale", "Kraken Tentacle", "Leprechaun Hat", "Siren Song", "Medusa Gaze", "Nymph's Veil", "Satyr Flute", "Treant Leaf"
    ]
    return items

def crafting_materials(items, num_materials=20):

    crafting_materials = [
        "Bronze Coin", "Iron Ingot", "Herb", "Magic Essence", "Parchment", "Compass", "Crystal", "Silver Coin",
        "Ancient Relic", "Gold Coin", "Wooden Branch", "String", "Wooden Shaft", "Feather", "Wooden Stick", "Rune",
        "Stone", "Wooden Frame", "Silk", "Iron Ingot", "Steel Chain", "Steel Plate", "Leather", "Wooden Shaft",
        "Magic Essence", "Oil", "Magnetite", "Gold Band", "Gem", "Ink Bottle", "Glass Lens", "Clockwork Mechanism",
        "Metal Wire", "Wooden Handle", "Cork", "Glass", "Silver Plate", "Silver Cup", "Gold Plate", "Gold Chain",
        "Crystal Vial", "Flower Petals", "Stem", "Silver Setting", "Silver Setting", "Gold Setting", "Gold Setting",
        "Silver Setting", "Magic Essence", "Magic Essence", "Dragon Skin", "Metal Plate", "Metal Shaft", "Silver Filigree",
        "Star Shard", "Metal Plate", "Cursed Gem", "Metal Frame", "Fairy Wing", "Basilisk Eye", "Metal Setting",
        "Phoenix Egg", "Metal Frame", "Spider Silk", "Troll Tooth", "Metal Setting", "Vampire Fang", "Silver Blade",
        "Broomstick", "Magic Essence", "Ghostly Essence", "Metal Chain", "Zombie Hand", "Metal Handle", "Giant's Club",
        "Wooden Pipe", "Gorgon Head", "Metal Frame", "Minotaur Horn", "Metal Setting", "Harpy Feather", "Thread",
        "Centaur Arrowhead", "Wooden Shaft", "Cyclops Eye", "Metal Setting", "Chimera Tail", "Leather", "Banshee Essence",
        "Metal Frame", "Griffin Feather", "Thread", "Hydra Scale", "Metal Plate", "Kraken Tentacle", "Metal Frame",
        "Leprechaun Hat", "Thread", "Siren Song", "Shell", "Medusa Gaze", "Stone", "Nymph's Veil", "Silk", "Satyr Flute",
        "Wooden Pipe", "Treant Leaf", "Wooden Frame"
    ]
    return random.sample(crafting_materials, num_materials)


crafting_recipes = {
    "Key": ["Bronze Coin", "Iron Ingot"],
    "Potion": ["Herb", "Magic Essence"],
    "Map": ["Parchment", "Compass"],
    "Gem": ["Crystal", "Silver Coin"],
    "Artifact": ["Ancient Relic", "Gold Coin"],
    "Sword": ["Iron Ingot", "Leather Strip"],
    "Shield": ["Wooden Plank", "Iron Ingot"],
    "Helmet": ["Iron Ingot", "Leather"],
    "Ring": ["Gold Band", "Gem"],
    "Amulet": ["Silver Chain", "Gem"],
    "Scroll": ["Parchment", "Ink Bottle"],
    "Book": ["Leather", "Parchment"],
    "Crystal Ball": ["Crystal", "Magic Essence"],
    "Dagger": ["Iron Ingot", "Leather Strip"],
    "Bow": ["Wooden Branch", "String"],
    "Arrow": ["Wooden Shaft", "Feather"],
    "Staff": ["Wooden Branch", "Crystal"],
    "Wand": ["Wooden Stick", "Magic Essence"],
    "Rune": ["Stone", "Magic Essence"],
    "Orb": ["Crystal", "Silver Chain"],
    "Cloak": ["Leather", "Thread"],
    "Gloves": ["Leather", "Thread"],
    "Boots": ["Leather", "Thread"],
    "Robe": ["Silk", "Thread"],
    "Chainmail": ["Iron Ingot", "Steel Chain"],
    "Plate Armor": ["Steel Plate", "Leather"],
    "Leather Armor": ["Leather", "Thread"],
    "Quiver": ["Leather", "Wooden Shaft"],
    "Scepter": ["Wooden Stick", "Magic Essence"],
    "Torch": ["Wooden Stick", "Oil"],
    "Compass": ["Magnetite", "Iron Ingot"],
    "Hourglass": ["Glass", "Sand"],
    "Coin": ["Metal Disc", "Engraving"],
    "Crown": ["Gold Plate", "Gem"],
    "Bracelet": ["Gold Chain", "Gem"],
    "Necklace": ["Silver Chain", "Gem"],
    "Elixir": ["Herb", "Magic Essence"],
    "Feather": ["Bird Feather", "Thread"],
    "Mirror": ["Glass", "Silver Plate"],
    "Flute": ["Wooden Stick", "Silver Pipe"],
    "Gemstone": ["Gem", "Silver Plate"],
    "Talisman": ["Wooden Pendant", "Magic Essence"],
    "Chalice": ["Silver Cup", "Gold Plate"],
    "Lantern": ["Metal Frame", "Oil"],
    "Candle": ["Wax", "Thread"],
    "Bottle": ["Glass", "Cork"],
    "Goblet": ["Gold Cup", "Silver Plate"],
    "Mug": ["Wooden Cup", "Metal Rim"],
    "Statuette": ["Clay", "Paint"],
    "Horn": ["Animal Horn", "Leather Strip"],
    "Rope": ["Twine", "Thread"],
    "Saddle": ["Leather", "Metal Buckle"],
    "Lute": ["Wooden Frame", "Strings"],
    "Painting": ["Canvas", "Paint"],
    "Mask": ["Wooden Mask", "Paint"],
    "Cloth": ["Fabric", "Thread"],
    "Feather Quill": ["Bird Feather", "Wooden Stick"],
    "Ink Bottle": ["Glass", "Ink"],
    "Spyglass": ["Metal Tube", "Glass Lens"],
    "Pocket Watch": ["Metal Casing", "Clockwork Mechanism"],
    "Lockpick": ["Metal Wire", "Wooden Handle"],
    "Telescope": ["Metal Tube", "Glass Lens"],
    "Goggles": ["Metal Frame", "Glass Lenses"],
    "Candelabrum": ["Metal Frame", "Candles"],
    "Fishing Rod": ["Wooden Pole", "Thread"],
    "Treasure Map": ["Parchment", "Ink Bottle"],
    "Bag of Gems": ["Gem", "Silk"],
    "Locket": ["Metal Frame", "Photo"],
    "Brass Key": ["Bronze Key", "Metal Handle"],
    "Silver Key": ["Silver Key", "Metal Handle"],
    "Golden Key": ["Gold Key", "Gem Handle"],
    "Bronze Coin": ["Bronze Ingot", "Coin Stamp"],
    "Silver Coin": ["Silver Ingot", "Coin Stamp"],
    "Gold Coin": ["Gold Ingot", "Coin Stamp"],
    "Crystal Vial": ["Crystal", "Glass"],
    "Rose": ["Flower Petals", "Stem"],
    "Crown Jewel": ["Gem", "Gold Setting"],
    "Crystal Dagger": ["Crystal", "Silver Blade"],
    "Emerald": ["Gem", "Silver Setting"],
    "Ruby": ["Gem", "Gold Setting"],
    "Sapphire": ["Gem", "Silver Setting"],
    "Diamond": ["Gem", "Gold Setting"],
    "Pearl": ["Pearl", "Silver Setting"],
    "Enchanted Feather": ["Feather", "Magic Essence"],
    "Mystic Rune": ["Rune", "Magic Essence"],
    "Dragon Scale": ["Dragon Skin", "Metal Plate"],
    "Phoenix Feather": ["Phoenix Feather", "Metal Shaft"],
    "Unicorn Horn": ["Unicorn Horn", "Silver Filigree"],
    "Star Crystal": ["Star Shard", "Metal Frame"],
    "Obsidian Shard": ["Obsidian", "Metal Plate"],
    "Cursed Amulet": ["Cursed Gem", "Metal Chain"],
    "Fairy Wing": ["Fairy Wing", "Thread"],
    "Basilisk Eye": ["Basilisk Eye", "Silver Plate"],
    "Mermaid Scale": ["Mermaid Scale", "Metal Setting"],
    "Phoenix Egg": ["Phoenix Egg", "Metal Frame"],
    "Spider Silk": ["Spider Silk", "Thread"],
    "Troll Tooth": ["Troll Tooth", "Metal Setting"],
    "Werewolf Fur": ["Werewolf Fur", "Leather"],
    "Vampire Fang": ["Vampire Fang", "Silver Blade"],
    "Witch's Broomstick": ["Broomstick", "Magic Essence"],
    "Ghostly Chain": ["Ghostly Essence", "Metal Chain"],
    "Zombie Hand": ["Zombie Hand", "Metal Frame"],
    "Giant's Club": ["Giant's Club", "Wooden Handle"],
    "Gorgon Head": ["Gorgon Head", "Metal Frame"],
    "Minotaur Horn": ["Minotaur Horn", "Metal Setting"],
    "Harpy Feather": ["Harpy Feather", "Thread"],
    "Centaur Arrow": ["Centaur Arrowhead", "Wooden Shaft"],
    "Cyclops Eye": ["Cyclops Eye", "Metal Setting"],
    "Chimera Tail": ["Chimera Tail", "Leather"],
    "Banshee Wail": ["Banshee Essence", "Metal Frame"],
    "Griffin Feather": ["Griffin Feather", "Thread"],
    "Hydra Scale": ["Hydra Scale", "Metal Plate"],
    "Kraken Tentacle": ["Kraken Tentacle", "Metal Frame"],
    "Leprechaun Hat": ["Leprechaun Hat", "Thread"],
    "Siren Song": ["Siren Song", "Shell"],
    "Medusa Gaze": ["Medusa Gaze", "Stone"],
    "Nymph's Veil": ["Nymph's Veil", "Silk"],
    "Satyr Flute": ["Satyr Flute", "Wooden Pipe"],
    "Treant Leaf": ["Treant Leaf", "Wooden Frame"],
}



def display_crafting_options():
    table = Table(title="Crafting Options", title_style="bold magenta", show_lines=True)
    table.add_column("Item", style="cyan", justify="center")
    table.add_column("Craftable", style="cyan", justify="center")

    craftable_items = set(player.crafting_materials) 

    for item in generate_items():
        if item in craftable_items:
            table.add_row(f"[green]{item}[/green]", "[green]Craftable[/green]")
        else:
            table.add_row(f"[red]{item}[/red]", "[red]Cannot craft[/red]")

    console.print(table)

def begin_story():
    global player
    print("Starting Story....")
    time.sleep(2)
    first_name = input("First name: ")
    last_name = input("Last name: ")
    player = Player(first_name, last_name)
    player.crafting_materials = crafting_materials(generate_items(), num_materials=10)

    print(f"\n{player.name}, welcome to the world!")

    return player

def handle_scenario(scenario):
    console.print(f"\n[bold]{scenario}[/bold]\n")
    user_choice = get_user_input("What will you do? (Type the number of your choice or 'exit' to quit)\n1. Explore\n2. Rest\n3. Inventory\n4. Craft\n")

    if user_choice.lower() == 'exit':
        console.print("Exiting the game. Goodbye!")
        exit()

    if user_choice == '1':
        explore()
    elif user_choice == '2':
        rest()
    elif user_choice == '3':
        display_inventory()
    elif user_choice == '4':
        craft()
    else:
        console.print("Invalid choice. Please choose a valid option.")

def explore():
    console.print("You decide to explore the surroundings...")

    encounter_chance = random.randint(1, 10)
    
    if encounter_chance <= 4: 
        enemy = generate_enemy()
        console.print(f"You encounter a {enemy}!")
        combat(enemy)
    else:
        found_item = random.choice(generate_items())
        console.print(f"You found a {found_item}!")
        player.inventory.append(found_item)

def generate_enemy():
    enemies = [
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
    return random.choice(enemies)

def combat(enemy):
    console.print(f"A wild {enemy} attacks you!")


    enemy_health = random.randint(20, 40)
    while enemy_health > 0 and player.health > 0:
        console.print(f"\nYour Health: {player.health}\n{enemy.capitalize()} Health: {enemy_health}")
        action = get_user_input("What will you do? (Type 'attack' to attack or 'run' to try to escape): ")

        if action.lower() == 'attack':
            player_damage = random.randint(10, 20)
            enemy_damage = random.randint(5, 15)

            console.print(f"You attack the {enemy} and deal {player_damage} damage!")
            enemy_health -= player_damage

            if enemy_health > 0:
                console.print(f"The {enemy} counterattacks and deals {enemy_damage} damage!")
                player.health -= enemy_damage
        elif action.lower() == 'run':
            run_success = random.randint(1, 2) == 1  

            if run_success:
                console.print(f"You manage to escape from the {enemy}!")
                return
            else:
                console.print(f"The {enemy} blocks your escape!")
                enemy_damage = random.randint(5, 15)
                player.health -= enemy_damage
        else:
            console.print("Invalid action. Please type 'attack' or 'run'.")

    if player.health <= 0:
        console.print("You were defeated in combat. Game over!")
        exit()
    else:
        console.print(f"You defeated the {enemy} and gained some experience!")


def rest():
    global player
    if player.healing_counter > 0:
        console.print("You decide to rest and recover some health.")
        player.health += random.randint(10, 20)
        console.print(f"Your health is now {player.health}.")
        player.healing_counter -= 1
        console.print(f"Remaining heals: {player.healing_counter}")
    else:
        console.print("You've exhausted your healing attempts. It's time to go on an adventure!")

def display_inventory():
    console.print("You check your inventory:")
    console.print(", ".join(player.inventory) or "Your inventory is empty.")

def craft():
    console.print("You decide to craft something...")

    if len(player.crafting_materials) < 2:
        console.print("You need at least 2 crafting materials to craft something.")
        return

    display_crafting_options()

    user_choice = get_user_input("Type the name of the item you want to craft (or type 'back' to go back): ")

    if user_choice.lower() == 'back':
        return

    if user_choice in crafting_recipes and all(material in player.crafting_materials for material in crafting_recipes[user_choice]):
        console.print(f"You crafted a {user_choice}!")
        player.inventory.append(user_choice)
  
        player.crafting_materials = [material for material in player.crafting_materials if material not in crafting_recipes[user_choice]]
    else:
        console.print(f"[{RED}]Cannot craft {user_choice}[/{RED}]. Make sure you have the required materials.")

def game_loop():
    while True:
        display_player_info()
        handle_scenario(random.choice(scenarios))

if __name__ == "__main__":
    clear_terminal()
    scenarios = [
        "While traveling through the forest, you encounter a talking tree that offers ancient wisdom. Will you listen to its advice or continue your journey?",
        "In the desert, you find a hidden oasis guarded by mystical creatures. They demand a tribute for safe passage. How will you negotiate with them?",
        "A mysterious portal appears in front of you. It seems to lead to another dimension. Do you dare to enter and explore the unknown?",
        "As you climb a mountain, you discover a cave entrance. Inside, you find a friendly tribe of mountain dwellers. Will you join them in a feast or proceed?",
        "A magical storm approaches, filled with ethereal lights. Do you try to harness its power or seek shelter to avoid potential dangers?",
        "While exploring, you come across a forgotten library in the woods. Inside, ancient scrolls reveal a forgotten spell. Do you attempt to learn it?",
        "A celestial event occurs, and a shooting star lands nearby. Investigate the crash site or make a wish on the fallen star?",
        "You encounter a wounded mythical creature in the woods. It seems harmless but in pain. Will you help heal it or leave it be?",
        "A riddle-posing sphinx blocks your path in the desert. Solve its riddle to proceed or face its enigmatic consequences.",
        "During a sandstorm, you stumble upon a hidden cave filled with glowing crystals. Do you collect the crystals or leave them untouched?",
        "An ancient guardian challenges you to a game of wits. Accept the challenge and test your intelligence.",
        "In the forest, you find a pool of enchanted water. Drinking from it might grant you a magical boon, but the consequences are unknown. Will you take the risk?",
        "A pack of enchanted wolves appears, offering to guide you through the woods. Accept their guidance or continue your journey alone?",
        "A mysterious figure approaches, claiming to be a time traveler. They offer you a glimpse into your future. Do you accept or reject their offer?",
        "You discover an abandoned mine in the mountain. Venture inside to uncover forgotten treasures or avoid potential dangers?",
        "A mischievous spirit challenges you to a game of riddles. Win the game, and it might grant you a valuable item.",
        "A group of nomads invites you to join their desert festival. Participate in the festivities or continue your quest?",
        "While crossing a bridge, you encounter a guardian spirit. It demands a toll for safe passage. Negotiate with the spirit or find an alternate route?",
        "In the woods, you find a magical portal leading to a parallel realm. Enter the portal and explore the mysterious land.",
        "A wise oracle appears on your journey, offering cryptic visions of your destiny. Will you seek clarity or leave the visions unanswered?"
    ]

    player = begin_story()
    
    banner = """\r
    [bold magenta]
                                                                                                 
   SSSSSSSSSSSSSSS      tttt                                                                     
 SS:::::::::::::::S  ttt:::t                                                                     
S:::::SSSSSS::::::S  t:::::t                                                                     
S:::::S     SSSSSSS  t:::::t                                                                     
S:::::S        ttttttt:::::ttttttt       ooooooooooo   rrrrr   rrrrrrrrryyyyyyy           yyyyyyy
S:::::S        t:::::::::::::::::t     oo:::::::::::oo r::::rrr:::::::::ry:::::y         y:::::y 
 S::::SSSS     t:::::::::::::::::t    o:::::::::::::::or:::::::::::::::::ry:::::y       y:::::y  
  SS::::::SSSSStttttt:::::::tttttt    o:::::ooooo:::::orr::::::rrrrr::::::ry:::::y     y:::::y   
    SSS::::::::SS    t:::::t          o::::o     o::::o r:::::r     r:::::r y:::::y   y:::::y    
       SSSSSS::::S   t:::::t          o::::o     o::::o r:::::r     rrrrrrr  y:::::y y:::::y     
            S:::::S  t:::::t          o::::o     o::::o r:::::r               y:::::y:::::y      
            S:::::S  t:::::t    tttttto::::o     o::::o r:::::r                y:::::::::y       
SSSSSSS     S:::::S  t::::::tttt:::::to:::::ooooo:::::o r:::::r                 y:::::::y        
S::::::SSSSSS:::::S  tt::::::::::::::to:::::::::::::::o r:::::r                  y:::::y         
S:::::::::::::::SS     tt:::::::::::tt oo:::::::::::oo  r:::::r                 y:::::y          
 SSSSSSSSSSSSSSS         ttttttttttt     ooooooooooo    rrrrrrr                y:::::y           
                                                                              y:::::y            
                                                                             y:::::y             
                                                                            y:::::y              
                                                                           y::::
             
[/bold magenta]
"""
    console.print(banner)
    time.sleep(3)
    clear_terminal()
    game_loop()
