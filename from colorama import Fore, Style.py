from colorama import Fore, Style, init
import random
import time
import os


init(autoreset=True)

def clear_console():
    # Fonction pour effacer la console selon le système
    os.system('cls' if os.name == 'nt' else 'clear')

def animated_christmas_tree2(height):
    colors = [Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.CYAN, Fore.MAGENTA]
    
    while True:
        clear_console()
        
        # Dessiner le feuillage
        for i in range(height):
            spaces = ' ' * (height - i - 1)
            leaves = ''
            for j in range(2*i + 1):
                leaves += random.choice(colors) + '*'
            print(spaces + leaves)
        
        # Dessiner le tronc
        trunk_width = height // 3
        if trunk_width % 2 == 0:
            trunk_width += 1
        trunk_height = height // 4
        trunk_spaces = ' ' * (height - trunk_width // 2 - 1)
        for _ in range(trunk_height):
            print(trunk_spaces + Fore.YELLOW + '|' * trunk_width)
        
        time.sleep(0.5)  # Met à jour les couleurs toutes les 0.5 secondes

# Exemple d'utilisation
animated_christmas_tree2(10)