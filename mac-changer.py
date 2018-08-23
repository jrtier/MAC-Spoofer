# ----Script by Adevtc----

import sys
import os
import time
import subprocess
import random


os.system('clear')
print("")
print("")
print("")
print("")
def slowprint(s):
    for c in s + '\n' :
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(10. / 150)
slowprint("[] Loading : []")
time.sleep(0.5)
slowprint("[] 'Sp0fd' by Adevtc []")
time.sleep(1.8)
slowprint("")
slowprint("")
slowprint("")
slowprint("")
slowprint("")
slowprint("")

slowprint("")
slowprint("")
slowprint("")
slowprint("")
slowprint("")
slowprint("")


os.system('clear')


print('''\033[1;36m

    __  __   _   ___    ___ _                           
    |  \/  | /_\ / __|  / __| |_  __ _ _ _  __ _ ___ _ _ 
    | |\/| |/ _ \ (__  | (__| ' \/ _` | ' \/ _` / -_) '_|
    |_|  |_/_/ \_\___|  \___|_||_\__,_|_||_\__, \___|_|  
                                           |___/                                                                                                                                           
        
''')


print("\033[0;37mType the number shown before the specific string to gain access to its contents")
print("\033[0;31m")
os.system("echo Current MAC-Address: ")
print("\033[0;37m")
os.system("ifconfig en0 | awk '/ether/{print $2}'")

print("")
print("")
print("\033[0;32m 1 \033[0;37m-- \033[0;94mRandom-Generated MAC-ADDRESS ")
print("")
print("\033[0;32m 2 \033[0;37m-- \033[0;94mCustom MAC-ADDRESS ")
print("")
print("\033[0;32m 3 \033[0;37m-- \033[0;94mReset to original MAC-ADDRESS ")

print("")
print("")

in_file = open("mac.txt", "w+")
os.system("ifconfig en0 | awk '/ether/{print $2}' >> mac.txt")
read = in_file.read()
in_file.close()
        
customChoice=input("\033[92m[?] \033[96mChoice --> \033[0;37m")
if customChoice==('1') :
    print("")
    time.sleep(0.05)
    print("")
    time.sleep(0.05)
    print("")
    time.sleep(0.05)
    print("")
    time.sleep(0.05)
    print("")
    time.sleep(0.05)
    print("")
    time.sleep(0.05)
    print("")
    time.sleep(0.05)
    print("")
    time.sleep(0.05)
    print("")
    time.sleep(0.05)
    print("")
    time.sleep(0.05)
    print("")
    time.sleep(0.05)
    print("")
    time.sleep(0.05)
    

    os.system("clear")
    print("\033[0;37m ")
    os.system("echo Current MAC-Address logged")
    slowprint("Importing OS...")
    time.sleep(0.5)
    slowprint("Generating 16-digit hexadecimal...")
    time.sleep(0.2)
    print("Loaded")
    time.sleep(0.5)
    print("Do you want to continue? ( y / n )")
    time.sleep(0.5)
    startNewMac=input("[     ]: ")
    time.sleep(1)
    print("")
    print("")
    os.system("echo Running procedure...")
    

        
    if startNewMac==('y') :
        os.system("sudo ifconfig en0 up")
        def slowprint(s):
            for c in s + '\n' :
                sys.stdout.write(c)
                sys.stdout.flush()
                time.sleep(10. / 250)

        os.system("sudo ifconfig en0 ether " + "02:00:00:%02x:%02x:%02x" % (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
        os.system("sudo ifconfig en0 down")
        slowprint("MAC-Address spoofed")
        print("Running safety procedure")
        os.system("networksetup -setairportpower en0 off")
        slowprint("WiFi disabled for MAC-Address non-logging purposes")
        time.sleep(0.2)
        os.system("networksetup -setairportpower en0 on")
        slowprint("WiFi re-enabled")
        time.sleep(0.2)
        print("Your new randomly-generated MAC-Address")
        print("")
        os.system("ifconfig en0 | awk '/ether/{print $2}'")
        
    if startNewMac==('n') :
        os.system("clear")
        os.system("killall Terminal")



        
if customChoice==('2') :
    print("")
    time.sleep(0.05)
    print("")
    time.sleep(0.05)
    print("")
    time.sleep(0.05)
    print("")
    time.sleep(0.05)
    print("")
    time.sleep(0.05)
    print("")
    time.sleep(0.05)
    print("")
    time.sleep(0.05)
    print("")
    time.sleep(0.05)
    print("")
    time.sleep(0.05)
    print("")
    time.sleep(0.05)
    print("")
    time.sleep(0.05)
    print("")
    time.sleep(0.05)

    os.system("clear")
    print("")
    print("")
    os.system("echo Current MAC-Address logged")
    os.system("echo Enter your MAC-Address: ")

    try:
        userinput=(input(""))
        def slowprint(s):
                for c in s + '\n' :
                    sys.stdout.write(c)
                    sys.stdout.flush()
                    time.sleep(10. / 250)
                    
        os.system("echo Running procedure")
        os.system("sudo ifconfig en0 up")
        os.system("sudo ifconfig en0 ether " + userinput)
        os.system("sudo ifconfig en0 down")
        slowprint("MAC-Address spoofed")
        print("Running safety procedure")
        os.system("networksetup -setairportpower en0 off")
        slowprint("WiFi disabled for MAC-Address non-logging purposes")
        time.sleep(0.2)
        os.system("networksetup -setairportpower en0 on")
        slowprint("WiFi re-enabled")
        time.sleep(0.2)
        print("Your new custom MAC-Address")
        print("")
        os.system("ifconfig en0 | awk '/ether/{print $2}'")
    except ValueError:
        print("Not a valued MAC-Address")

if customChoice==('3') :
    print("")
    time.sleep(0.05)
    print("")
    time.sleep(0.05)
    print("")
    time.sleep(0.05)
    print("")
    time.sleep(0.05)
    print("")
    time.sleep(0.05)
    print("")
    time.sleep(0.05)
    print("")
    time.sleep(0.05)
    print("")
    time.sleep(0.05)
    print("")
    time.sleep(0.05)
    print("")
    time.sleep(0.05)
    print("")
    time.sleep(0.05)
    print("")
    time.sleep(0.05)
    
    def slowprint(s):
        for c in s + '\n' :
            sys.stdout.write(c)
            sys.stdout.flush()
            time.sleep(10. / 250)
                    
    os.system("clear")

    print("")
    print("")
    print("Resetting MAC-Address")
    time.sleep(0.2)
    print("Gathering data from mac.txt")
    time.sleep(0.4)
    in_file = open("mac.txt")
    read = in_file.read()
    os.system("sudo ifconfig en0 up")
    os.system("sudo ifconfig en0 ether " + read)
    os.system("sudo ifconfig en0 down")
    slowprint("MAC-Address spoofed")
    print("Running safety procedure")
    time.sleep(0.2)
    os.system("networksetup -setairportpower en0 off")
    slowprint("WiFi disabled for MAC-Address non-logging purposes")
    time.sleep(0.2)
    os.system("networksetup -setairportpower en0 on")
    slowprint("WiFi re-enabled")
    time.sleep(0.2)
    print("Your old MAC-Address")
    print("")
    os.system("ifconfig en0 | awk '/ether/{print $2}'")
    os.system("rm mac.txt")



    
    
    
 
