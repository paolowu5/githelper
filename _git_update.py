import os
import time
import datetime


print("""

        __________                   _________      _____      
_______ ___(_)_  /_   ____  _______________  /_____ __  /_____ 
__  __ `/_  /_  __/   _  / / /__  __ \  __  /_  __ `/  __/  _ |
_  /_/ /_  / / /_     / /_/ /__  /_/ / /_/ / / /_/ // /_ /  __/
_\__, / /_/  \__/     \__,_/ _  .___/\__,_/  \__,_/ \__/ \___/ 
/____/                       /_/                               

""")

def create_backup():
    """Crea un backup dell'ultima versione su GitHub."""
    backup_dir = "work/backup"
    os.makedirs(backup_dir, exist_ok=True)
    
    # Ottiene l'ultimo messaggio di commit
    last_commit_msg = os.popen("git log -1 --pretty=%B").read().strip().replace(" ", "_")
    
    # Nome della cartella con commento commit e data
    timestamp = datetime.datetime.now().strftime("%d-%m-%Y_%H-%M-%S")
    backup_folder = os.path.join(backup_dir, f"{last_commit_msg}_{timestamp}")
    os.makedirs(backup_folder, exist_ok=True)
    
    print("Clonazione dell'ultima versione da GitHub...")
    remote_url = os.popen("git config --get remote.origin.url").read().strip()
    
    if remote_url:
        os.system(f"git clone --depth 1 {remote_url} {backup_folder}")
        print(f"Backup creato in: {backup_folder}")
    else:
        print("Errore: Nessun repository remoto trovato.")

def git_update():
    """Esegue l'update del repository con opzione di backup."""
    repo_name = os.popen("git rev-parse --show-toplevel").read().strip().split(os.sep)[-1]
    print(f"Commit for: {repo_name}\n")
    
    choice = input("Do you need to backup files first? (y/n): ")
    if choice.lower() == 'y':
        create_backup()
    
    os.system("git add .")
    time.sleep(1)
    
    update_name = input("Name commit: ")
    commit_command = f'git commit -m "{update_name}"'
    print(f"{commit_command}")
    os.system(commit_command)
    
    choice = input("\nCommit on main branch? (y/n): ")
    if choice.lower() == 'y':
        print("Pushing on main branch...")
        os.system("git push origin main")
    else:
        print("Operazione terminata senza push.")
    
    input("\nPress any key to continue...")
    exit()

if __name__ == "__main__":
    git_update()
