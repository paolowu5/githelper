# git_commands.py
import subprocess
import time
from utils.ui import clear_screen, show_banner
from utils.config import RetroColors, DEFAULT_BRANCH, DEFAULT_COMMIT_MESSAGE

def git_status():
    """Shows the current repository status."""
    try:
        clear_screen()
        show_banner()
        print(RetroColors.HEADER + "\n[+] Current git repository status:")
        result = subprocess.run(["git", "status"], capture_output=True, text=True, check=True)
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print(RetroColors.WARNING + f"\n[!] Git error: {e.stderr}")
    except FileNotFoundError:
        print(RetroColors.WARNING + "\n[!] Git is not installed or not found.")
    print(RetroColors.INFO + "\n[i] Press Enter to return to main menu...")
    input()

def git_log():
    """Shows commit history."""
    clear_screen()
    show_banner()
    print(RetroColors.HEADER + "\n[+] Commit history:")
    
    num_commits = input(RetroColors.PROMPT + "How many commits to display? (leave empty for 30): ")
    try:
        if num_commits:
            num = int(num_commits)
            result = subprocess.run(["git", "log", "--oneline", "-n", str(num)], 
                                  capture_output=True, text=True, check=True)
        else:
            result = subprocess.run(["git", "log", "--oneline", "-n", "30"], 
                                  capture_output=True, text=True, check=True)
        print("\n" + result.stdout)
        if not num_commits:
            print(RetroColors.INFO + "\n[i] Showing last 30 commits. Use a number to see more.")
    except subprocess.CalledProcessError as e:
        print(RetroColors.WARNING + f"\n[!] Error retrieving logs: {e.stderr}")
    print(RetroColors.INFO + "\n[i] Press Enter to return to main menu...")
    input()

def git_init():
    """Initializes a new Git repository."""
    clear_screen()
    show_banner()
    print(RetroColors.HEADER + "\n[+] Initializing a new Git repository")
    
    choice = input(RetroColors.PROMPT + "Confirm initialization of a new repository? (y/n): ")
    if choice.lower() == 'y':
        try:
            subprocess.run(["git", "init"], capture_output=True, text=True, check=True)
            print(RetroColors.SUCCESS + "\n[✓] Repository initialized!")
            
            add_files = input(RetroColors.PROMPT + "\nAdd all files and make first commit? (y/n): ")
            if add_files.lower() == 'y':
                subprocess.run(["git", "add", "."], check=True)
                commit_msg = input(RetroColors.PROMPT + "Message for first commit (default: Initial commit): ")
                if not commit_msg:
                    commit_msg = "Initial commit"
                subprocess.run(["git", "commit", "-m", commit_msg], check=True)
                print(RetroColors.SUCCESS + f"\n[✓] First commit created with message: '{commit_msg}'")
        except subprocess.CalledProcessError as e:
            print(RetroColors.WARNING + f"\n[!] Error: {e.stderr}")
    else:
        print(RetroColors.WARNING + "\n[!] Initialization cancelled.")
    time.sleep(1)
    print(RetroColors.INFO + "\n[i] Press Enter to return to main menu...")
    input()

def git_add_remote():
    """Adds a remote origin."""
    clear_screen()
    show_banner()
    print(RetroColors.HEADER + "\n[+] Add remote origin")
    
    try:
        result = subprocess.run(["git", "remote", "-v"], capture_output=True, text=True, check=True)
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print(RetroColors.WARNING + f"\n[!] Error: {e.stderr}")
    
    choice = input(RetroColors.PROMPT + "\nRemove any existing origins? (y/n): ")
    if choice.lower() == 'y':
        subprocess.run(["git", "remote", "remove", "origin"], check=True)
        print(RetroColors.SUCCESS + "[✓] Existing origins removed.")
    elif choice.lower() == 'n':
        print(RetroColors.INFO + "\n[i] Keeping existing origins.")
        print(RetroColors.INFO + "\n[i] Press Enter to return to main menu...")
        input()
        return
    
    username = input(RetroColors.PROMPT + "\nEnter your GitHub username: ")
    repo_name = input(RetroColors.PROMPT + "Enter repository name: ")
    remote_url = f"https://github.com/{username}/{repo_name}.git"
    try:
        subprocess.run(["git", "remote", "add", "origin", remote_url], check=True)
        print(RetroColors.SUCCESS + f"\n[✓] Origin added: {remote_url}")
        print(RetroColors.HEADER + "\n[+] Verify origin:")
        result = subprocess.run(["git", "remote", "-v"], capture_output=True, text=True, check=True)
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print(RetroColors.WARNING + f"\n[!] Error: {e.stderr}")
    time.sleep(1)
    print(RetroColors.INFO + "\n[i] Press Enter to return to main menu...")
    input()

# Aggiungi qui le altre funzioni come git_create_branch, git_add_all, git_commit, git_push, quick_update
# con lo stesso approccio basato su subprocess e gestione errori.