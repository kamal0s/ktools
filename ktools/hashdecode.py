import hashlib
W = '\033[0m'  # white (normal)
R = '\033[31m'  # red
G = '\033[32m'  # green
O = '\033[33m'  # orange
B = '\033[34m'  # blue
P = '\033[35m'  # purple
C = '\033[36m'  # cyan
GR = '\033[37m'  # gray

def HashEnc():
 try:
    h = str(input(P+"[+] "+W+"Input Hash : "))
    while h == '':
        print(R+"[-] "+"Hash is Incorrect Try Again ")
        h = str(input(B+"[+]"+W+"Input Hash : "))
        continue
    d = True
    while d == True:
     try:
      wl = input(B+"[+]"+W+" Please Add Wordlists : ")
      f = open(wl,'r')
      passwo = f.read().split()
      f.close()
      passwordss = (passwo)
      d = False
     except:
        print(R+"[-] "+W+"No Wordlist is Found !")
        continue



    def passdump(passo,typ):
        hashd = hashlib.new(typ)
        hashd.update(passo.encode())
        x = hashd.hexdigest()
        return x


    u = True
    while u == True:
     types = str(input(B+"[+] "+W+"Please Input The Type of Encoding : "))
     for passwords in passwordss:

        try:
             pa = passdump(passwords,types)
             u = False
        except:

            continue
        if pa == h:
                print("\n\t\t\t"+P+"[*]"+W+"The Password is Found : " +G+ passwords+W)
                break
        else:
               continue

    if pa != h :
        print("\n\t\t\t"+R+"[-] "+W+"Password Not Found , Try Another Wordlist !")
 except KeyboardInterrupt:
     pass
 except:
     pass





