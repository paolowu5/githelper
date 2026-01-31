#!/usr/bin/env python3
import os
import time
import sys
import shutil
import subprocess
import colorama
from colorama import Fore, Back, Style

colorama.init(autoreset=True)

class RetroColors:
    TITLE = Fore.YELLOW + Style.BRIGHT
    HEADER = Fore.CYAN + Style.BRIGHT
    SUCCESS = Fore.GREEN + Style.BRIGHT
    WARNING = Fore.RED + Style.BRIGHT
    INFO = Fore.BLUE + Style.BRIGHT
    PROMPT = Fore.YELLOW
    SECTION = Fore.CYAN + Style.BRIGHT
    MENU_ITEM = Fore.GREEN
    BORDER = Fore.YELLOW + Style.BRIGHT

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def show_banner():
    print(RetroColors.TITLE + """
╔════════════════════════════════════════╗
║             GITHELPER                  ║
║                                        ║
╚════════════════════════════════════════╝
    """)

def print_border():
    return RetroColors.BORDER + "═" * 40

def run_git_command(command, silent=False):
    """Execute a Git command and return the result."""
    result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    if not silent and result.returncode != 0:
        print(RetroColors.WARNING + f"\n[!] Error: {result.stderr.strip()}")
    return result

def ensure_git_repository():
    if not os.path.exists(".git"):
        print(RetroColors.WARNING + "\n[!] No Git repository detected.")
        if input(RetroColors.PROMPT + "Initialize repository now? (y/n): ").lower() == 'y':
            run_git_command("git init")
            run_git_command("git branch -M main")
            print(RetroColors.SUCCESS + "\n[✓] Repository initialized.")
            return True
        else:
            print(RetroColors.INFO + "\n[i] Operation cancelled.")
            return False
    return True


def git_status():
    clear_screen()
    show_banner()

    if not ensure_git_repository():
        input(RetroColors.INFO + "\n[i] Press Enter to return...")
        return

    print(RetroColors.HEADER + "\n[+] Repository Status")
    os.system("git status")
    input(RetroColors.INFO + "\n[i] Press Enter to return...")

def git_log():
    clear_screen()
    show_banner()

    if not ensure_git_repository():
        input(RetroColors.INFO + "\n[i] Press Enter to return...")
        return

    print(RetroColors.HEADER + "\n[+] Commit History")
    num = input(RetroColors.PROMPT + "Number of commits to display (default: 30): ")
    cmd = f"git log --oneline -n {num}" if num else "git log --oneline -n 30"
    print("\n" + os.popen(cmd).read())
    input(RetroColors.INFO + "\n[i] Press Enter to return...")


def guided_init():
    """
    Guided setup: Initialize repo → initial commit → set remote → summary + optional first push
    """
    clear_screen()
    show_banner()

    print(RetroColors.HEADER + "\n[+] Guided Setup: New Project → Git + GitHub")
    print(RetroColors.WARNING + "This wizard will prepare a brand-new project for Git and GitHub.\n")

    # ────────────────────────────────────────────────
    # 1. Initialize local repository (if not already present)
    # ────────────────────────────────────────────────
    repo_already_exists = os.path.exists(".git")

    if repo_already_exists:
        print(RetroColors.WARNING + "[!] Warning: A Git repository already exists in this folder (.git found).")
        print(RetroColors.WARNING + "     Continuing may overwrite the existing remote origin.")
        response = input(RetroColors.PROMPT + "Continue anyway? (yes/no): ").lower()
        if response not in ['y', 'yes', 's', 'si']:
            print(RetroColors.INFO + "\nOperation cancelled.")
            input(RetroColors.INFO + "\n[i] Press Enter to return to menu...")
            return
    else:
        print(RetroColors.INFO + "[i] Initializing local Git repository...")
        # Modern Git (≥2.28) supports --initial-branch
        run_git_command("git init --initial-branch=main")
        # Fallback for older Git versions (uncomment if needed):
        # run_git_command("git init")
        # run_git_command("git branch -M main")
        print(RetroColors.SUCCESS + "[✓] Repository initialized with main branch")

    # ────────────────────────────────────────────────
    # 2. Create initial commit (only if repo is empty)
    # ────────────────────────────────────────────────
    has_commits = False
    try:
        result = subprocess.run("git rev-parse HEAD", shell=True,
                                stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        has_commits = result.returncode == 0
    except:
        pass

    if not has_commits:
        print(RetroColors.INFO + "\n[i] No commits yet → preparing initial commit")

        print(RetroColors.INFO + "Staging all files (git add .)...")
        run_git_command("git add .")

        default_msg = "Initial project setup"
        msg = input(RetroColors.PROMPT + f"Commit message (default: '{default_msg}'): ").strip() or default_msg

        commit_result = run_git_command(f'git commit -m "{msg}"')
        if commit_result.returncode == 0:
            print(RetroColors.SUCCESS + f"[✓] Initial commit created: '{msg}'")
        else:
            print(RetroColors.WARNING + "[!] Commit failed. Possibly no files were staged?")
            print(RetroColors.INFO + "   You can add files manually and try again later.")
    else:
        print(RetroColors.INFO + "[i] Repository already has commits → skipping initial commit")

    # ────────────────────────────────────────────────
    # 3. Configure remote origin
    # ────────────────────────────────────────────────
    print("\n" + print_border())
    print(RetroColors.HEADER + "       GITHUB REMOTE CONFIGURATION")
    print(print_border())

    print(RetroColors.INFO + "Current remotes:")
    os.system("git remote -v")

    response = input(RetroColors.PROMPT + "\nConfigure / update 'origin' remote? (yes/no): ").lower()
    if response in ['y', 'yes', 's', 'si']:

        # Remove existing origin silently (no error if it doesn't exist)
        run_git_command("git remote remove origin", silent=True)

        username = input(RetroColors.PROMPT + "Your GitHub username: ").strip()
        repo_name = input(RetroColors.PROMPT + "Repository name on GitHub: ").strip()

        if not username or not repo_name:
            print(RetroColors.WARNING + "Username and repository name are required → remote setup cancelled.")
        else:
            url = f"https://github.com/{username}/{repo_name}.git"
            run_git_command(f"git remote add origin {url}")
            print(RetroColors.SUCCESS + f"[✓] Remote 'origin' set to: {url}")

            print("\n" + RetroColors.INFO + "Updated remotes:")
            os.system("git remote -v")

    # ────────────────────────────────────────────────
    # 4. Summary + offer first push
    # ────────────────────────────────────────────────
    print("\n" + print_border())
    print(RetroColors.HEADER + "             SETUP COMPLETED")
    print(print_border())

    print(RetroColors.SUCCESS + "  • Local repository initialized")
    if not has_commits:
        print(RetroColors.SUCCESS + "  • Initial commit created")
    print(RetroColors.SUCCESS + "  • Main branch set")
    if "origin" in subprocess.getoutput("git remote"):
        print(RetroColors.SUCCESS + "  • Remote origin configured")

    print("\n" + RetroColors.INFO + "Recommended next steps:")
    print(RetroColors.MENU_ITEM + "  • Option 8 → Manual push")
    print(RetroColors.MENU_ITEM + "  • Option 9 → Quick Update (add + commit + push)")

    if input(RetroColors.PROMPT + "\nPerform the first push now? (yes/no): ").lower() in ['y', 'yes', 's', 'si']:
        print(RetroColors.INFO + "Running: git push -u origin main")
        push_result = run_git_command("git push -u origin main")
        if push_result.returncode == 0:
            print(RetroColors.SUCCESS + "[✓] First push successful! Project is now live on GitHub.")
        else:
            print(RetroColors.WARNING + "[!] Push failed. Common causes:")
            print("   • Repository does not exist on GitHub yet")
            print("   • You must create an empty repository on github.com first")
            print("   • Authentication issue (try Personal Access Token or SSH)")
            print("   • No commits on main branch")

    input(RetroColors.INFO + "\n[i] Press Enter to return to main menu...")

def git_add_remote():
    clear_screen()
    show_banner()

    if not ensure_git_repository():
        input(RetroColors.INFO + "\n[i] Press Enter to return...")
        return

    print(RetroColors.HEADER + "\n[+] Manage Remote Origin")
    os.system("git remote -v")

    if input(RetroColors.PROMPT + "\nRemove existing origins? (y/n): ").lower() == 'y':
        run_git_command("git remote remove origin")
        print(RetroColors.SUCCESS + "\n[✓] Existing origins removed.")
    else:
        input(RetroColors.INFO + "\n[i] Press Enter to return...")
        return

    username = input(RetroColors.PROMPT + "\nGitHub username: ")
    repo = input(RetroColors.PROMPT + "Repository name: ")
    url = f"https://github.com/{username}/{repo}.git"

    run_git_command(f"git remote add origin {url}")
    print(RetroColors.SUCCESS + f"\n[✓] Origin added: {url}")
    os.system("git remote -v")
    input(RetroColors.INFO + "\n[i] Press Enter to return...")

def git_create_branch():
    clear_screen()
    show_banner()

    if not ensure_git_repository():
        input(RetroColors.INFO + "\n[i] Press Enter to return...")
        return

    print(RetroColors.HEADER + "\n[+] Branch Management")
    os.system("git branch")

    choice = input(RetroColors.PROMPT + "\nCreate new branch (c), switch branch (s), or Enter to cancel: ").lower()

    if choice == "c":
        branch = input(RetroColors.PROMPT + "Branch name: ").strip()
        if branch:
            run_git_command(f"git branch {branch}")
            run_git_command(f"git checkout {branch}")
            print(RetroColors.SUCCESS + f"\n[✓] Branch '{branch}' created and checked out.")

    elif choice == "s":
        branch = input(RetroColors.PROMPT + "Branch name: ").strip()
        if branch:
            run_git_command(f"git checkout {branch}")
            print(RetroColors.SUCCESS + f"\n[✓] Switched to branch '{branch}'.")

    input(RetroColors.INFO + "\n[i] Press Enter to return...")

def git_reset():
    clear_screen()
    show_banner()
    print(RetroColors.HEADER + "\n[+] Reset Local Repository")
    if not os.path.exists(".git"):
        print(RetroColors.WARNING + "\n[!] No Git repository found.")
        input(RetroColors.INFO + "\n[i] Press Enter to return...")
        return
    print(RetroColors.WARNING + "\n[!] Warning: This will delete the local .git directory.")
    if input(RetroColors.PROMPT + "Confirm deletion? (y/n): ").lower() == 'y':
        try:
            shutil.rmtree(".git")
            print(RetroColors.SUCCESS + "\n[✓] Local repository deleted.")
        except PermissionError as e:
            print(RetroColors.WARNING + f"\n[!] Permission error: {e}")
            if os.name == 'nt':
                os.system("rmdir /s /q .git")
                if not os.path.exists(".git"):
                    print(RetroColors.SUCCESS + "\n[✓] Deleted using alternative command.")
                else:
                    print(RetroColors.WARNING + "\n[!] Deletion failed. Remove '.git' manually.")
    time.sleep(1)
    input(RetroColors.INFO + "\n[i] Press Enter to return...")

def git_add_all():
    clear_screen()
    show_banner()

    if not ensure_git_repository():
        input(RetroColors.INFO + "\n[i] Press Enter to return...")
        return

    print(RetroColors.HEADER + "\n[+] Stage All Files")
    run_git_command("git add .")
    print(RetroColors.SUCCESS + "\n[✓] All files staged.")
    input(RetroColors.INFO + "\n[i] Press Enter to return...")

def git_commit():
    clear_screen()
    show_banner()

    if not ensure_git_repository():
        input(RetroColors.INFO + "\n[i] Press Enter to return...")
        return

    print(RetroColors.HEADER + "\n[+] Create Commit")
    msg = input(RetroColors.PROMPT + "Commit message (default: Update): ") or "Update"
    run_git_command(f'git commit -m "{msg}"')
    print(RetroColors.SUCCESS + f"\n[✓] Commit created: '{msg}'")
    input(RetroColors.INFO + "\n[i] Press Enter to return...")

def git_push():
    clear_screen()
    show_banner()

    if not ensure_git_repository():
        input(RetroColors.INFO + "\n[i] Press Enter to return...")
        return

    print(RetroColors.HEADER + "\n[+] Push to Remote")
    os.system("git branch")

    branch = input(RetroColors.PROMPT + "\nBranch to push (default: main): ").strip() or "main"

    if input(RetroColors.PROMPT + f"Confirm push to '{branch}'? (y/n): ").lower() != 'y':
        return

    run_git_command(f"git push -u origin {branch}")
    print(RetroColors.SUCCESS + "\n[✓] Push completed.")
    input(RetroColors.INFO + "\n[i] Press Enter to return...")
  
def quick_update():
    clear_screen()
    show_banner()

    if not ensure_git_repository():
        input(RetroColors.INFO + "\n[i] Press Enter to return...")
        return

    run_git_command("git add .")
    msg = input(RetroColors.PROMPT + "\nCommit message (default: Update): ") or "Update"
    run_git_command(f'git commit -m "{msg}"')

    branch = input(RetroColors.PROMPT + "\nBranch (default: main): ") or "main"
    run_git_command(f"git push -u origin {branch}")

    print(RetroColors.SUCCESS + "\n[✓] Update completed.")
    input(RetroColors.INFO + "\n[i] Press Enter to return...")

def main_menu():
    while True:
        clear_screen()
        show_banner()
        border = print_border()
        print(border)
        print(RetroColors.SECTION + "          COMMAND MENU")
        print(border)
        print(RetroColors.SECTION + "\n[STATUS]")
        print(RetroColors.MENU_ITEM + "1. Repository Status")
        print(RetroColors.MENU_ITEM + "2. Commit History")
        print(RetroColors.SECTION + "\n[SETUP]")
        print(RetroColors.MENU_ITEM + "3. Wizard quick setup (init + commit + remote)")
        print(RetroColors.MENU_ITEM + "4. Manage Remote Origin")
        print(RetroColors.MENU_ITEM + "5. Branch Management")
        print(RetroColors.MENU_ITEM + "10. Reset Local Repository")
        print(RetroColors.SECTION + "\n[UPDATE]")
        print(RetroColors.MENU_ITEM + "6. Stage All Files")
        print(RetroColors.MENU_ITEM + "7. Create Commit")
        print(RetroColors.MENU_ITEM + "8. Push to Remote")
        print(RetroColors.MENU_ITEM + "9. Quick Update")
        print(border)
        print(RetroColors.MENU_ITEM + "0. Exit")
        print(border)
        
        choice = input(RetroColors.PROMPT + "\nSelect an option: ")
        if choice == '1': git_status()
        elif choice == '2': git_log()
        elif choice == '3': guided_init()        
        elif choice == '4': git_add_remote()
        elif choice == '5': git_create_branch()
        elif choice == '6': git_add_all()
        elif choice == '7': git_commit()
        elif choice == '8': git_push()
        elif choice == '9': quick_update()
        elif choice == '10': git_reset()
        elif choice == '0':
            clear_screen()
            print(RetroColors.TITLE + "Thank you for using GitHelper!")
            sys.exit(0)
        else:
            print(RetroColors.WARNING + "\n[!] Invalid option.")
            time.sleep(1)

if __name__ == "__main__":
    main_menu()