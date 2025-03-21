import os
import colorama
from colorama import Fore, Style

colorama.init(autoreset=True)

class RetroColors:
    TITLE = Fore.YELLOW + Style.BRIGHT
    HEADER = Fore.CYAN + Style.BRIGHT
    SUCCESS = Fore.GREEN + Style.BRIGHT
    WARNING = Fore.RED + Style.BRIGHT
    INFO = Fore.BLUE + Style.BRIGHT
    SECTION = Fore.CYAN + Style.BRIGHT
    PROMPT = Fore.YELLOW
    MENU_ITEM = Fore.GREEN
    BORDER = Fore.YELLOW + Style.BRIGHT

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def show_banner():
    print(RetroColors.TITLE + "\nGIT MANAGER\n")
