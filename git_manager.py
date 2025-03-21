#!/usr/bin/env python3
# git_manager.py
import sys
from utils.ui import clear_screen, show_banner, display_menu
from utils.git_commands import git_status, git_log, git_init, git_add_remote
from utils.config import RetroColors

def main():
    """Main entry point for Git Manager."""
    while True:
        clear_screen()
        show_banner()
        display_menu()
        
        choice = input(RetroColors.PROMPT + "\nSelect an option: ")
        
        if choice == '1':
            git_status()
        elif choice == '2':
            git_log()
        elif choice == '3':
            git_init()
        elif choice == '4':
            git_add_remote()
        elif choice == '5':
            # git_create_branch()
            pass
        elif choice == '6':
            # git_add_all()
            pass
        elif choice == '7':
            # git_commit()
            pass
        elif choice == '8':
            # git_push()
            pass
        elif choice == '9':
            # quick_update()
            pass
        elif choice == '0':
            clear_screen()
            print(RetroColors.TITLE + "Thank you for using Git Manager! Goodbye.")
            sys.exit(0)
        else:
            print(RetroColors.WARNING + "\n[!] Invalid option. Please try again.")
            input(RetroColors.INFO + "\n[i] Press Enter...")

if __name__ == "__main__":
    main()