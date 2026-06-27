#!/usr/bin/env python3

def compare_passwords(target_password, password_file):
    try:
        with open(password_file, "r", encoding="utf-8", errors="ignore") as file:
            for count, line in enumerate(file, start=1):
                password = line.strip()

                if password == target_password:
                    print(f"[+] Password found: {password}")
                    print(f"[+] Found at line: {count}")
                    return

        print("[-] Password not found in the list.")

    except FileNotFoundError:
        print("[-] Password list file not found.")
    except Exception as e:
        print(f"Error: {e}")


def main():
    target_password = input("Enter the password to search for: ")
    password_file = input("Enter the path to the password list: ")

    compare_passwords(target_password, password_file)


if __name__ == "__main__":
    main()
