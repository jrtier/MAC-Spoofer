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
time.sleep(3)
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
os.system("ifconfig en0 |grep ether")

print("")
print("")
print("\033[0;32m 1 \033[0;37m-- \033[0;94mRandom-Generated MAC-ADDRESS ")
print("")
print("\033[0;32m 2 \033[0;37m-- \033[0;94mCustom MAC-ADDRESS ")
print("")
print("\033[0;32m 3 \033[0;37m-- \033[0;94mReset to original MAC-ADDRESS ")
print("")
print("")

customChoice=input("\033[92m[?] \033[96mChoice -->")
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
    slowprint("importing resources.")
    time.sleep(0.2)
    slowprint("generating random hexadecimal -- 16 digits")
    time.sleep(0.5)
    print("loaded")
    time.sleep(1)
    print("Randomly generated MAC-Address function loaded.")
    time.sleep(1)
    print("Do you want to continue? ( y / n )")
    time.sleep(1)
    startNewMac=input("[     ]: ")
    time.sleep(1)

    in_file = open("mac.txt", "w+")
    os.system("ifconfig en0 | awk '/ether/{print $2}' >> mac.txt")
    read = in_file.read()
    in_file.close()
        
    if startNewMac==('y') :
        os.system("sudo ifconfig en0 up")
        def slowprint(s):
            for c in s + '\n' :
                sys.stdout.write(c)
                sys.stdout.flush()
                time.sleep(10. / 250)

        os.system("sudo ifconfig en0 ether " + "02:00:00:%02x:%02x:%02x" % (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
        os.system("sudo ifconfig en0 down")
        slowprint("MAC-Address changed")
        print("Running safety procedure")
        os.system("networksetup -setairportpower en0 off")
        slowprint("WiFi disabled for MAC-Address non-logging purposes")
        time.sleep(0.2)
        os.system("networksetup -setairportpower en0 on")
        slowprint("WiFi re-enabled")
        time.sleep(0.2)
        print("Your new randomly-generated MAC-Address")
        print("")
        os.system("ifconfig en0 |grep ether")
        
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
   
    os.system("echo Enter your MAC-Address: ")

    try:
        userinput=(input(""))
        def slowprint(s):
                for c in s + '\n' :
                    sys.stdout.write(c)
                    sys.stdout.flush()
                    time.sleep(10. / 250)

        os.system("sudo ifconfig en0 up")
        os.system("sudo ifconfig en0 ether " + userinput)
        os.system("sudo ifconfig en0 down")
        slowprint("MAC-Address changed")
        print("Running safety procedure")
        os.system("networksetup -setairportpower en0 off")
        slowprint("WiFi disabled for MAC-Address non-logging purposes")
        time.sleep(0.2)
        os.system("networksetup -setairportpower en0 on")
        slowprint("WiFi re-enabled")
        time.sleep(0.2)
        print("Your new custom MAC-Address")
        print("")
        os.system("ifconfig en0 |grep ether")



    except ValueError: #In the works
        print("Not a valid MAC-Address")
        os.system("exit")


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

    os.system("clear")

    print("Resetting MAC-Address")
    print("MAC-Address Reset")
    print("")
   

    in_file = open("mac.txt")
    read = in_file.read()
    os.system("sudo ifconfig en0 up")
    os.system("sudo ifconfig en0 ether " + read)
    os.system("sudo ifconfig en0 down")
    slowprint("MAC-Address changed")
    print("Running safety procedure")
    os.system("networksetup -setairportpower en0 off")
    slowprint("WiFi disabled for MAC-Address non-logging purposes")
    time.sleep(0.2)
    os.system("networksetup -setairportpower en0 on")
    slowprint("WiFi re-enabled")
    time.sleep(0.2)
    print("Your new custom MAC-Address")
    print("")
    os.system("ifconfig en0 |grep ether")
    os.system("rm mac.txt")



    
    
    
 
