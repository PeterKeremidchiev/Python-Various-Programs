from colorama import Fore
from pyfiglet import figlet_format

input_string = input()


print(Fore.RED + figlet_format(input_string, font="doh", width = 200) + Fore.RESET)