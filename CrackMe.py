import hashlib
import time
import colorama
from colorama import Fore, Style

colorama.init()

def animate_loading():
    chars = "/—\|"
    duration = 3  # Duration in seconds
    end_time = time.time() + duration
    while time.time() < end_time:
        for char in chars:
            print(f"\r{Fore.YELLOW}Loading {char}{Style.RESET_ALL}", end="")
            time.sleep(0.1)

def crack_passwords():
    print(f"\n{Fore.GREEN}[+] Password cracking started...{Style.RESET_ALL}")
    # Implement password cracking logic here
    time.sleep(2)
    print(f"{Fore.GREEN}[+] Password cracking completed{Style.RESET_ALL}")

def crack_ssh():
    print(f"\n{Fore.GREEN}[+] SSH password cracking started...{Style.RESET_ALL}")
    # Implement SSH password cracking logic here
    time.sleep(2)
    print(f"{Fore.GREEN}[+] SSH password cracking completed{Style.RESET_ALL}")

def crack_ftp():
    print(f"\n{Fore.GREEN}[+] FTP password cracking started...{Style.RESET_ALL}")
    # Implement FTP password cracking logic here
    time.sleep(2)
    print(f"{Fore.GREEN}[+] FTP password cracking completed{Style.RESET_ALL}")

def crack_hashes():
    print(f"\n{Fore.GREEN}[+] Hash cracking started...{Style.RESET_ALL}")

    # Get the hash to crack from the user
    hash_to_crack = input("Enter the hash to crack: ").strip()
    # Get the hash algorithm to use from the user
    hash_algorithm = input("Enter the hash algorithm (e.g., md5, sha1): ").lower()

    # Check if the hash algorithm is supported
    if hash_algorithm not in hashlib.algorithms_available:
        print(f"{Fore.RED}[-] Hash algorithm '{hash_algorithm}' is not supported.{Style.RESET_ALL}")
        return

    # Get the path to the wordlist file from the user
    wordlist_path = input("Enter the path to the wordlist file: ")

    # Flag to indicate if a match has been found
    match_found = False

    # Attempt to crack the hash using the wordlist
    with open(wordlist_path, 'r', encoding='utf-8', errors='ignore') as f:
        for word in f:
            # Remove newline characters and whitespace
            word = word.strip()
            # Hash the word using the specified algorithm
            hashed_word = hashlib.new(hash_algorithm, word.encode()).hexdigest()
            # Compare the hashed word with the provided hash
            if hashed_word.strip() == hash_to_crack:
                print(f"\n{Fore.GREEN}[+] Match found! Password: {word}{Style.RESET_ALL}")
                match_found = True
                break  # Stop the search when a match is found

    if not match_found:
        print(f"\n{Fore.RED}[-] Match not found in wordlist.{Style.RESET_ALL}")

    print(f"{Fore.GREEN}[+] Hash cracking completed{Style.RESET_ALL}")

def main():
    print(f"{Fore.MAGENTA}╔══════════════════════════╗")
    print("║  Glitch Scheme Signature  ║")
    print("║  ██████╗░░█████╗░███╗░░░███╗██╗░░██╗  ║")
    print("║  ██╔══██╗██╔══██╗████╗░████║██║░██╔╝  ║")
    print("║  ██║░░██║██║░░██║██╔████╔██║█████═╝░  ║")
    print("║  ██║░░██║██║░░██║██║╚██╔╝██║██╔═██╗░  ║")
    print("║  ██████╔╝╚█████╔╝██║░╚═╝░██║██║░╚██╗  ║")
    print("║  ╚═════╝░░╚════╝░╚═╝░░░░░╚═╝╚═╝░░╚═╝  ║")
    print("║       Made by: Cyb0rgBytes       ║")
    print("╚══════════════════════════╝{Style.RESET_ALL}")

    while True:
        print("\nChoose an option:")
        print("1. Crack passwords")
        print("2. Crack SSH")
        print("3. Crack FTP")
        print("4. Crack hashes")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            animate_loading()
            crack_passwords()
        elif choice == "2":
            animate_loading()
            crack_ssh()
        elif choice == "3":
            animate_loading()
            crack_ftp()
        elif choice == "4":
            animate_loading()
            crack_hashes()
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
