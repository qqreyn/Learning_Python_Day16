from colorama import init, Fore, Back, Style
from dateutil import parser
from datetime import datetime

init(autoreset=True)

def print_header():
    print(Back.BLUE + Fore.WHITE + "=== COLORFUL CONSOLE APP ===")
    print()

def get_user_date():
    user_input = input(Fore.CYAN + "Enter a date (example: 2026-03-10 or March 10 2026): ")
    
    try:
        parsed_date = parser.parse(user_input)
        return parsed_date
    except Exception as e:
        print(Fore.RED + "Invalid date format!")
        return None

def display_date_info(date_obj):
    print()
    print(Fore.GREEN + "Parsed Date Information:")
    print(Fore.YELLOW + f"Full datetime: {date_obj}")
    print(Fore.MAGENTA + f"Formatted (DD/MM/YYYY): {date_obj.strftime('%d/%m/%Y')}")
    print(Fore.CYAN + f"Day of week: {date_obj.strftime('%A')}")

    days_left = (date_obj - datetime.now()).days
    print(Fore.WHITE + f"Days from today: {days_left}")

def main():
    print_header()
    
    date_obj = get_user_date()
    
    if date_obj:
        display_date_info(date_obj)
    else:
        print(Fore.RED + "Exiting program due to error.")

if __name__ == "__main__":
    main()