import hashlib
import random

W = '\033[0m'  # white (normal)
R = '\033[31m'  # red
G = '\033[32m'  # green
O = '\033[33m'  # orange
B = '\033[34m'  # blue
P = '\033[35m'  # purple
C = '\033[36m'  # cyan
GR = '\033[37m'  # gray


def RanHash():
 try:
    has = input("[+] Please Input your Hash : ")
    ran = input("[+] Please Input the character you think the Password it content : ")
    v = True
    while v == True:
     types = input("[+] Please Input Encode Type : ")
     for i in range(1,10**len(ran)):

         r = ''.join(random.choice(ran) for i in range(len(ran)))
         try:
          d = hashlib.new(types)
          v = False
         except:
          continue
         d.update(r.encode())
         f = d.hexdigest()

         print(O+"[-] "+W+r+ "\t" +f)
  
         if f == has:
          print("\n"+P+"[*] "+G+r+ "\t" +f)
          break
    if f != has:
       print("\n"+R+"[-] "+W+"The Password not in this character, Try Another !")
 except KeyboardInterrupt:
     pass