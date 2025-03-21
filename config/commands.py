import os
import time
from config.utils import clear_screen, show_banner, RetroColors

def git_status():
    clear_screen()
    show_banner()
    print(RetroColors.HEADER + "\n[+] Current git repository status:")
    os.system("git status")
    input(RetroColors.INFO + "\n[i] Press Enter to return to main menu...")

def git_log():
    clear_screen()
    show_banner()
    print(RetroColors.HEADER + "\n[+] Commit history:")
    num_commits = input(RetroColors.PROMPT + "How many commits to display? (default: 30): ") or "30"
    os.system(f"git log --oneline -n {num_commits}")
    input(RetroColors.INFO + "\n[i] Press Enter to return to main menu...")

def git_init():
    clear_screen()
    show_banner()
    if input(RetroColors.PROMPT + "Confirm initialization? (y/n): ").lower() == "y":
        os.system("git init && git branch -M main")
        print(RetroColors.SUCCESS + "\n[✓] Repository initialized with 'main' branch!")
    input(RetroColors.INFO + "\n[i] Press Enter to return to main menu...")

def git_add_remote():
    clear_screen()
    show_banner()
    os.system("git remote -v")
    username = input(RetroColors.PROMPT + "GitHub username: ")
    repo_name = input(RetroColors.PROMPT + "Repository name: ")
    os.system(f"git remote add origin https://github.com/{username}/{repo_name}.git")
    input(RetroColors.INFO + "\n[i] Press Enter to return to main menu...")

def git_create_branch():
    clear_screen()
    show_banner()
    os.system("git branch")
    choice = input(RetroColors.PROMPT + "Create (c) / Switch (s) / Cancel (Enter): ").lower()
    
    if choice == "c":
        branch = input(RetroColors.PROMPT + "New branch name: ").strip()
        if branch:
            os.system(f"git checkout -b {branch}")
            print(RetroColors.SUCCESS + f"\n[✓] Switched to new branch '{branch}'")
    elif choice == "s":
        branch = input(RetroColors.PROMPT + "Branch name: ").strip()
        os.system(f"git checkout {branch}")
    input(RetroColors.INFO + "\n[i] Press Enter to return to main menu...")

def git_add_all():
    clear_screen()
    show_banner()
    os.system("git add .")
    print(RetroColors.SUCCESS + "\n[✓] Files added!")
    input(RetroColors.INFO + "\n[i] Press Enter to return to main menu...")

def git_commit():
    clear_screen()
    show_banner()
    message = input(RetroColors.PROMPT + "Commit message: ") or "Update"
    os.system(f'git commit -m "{message}"')
    input(RetroColors.INFO + "\n[i] Press Enter to return to main menu...")

def git_push():
    clear_screen()
    show_banner()
    branch = input(RetroColors.PROMPT + "Branch to push (default: main): ").strip() or "main"
    os.system(f"git fetch origin {branch} && git rebase origin/{branch} && git push origin {branch}")
    input(RetroColors.INFO + "\n[i] Press Enter to return to main menu...")

def quick_update():
    clear_screen()
    show_banner()
    os.system("git add .")
    message = input(RetroColors.PROMPT + "Commit message: ") or "Update"
    os.system(f'git commit -m "{message}"')
    branch = input(RetroColors.PROMPT + "Branch to push (default: main): ").strip() or "main"
    os.system(f"git push origin {branch}")
    input(RetroColors.INFO + "\n[i] Press Enter to return to main menu...")
