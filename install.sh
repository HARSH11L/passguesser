#!/bin/bash

echo "[*] Installing PassGuesser..."

chmod +x passguesser.py
sudo cp passguesser.py /usr/local/bin/passguesser

echo "[+] Installation Complete!"
echo
echo "Run it using:"
echo "passguesser -p \"password\" -l \"/path/to/wordlist\""
