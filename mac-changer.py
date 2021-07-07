# ----Script by Adevtc----
# ----Forked by mattraimondi-----

import sys
import os
import random

class ColorEscapeSequences:
    lightgrey = "\033[0;37m"
    red = "\033[0;31m"
    green = "\033[92m"
    blue = "\033[0;94m"
    turquoise = "\033[96m"

os.system('clear')
print(f'''{ColorEscapeSequences.turquoise}

     __  __   _   ___    ___ _
    |  \/  | /_\ / __|  / __| |_  __ _ _ _  __ _ ___ _ _
    | |\/| |/ _ \ (__  | (__| ' \/ _` | ' \/ _` / -_) '_|
    |_|  |_/_/ \_\___|  \___|_||_\__,_|_||_\__, \___|_|
                                           |___/

''')
print(f"{ColorEscapeSequences.lightgrey}Type the number shown before the specific string to gain access to its contents{ColorEscapeSequences.red}\n\nCurrent MAC-Address:{ColorEscapeSequences.lightgrey}\n")
os.system("ifconfig en0 | awk '/ether/{print $2}'")
print(f"\n\n{ColorEscapeSequences.green} 1 {ColorEscapeSequences.lightgrey}-- {ColorEscapeSequences.blue}Random-Generated MAC-ADDRESS\n\n{ColorEscapeSequences.green} 2 {ColorEscapeSequences.lightgrey}-- {ColorEscapeSequences.blue}Custom MAC-ADDRESS \n\n{ColorEscapeSequences.green} 3 {ColorEscapeSequences.lightgrey}-- {ColorEscapeSequences.blue}Reset to original MAC-ADDRESS\n\n")

doesMacExist = os.popen("ls").read()
if "mac.txt" not in doesMacExist:
    os.system("ifconfig en0 | awk '/ether/{print $2}' >> mac.txt")

customChoice=input(f"{ColorEscapeSequences.green}[?] {ColorEscapeSequences.turquoise}Choice --> {ColorEscapeSequences.lightgrey}")

if customChoice == '1':
    os.system("clear")
    print(f"{ColorEscapeSequences.lightgrey}Current MAC-Address logged\nImporting OS...\nGenerating 16-digit hexadecimal...\nLoaded\nDo you want to continue? ( y / n )")
    startNewMac=input("[     ]: ")
    print("\n\nRunning procedure...")
    if startNewMac == 'y':
        os.system("sudo ifconfig en0 up; sudo ifconfig en0 ether 02:00:00:%02x:%02x:%02x; sudo ifconfig en0 down; networksetup -setairportpower en0 off; networksetup -setairportpower en0 on" % (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
        print(f"Your new randomly-generated MAC-Address\n")
        os.system("ifconfig en0 | awk '/ether/{print $2}'")

    if startNewMac == 'n':
        os.system("clear")

if customChoice == '2':
    os.system("clear")
    print("\n\nCurrent MAC-Address logged\nEnter your MAC-Address: ")

    try:
        userinput=(input(""))
        print("Running procedure")
        os.system(f"sudo ifconfig en0 up; sudo ifconfig en0 ether {userinput}; sudo ifconfig en0 down; networksetup -setairportpower en0 off; networksetup -setairportpower en0 on")
        print(f"Your new custom MAC-Address\n")
        os.system("ifconfig en0 | awk '/ether/{print $2}'")
    except ValueError:
        print("Not a valid MAC-Address")

if customChoice == '3':
    os.system("clear")
    print("\n\nResetting MAC-Address\nGathering data from mac.txt")
    with open("mac.txt", "r+") as in_file:
        read = in_file.read()
    os.system(f"sudo ifconfig en0 up; sudo ifconfig en0 ether {read}; sudo ifconfig en0 down; networksetup -setairportpower en0 off; networksetup -setairportpower en0 on")
    print(f"Your old MAC-Address\n")
    os.system("ifconfig en0 | awk '/ether/{print $2}'; rm mac.txt")
