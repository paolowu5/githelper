import sys
import time
from config.utils import clear_screen, show_banner, RetroColors
from config.commands import (
    git_status, git_log, git_init, git_add_remote,
    git_create_branch, git_add_all, git_commit,
    git_push, quick_update
)

def main_menu():
    """Mostra il menu principale e gestisce gli input utente"""
    while True:
        clear_screen()
        show_banner()

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

        choice = input(RetroColors.PROMPT + "\nSelect an option: ")

        commands = {
            "1": git_status,
            "2": git_log,
            "3": git_init,
            "4": git_add_remote,
            "5": git_create_branch,
            "6": git_add_all,
            "7": git_commit,
            "8": git_push,
            "9": quick_update
        }

        if choice in commands:
            commands[choice]()
        elif choice == "0":
            clear_screen()
            print(RetroColors.TITLE + "Thank you for using Git Manager!")
            sys.exit(0)
        else:
            print(RetroColors.WARNING + "\n[!] Invalid option. Please try again.")
            time.sleep(1)
