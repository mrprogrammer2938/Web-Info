#!/usr/bin/bash
# This code write by (Mr.nope)
clear
echo "installing... "
sleep 1
echo ""
echo ""
echo "      ████████████████████████████████████████████████"
echo "      █▄─█▀▀▀█─▄█▄─▄▄─█▄─▄─▀███▄─▄█▄─▀█▄─▄█▄─▄▄─█─▄▄─█"
echo "      ██─█─█─█─███─▄█▀██─▄─▀████─███─█▄▀─███─▄███─██─█"
echo "      ▀▀▄▄▄▀▄▄▄▀▀▄▄▄▄▄▀▄▄▄▄▀▀▀▀▄▄▄▀▄▄▄▀▀▄▄▀▄▄▄▀▀▀▄▄▄▄▀"
echo "                    (🅦🅔🅑 🅘🅝🅕🅞)"
echo ""
sudo apt install python3
sudo apt install whois
sudo apt install python
sudo apt install pip3
sudo apt install pip
pip install requirements.txt
chmod +x webinfo.py
echo ""
echo "fnish!"
echo ""
echo "usage: ./webinfo.py"
echo ""
exit 1
