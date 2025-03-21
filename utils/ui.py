# ui.py
import os
import colorama
from utils.config import RetroColors

# Initialize colorama
colorama.init(autoreset=True)

def clear_screen():
    """Clears the screen based on operating system."""
    os.system('cls' if os.name == 'nt' else 'clear')

def show_banner():
    """Displays the application banner with Amstrad CPC inspired styling."""
    print(RetroColors.TITLE + """
╔════════════════════════════════════════╗
║             GIT MANAGER                ║
║                                        ║
╚════════════════════════════════════════╝
    """)

def display_menu():
    """Displays the main menu options."""
    border = RetroColors.BORDER + "═" * 40
    print(border)
    print(RetroColors.SECTION + "          COMMAND MENU")
    print(border)
    
    print(RetroColors.SECTION + "\n[INFO]")
    print(RetroColors.MENU_ITEM + "1. Repository status (git status)")
    print(RetroColors.MENU_ITEM + "2. View commit history (git log)")
    
    print(RetroColors.SECTION + "\n[SETUP]")
    print(RetroColors.MENU_ITEM + "3. Initialize repository (git init)")
    print(RetroColors.MENU_ITEM + "4. Manage remote origin (git remote)")
    print(RetroColors.MENU_ITEM + "5. Manage branches (git branch)")
    
    print(RetroColors.SECTION + "\n[UPDATE]")
    print(RetroColors.MENU_ITEM + "6. Add all files (git add .)")
    print(RetroColors.MENU_ITEM + "7. Create commit (git commit)")
    print(RetroColors.MENU_ITEM + "8. Push code (git push)")
    print(RetroColors.MENU_ITEM + "9. Quick update (add, commit, push)")
    
    print(border)
    print(RetroColors.MENU_ITEM + "0. Exit")
    print(border)