from colorama import Fore

def show_directory(path, spaces=""):
    print(f"{spaces}{Fore.BLUE}{path}{Fore.RESET}")

def show_file(path, spaces=""):
    print(f"{spaces}{Fore.GREEN}{path}{Fore.RESET}")

