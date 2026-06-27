#!/usr/bin/env python3

import argparse

def compare_passwords(target_password, password_file):
    try:
        with open(password_file, "r", encoding="utf-8", errors="ignore") as file:
            for count, line in enumerate(file, start=1):
                password = line.strip()

                if password == target_password:
                    print(f"[+] Password found: {password}")
                    print(f"[+] Found at line: {count}")
                    return

        print("[-] Password not found.")

    except FileNotFoundError:
        print("[-] Password list not found.")

parser = argparse.ArgumentParser(
    description="Password List Comparator"
)

parser.add_argument(
    "-p", "--password",
    required=True,
    help="Password to search for"
)

parser.add_argument(
    "-l", "--list",
    required=True,
    help="Path to the password list"
)

args = parser.parse_args()

compare_passwords(args.password, args.list)
