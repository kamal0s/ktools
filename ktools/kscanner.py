import sys,socket,time
W = '\033[0m'  # white (normal)
R = '\033[31m'  # red
G = '\033[32m'  # green
O = '\033[33m'  # orange
B = '\033[34m'  # blue
P = '\033[35m'  # purple
C = '\033[36m'  # cyan
GR = '\033[37m'  # gray

def Scanner():
  try:

   host = input(B+"[+] "+W+"Input the target Host : ")
   while True:
    try:
     x = int(input(B+"[+] "+W+"Input the Start Port : "))
     y = int(input(B+"[+] "+W+"Input the End Port : "))
    except:
        print(R+"[-]"+W+"Input Must Be from 1 to 9999")
        continue
    for port in range(x,y):

      s = socket.socket()
      s.settimeout(1)
      try:
         s.connect((host,port))
         print (P+"[*] "+W+"The Port " +str(port)+ " is "+G+"open ! ")
      except socket.error :
         print ("",end="")
      finally:
          pass
    break
  except KeyboardInterrupt:
        pass
  except:
        print(R+"[-] "+W+"Error Check the HOST")