#!/usr/bin/env python3
import os
import time
import sys
import colorama
from colorama import Fore, Back, Style

# Initialize colorama
colorama.init(autoreset=True)

# Color themes - Retrowave style
class RetroColors:
    TITLE = Fore.YELLOW + Style.BRIGHT
    HEADER = Fore.CYAN + Style.BRIGHT
    HIGHLIGHT = Fore.WHITE + Style.BRIGHT
    SUCCESS = Fore.GREEN + Style.BRIGHT
    WARNING = Fore.RED + Style.BRIGHT
    INFO = Fore.BLUE + Style.BRIGHT
    PROMPT = Fore.YELLOW
    SECTION = Fore.CYAN + Style.BRIGHT
    MENU_ITEM = Fore.GREEN
    BORDER = Fore.YELLOW + Style.BRIGHT

def clear_screen():
    """Clears the screen based on operating system"""
    os.system('cls' if os.name == 'nt' else 'clear')

def show_banner():
    """Displays the application banner with Amstrad CPC inspired styling"""
    print(RetroColors.TITLE + """
╔════════════════════════════════════════╗
║             GIT MANAGER                ║
║                                        ║
╚════════════════════════════════════════╝
    """)

# [INFO] FUNCTIONS
def git_status():
    """Shows the current repository status"""
    clear_screen()
    show_banner()
    print(RetroColors.HEADER + "\n[+] Current git repository status:")
    os.system("git status")
    print(RetroColors.INFO + "\n[i] Press Enter to return to main menu...")
    input()

def git_log():
    """Shows commit history"""
    clear_screen()
    show_banner()
    print(RetroColors.HEADER + "\n[+] Commit history:")
    
    # Ask how many commits to display
    num_commits = input(RetroColors.PROMPT + "How many commits to display? (leave empty for all): ")
    
    try:
        if num_commits:
            num = int(num_commits)
            # Using os.popen to capture output and handle pagination
            log_output = os.popen(f"git log --oneline -n {num}").read()
        else:
            # Limit to 30 by default to avoid excessive output
            log_output = os.popen("git log --oneline -n 30").read()
            
        # Display the output
        print("\n" + log_output)
        
        # If there are more logs than what was displayed
        if not num_commits:
            print(RetroColors.INFO + "\n[i] Showing last 30 commits. Use a number to see more.")
    except Exception as e:
        print(RetroColors.WARNING + f"\n[!] Error retrieving logs: {e}")
    
    print(RetroColors.INFO + "\n[i] Press Enter to return to main menu...")
    input()

# [SETUP] FUNCTIONS
def git_init():
    """Initializes a new Git repository and sets the default branch to main"""
    clear_screen()
    show_banner()
    print(RetroColors.HEADER + "\n[+] Initializing a new Git repository")
    
    choice = input(RetroColors.PROMPT + "Confirm initialization of a new repository? (y/n): ")
    if choice.lower() == 'y':
        os.system("git init")
        
        # Rename branch to main
        os.system("git branch -M main")
        print(RetroColors.SUCCESS + "\n[✓] Repository initialized with 'main' as the default branch!")
        
        # Ask to add files and make first commit
        add_files = input(RetroColors.PROMPT + "\nAdd all files and make first commit? (y/n): ")
        if add_files.lower() == 'y':
            os.system("git add .")
            commit_msg = input(RetroColors.PROMPT + "Message for first commit (default: Initial commit): ")
            if not commit_msg:
                commit_msg = "Initial commit"
            
            os.system(f'git commit -m "{commit_msg}"')
            print(RetroColors.SUCCESS + f"\n[✓] First commit created with message: '{commit_msg}'")
    
    else:
        print(RetroColors.WARNING + "\n[!] Initialization cancelled.")
    
    time.sleep(1)
    print(RetroColors.INFO + "\n[i] Press Enter to return to main menu...")
    input()

def git_add_remote():
    """Adds a remote origin"""
    clear_screen()
    show_banner()
    print(RetroColors.HEADER + "\n[+] Add remote origin")
    
    # First check if origin already exists
    os.system("git remote -v")
    
    choice = input(RetroColors.PROMPT + "\nRemove any existing origins? (y/n): ")
    if choice.lower() == 'y':
        os.system("git remote remove origin")
        print(RetroColors.SUCCESS + "[✓] Existing origins removed.")
    elif choice.lower() == 'n':
        print(RetroColors.INFO + "\n[i] Keeping existing origins.")
        print(RetroColors.INFO + "\n[i] Press Enter to return to main menu...")
        input()
        return
    
    username = input(RetroColors.PROMPT + "\nEnter your GitHub username: ")
    repo_name = input(RetroColors.PROMPT + "Enter repository name: ")
    
    remote_url = f"https://github.com/{username}/{repo_name}.git"
    os.system(f'git remote add origin {remote_url}')
    print(RetroColors.SUCCESS + f"\n[✓] Origin added: {remote_url}")
    time.sleep(1)
    
    # Verify
    print(RetroColors.HEADER + "\n[+] Verify origin:")
    os.system("git remote -v")
    print(RetroColors.INFO + "\n[i] Press Enter to return to main menu...")
    input()

def git_create_branch():
    """Creates or changes branch"""
    clear_screen()
    show_banner()
    print(RetroColors.HEADER + "\n[+] Branch management")
    
    # Show existing branches
    print(RetroColors.HEADER + "\nCurrent branches:")
    os.system("git branch")
    
    choice = input(RetroColors.PROMPT + "\nCreate new branch (c), switch branch (s), or press Enter to cancel: ").strip().lower()
    
    if choice == "c":
        branch_name = input(RetroColors.PROMPT + "Enter new branch name: ").strip()
        if branch_name:
            os.system(f"git branch {branch_name}")
            os.system(f"git checkout {branch_name}")
            print(RetroColors.SUCCESS + f"\n[✓] Branch '{branch_name}' created and switched to it!")
        else:
            print(RetroColors.WARNING + "\n[!] Branch creation cancelled (no name provided).")

    elif choice == "s":
        branch_name = input(RetroColors.PROMPT + "Enter branch name to switch to: ").strip()
        if branch_name:
            os.system(f"git checkout {branch_name}")
            print(RetroColors.SUCCESS + f"\n[✓] Switched to branch '{branch_name}'!")
        else:
            print(RetroColors.WARNING + "\n[!] Switch cancelled (no branch name provided).")

    else:
        print(RetroColors.INFO + "\n[i] No action taken. Returning to the main menu...")

    time.sleep(1)
    print(RetroColors.INFO + "\n[i] Press Enter to return to main menu...")
    input()

# [UPDATE] FUNCTIONS
def git_add_all():
    """Adds all files to commit"""
    clear_screen()
    show_banner()
    print(RetroColors.HEADER + "\n[+] Adding all files to commit...")
    os.system("git add .")
    print(RetroColors.SUCCESS + "\n[✓] Operation completed!")
    time.sleep(1)
    print(RetroColors.INFO + "\n[i] Press Enter to return to main menu...")
    input()

def git_commit():
    """Creates a commit with a message"""
    clear_screen()
    show_banner()
    print(RetroColors.HEADER + "\n[+] Creating a new commit")
    
    commit_message = input(RetroColors.PROMPT + "Enter commit message: ")
    if not commit_message:
        commit_message = "Update"
    
    os.system(f'git commit -m "{commit_message}"')
    print(RetroColors.SUCCESS + f"\n[✓] Commit created with message: '{commit_message}'")
    time.sleep(1)
    print(RetroColors.INFO + "\n[i] Press Enter to return to main menu...")
    input()

def git_push():
    """Pushes code to remote"""
    clear_screen()
    show_banner()
    print(RetroColors.HEADER + "\n[+] Push code to remote")
    
    # Show current branches
    print(RetroColors.HEADER + "\nCurrent branches:")
    os.system("git branch")
    
    branch_name = input(RetroColors.PROMPT + "\nEnter branch name to push (default: main): ")
    if not branch_name:
        branch_name = "main"
    
    choice = input(RetroColors.PROMPT + f"Confirm push to '{branch_name}'? (y/n): ")
    if choice.lower() == 'y':
        print(RetroColors.HEADER + f"\n[+] Pushing to branch '{branch_name}'...")
        os.system(f"git push -u origin {branch_name}")
        print(RetroColors.SUCCESS + "\n[✓] Push completed!")
    else:
        print(RetroColors.WARNING + "\n[!] Push cancelled.")
    
    time.sleep(1)
    print(RetroColors.INFO + "\n[i] Press Enter to return to main menu...")
    input()

def quick_update():
    """Performs complete update process: add, commit and push"""
    clear_screen()
    show_banner()
    print(RetroColors.HEADER + "\n[+] Quick update (add, commit, push)")
    
    # Add
    print(RetroColors.HEADER + "\n[+] Adding all files...")
    os.system("git add .")
    
    # Commit
    update_name = input(RetroColors.PROMPT + "\nCommit name: ")
    if not update_name:
        update_name = "Update"
    
    commit_command = f'git commit -m "{update_name}"'
    print(RetroColors.HEADER + f"\n[+] Executing: {commit_command}")
    os.system(commit_command)
    
    # Push
    branch_name = input(RetroColors.PROMPT + "\nBranch to push to (default: main): ")
    if not branch_name:
        branch_name = "main"
    
    choice = input(RetroColors.PROMPT + f"\nConfirm push to '{branch_name}'? (y/n): ")
    if choice.lower() == 'y':
        print(RetroColors.HEADER + f"\n[+] Pushing to branch '{branch_name}'...")
        os.system(f"git push origin {branch_name}")
        print(RetroColors.SUCCESS + "\n[✓] Push completed!")
    else:
        print(RetroColors.WARNING + "\n[!] Push cancelled.")
    
    time.sleep(1)
    print(RetroColors.INFO + "\n[i] Press Enter to return to main menu...")
    input()

def main_menu():
    """Main menu"""
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
        
        if choice == '1':
            git_status()
        elif choice == '2':
            git_log()
        elif choice == '3':
            git_init()
        elif choice == '4':
            git_add_remote()
        elif choice == '5':
            git_create_branch()
        elif choice == '6':
            git_add_all()
        elif choice == '7':
            git_commit()
        elif choice == '8':
            git_push()
        elif choice == '9':
            quick_update()
        elif choice == '0':
            clear_screen()
            print(RetroColors.TITLE + "Thank you for using Git Helper! Goodbye.")
            sys.exit(0)
        else:
            print(RetroColors.WARNING + "\n[!] Invalid option. Please try again.")
            time.sleep(1)

if __name__ == "__main__":
    main_menu()