#!/usr/bin/python3
from ktools.Wpa import WpaAttack
from ktools.hashdecode import HashEnc
import sys
from ktools.kscanner import Scanner
from ktools.ranhash import RanHash

W = '\033[0m'  # white (normal)
R = '\033[31m'  # red
G = '\033[32m'  # green
O = '\033[33m'  # orange
B = '\033[34m'  # blue
P = '\033[35m'  # purple
C = '\033[36m'  # cyan
GR = '\033[37m'  # gray

print(G+"""\t\t\t

                                                                                                                        
      ,-.   ___                          ,--,               
  ,--/ /| ,--.'|_                      ,--.'|               
,--. :/ | |  | :,'    ,---.     ,---.  |  | :               
:  : ' /  :  : ' :   '   ,'\   '   ,'\ :  : '    .--.--.    
|  '  / .;__,'  /   /   /   | /   /   ||  ' |   /  /    '   
'  |  : |  |   |   .   ; ,. :.   ; ,. :'  | |  |  :  /`./   
|  |   \:__,'| :   '   | |: :'   | |: :|  | :  |  :  ;_     
'  : |. \ '  : |__ '   | .; :'   | .; :'  : |__ \  \    `.  
|  | ' \ \|  | '.'||   :    ||   :    ||  | '.'| `----.   \ 
'  : |--' ;  :    ; \   \  /  \   \  / ;  :    ;/  /`--'  / 
;  |,'    |  ,   /   `----'    `----'  |  ,   /'--'.     /  
'--'       ---`-'        """+W+"""by Kamal.S"""+G+"""    ---`-'   `--'---'   
                                                            """)
while True:
 try:

        print("\n\n")
        print("\t" + P + "[1] " + W + "Wireless Attack (WPA - WPA2)")
        print("\n\t" + P + "[2] " + W + "Port Scanning")
        print("\n\t" + P + "[3] " + W + "Hash Decrypt")
        print("\n\t" + P + "[4] " + W + "Exit\n\n")
        choice = int(input(B+"[+] "+W+"Select From (1 to 4) : "))
        if choice == 1:
            WpaAttack()
        elif choice == 2:
            Scanner()
        elif choice == 3:
          while True:
             print("\n\t" + P + "[1] " + W + "Decrypt Using Wordlist ..")
             print("\n\t" + P + "[2] " + W + "Decrypt Using Specific Word\n")
             choose = int(input(B+"[+] "+W+"Select From (1 to 2) : "))
             if choose == 1:
                 HashEnc()
                 break
             elif choose == 2:
                 RanHash()
                 break
             else:
                 print(R+"[-] "+W+"Error Please select choice in the list ")
                 continue

        elif choice == 4:
                 print(R + "[-] " + W + "Good By ")
                 break
        else:
                 print(R+"[-] "+W+"Error Please select choice in the list ")

 except KeyboardInterrupt:
                 print(R + "\n[-] " + W + "Good By ")
                 exit()
 except:
                 continue
