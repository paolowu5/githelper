# config.py
from colorama import Fore, Style

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

# Constants
DEFAULT_BRANCH = "main"
DEFAULT_COMMIT_MESSAGE = "Update"