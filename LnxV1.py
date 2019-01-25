#!/usr/local/bin/python
# code by 3xploit
# LNX.CREW
# https://www.lnx-crew.zone.id



import os

def menu():

  print(""" 
  	| |   |_ _| \ | | | | \ \/ /   |_ _| \ | / ___|_   _|/ \  | |   | ____|  _ \ 
        | |    | ||  \| | | | |\  /     | ||  \| \___ \ | | / _ \ | |   |  _| | |_) |
        | |___ | || |\  | |_| |/  \     | || |\  |___) || |/ ___ \| |___| |___|  _ < 
        |_____|___|_| \_|\___//_/\_\___|___|_| \_|____/ |_/_/   \_\_____|_____|_| \_\
                                                                                 ver:1.0              
[+] Coded By 3xploit
[+] Developer blackarch[+]https://blackarch.org/tools.html
[+] My_Team LNX.CREW
========================================
1. THC-Hydra install
2. Metasploit install
3. Nethunter install
4. Ubuntu install
5. Fedora install
6. Beef-Xss install
7. Nmap install
8. Xerosploit install
-----------------------------------------
0. Exit
==========================================
""")

loop = True

while loop:
    menu()
    lnxcrew = input("#: ")
    if lnxcrew == "1":
        os.system("cd /data/data/com.termux/files/home")
        os.system("pkg update -y")
        os.system("pkg install -y hydra")
        os.system("cd /data/data/com.termux/files/home")
        print("====================================")
        print("[+] THC-Hydra success install")
        print("====================================")
        rmenu = input("[?] Back to Menu? (y/n): ")
        if rmenu == "y":
            menu()
        else:
            break
    elif lnxcrew == "2":
        os.system("pkg install -y wget")
        os.system("cd /data/data/com.termux/files/home && wget https://Auxilus.github.io/metasploit.sh")
        os.system("cd /data/data/com.termux/files/home && bash metasploit.sh")
        os.system("cd /data/data/com.termux/files/home && cd metasploit-framework")
        os.system("cd /data/data/com.termux/files/home && gem install bundle --pre")
        os.system("cd /data/data/com.termux/files/home && bundle config build.nokogiri --use-system-libraries")
        os.system("cd /data/data/com.termux/files/home/metasploit-framework && bundle install")
        os.system("cd /data/data/com.termux/files/home/metasploit-framework && bundle update nokogiri")
        os.system("cd /data/data/com.termux/files/home/")
        print("====================================")
        print("[+] Metasploit success install")
        print("====================================")
        rmenu = input("[?] Back to Menu? (y/n): ")
        if rmenu == "y":
            menu()
        else:
            break
    elif lnxcrew == "3":
        os.system("pkg update -y")
        os.system("cd /data/data/com.termux/files/home && git clone https://github.com/Hax4us/Nethunter-In-Termux.git")
        os.system("cd /data/data/com.termux/files/home && cd Nethunter-In-Termux && chmod +x kalinethunter")
        os.system("cd /data/data/com.termux/files/home")
        print("====================================")
        print("[+] Nethunter success install")
        print("====================================")
        rmenu = input("[?] Back to Menu? (y/n): ")
        if rmenu == "y":
            menu()
        else:
            break
    elif lnxcrew == "4":
        os.system("pkg update -y")
        os.system("pkg install -y git")
        os.system("cd /data/data/com.termux/files/home && git clone https://github.com/Neo-Oli/termux-ubuntu.git")
        os.system("cd /data/data/com.termux/files/home && cd termux-ubuntu && bash ubuntu.sh")
        print("====================================")
        print("[+] Ubuntu success install")
        print("====================================")
        rmenu = input("[?] Back to Menu? (y/n): ")
        if rmenu == "y":
            menu()
        else:
            break
    elif lnxcrew == "5":
        os.system("pkg update -y")
        os.system("pkg install -y git")
        os.system("pkg install -y wget")
        os.system("apt update && apt install wget -y && /data/data/com.termux/files/usr/bin/wget https://raw.githubusercontent.com/nmilosev/termux-fedora/master/termux-fedora.sh")
        print("====================================")
        print("[+] Fedora success install")
        print("====================================")
        rmenu = input("[?] Back to Menu? (y/n): ")
        if rmenu == "y":
            menu()
        else:
            break
    elif lnxcrew == "6":
        os.system("cd /data/data/com.termux/files/home")
        os.system("pkg update -y")
        os.system("pkg install nano")
        os.system("pkg install python -y")
        os.system("pkg install python2 -y")
        os.system("pkg install cat -y")
        os.system('mkdir -p $PREFIX/etc/apt/sources.list.d && printf "deb [trusted=yes] https://hax4us.github.io/termux-tools/ extras main" > $PREFIX/etc/apt/sources.list.d/hax4us.list')
        os.system("pkg update")
        os.system("pkg install beef-xss")
        os.system("cd /data/data/com.termux/files/home")
        print("=============================")
        print("[+] Beef-Xss success install")
        print("=============================")
        rmenu = input("[?] Back to Menu? (y/n): ")
        if rmenu == "y":
            menu()
        else:
            break
    elif lnxcrew == "7":
        os.system("cd /data/data/com.termux/files/home")
        os.system("pkg update -y")
        os.system("pkg install -y nmap")
        os.system("cd /data/data/com.termux/files/home")
        print("===========================")
        print("[+] Nmap success install")
        print("===========================")
        rmenu = input("[?] Back to Menu? (y/n): ")
        if rmenu == "y":
            menu()
        else:
            break
    elif lnxcrew == "8":
        os.system("cd /data/data/com.termux/files/home")
        os.system("pkg updaye -y")
        os.system('mkdir -p $PREFIX/etc/apt/sources.list.d && printf "deb [trusted=yes] https://hax4us.github.io/termux-tools/ extras main" > $PREFIX/etc/apt/sources.list.d/hax4us.list')
        os.system("pkg update")
        os.system("cd /data/data/com.termux/files/home")
        os.system("pkg install xerosploit")
        print("==========================")
        print("[+] Xerosploit success install")
        print("==========================")
        rmenu == input("[?] Back to Menu? (y/n): ")
        if rmenu == "y":
            menu()
        else:
            break
    elif lnxcrew == "0":
        print("THANKS Bro!!..")
        break
