#!/usr/bin/python3
# This code write by (ms.nope)
from colorama import Fore,init
import subprocess
import socket
import requests
import os
import time
init()

class color:
     line = '\033[4m'
     End = '\033[0m'
     darkblue = '\033[34m'
     green = '\033[92m'
     red = '\033[91m'
choose1 = color.green + "\nwebinfo/> " + color.End
web = color.green + "\nEnter ip: " + color.End
Error = color.red + "Error webinfo!" + color.End
quit = color.green + "Exiting packge!... " + color.End
time.sleep(1)
os.system("clear")
print(color.line + """
                                      mm                                   mmmm          
     *@@@@*     @     *@@@*          m@@             *@@@@*              m@* **          
       *@@     m@@     m@             @@               @@                @@*             
        @@m   m@@@m   m@     mm@*@@   @@m@@@@m         @@  *@@@@@@@@m   @@@@@    m@@*@@m 
         @@m  @* @@m  @*    m@*   @@  @@    *@@        @@    @@    @@    @@     @@*   *@@
         !@@ @*  *@@ @*     !@******  !@     @@        @!    @!    @@    !@     @@     @@
          !@@m    !@@m      !@m    m  !!!   m@!        @!    @!    !@    !@     @@     !@
          !!@!*   !!@!*     !!******  !!     !!        !!    !!    !!    !:     !@     !!
          !!!!    !!!!      :!!       :!!   !!!        :!    !!    !!    !:     !!!   !!!
           :       :         : : ::   : : : ::       :!: : : :::  :!: :: :::     : : : : 
                                                                                    
                                                                                   """ + color.End + color.red + """
                               (🅦🅔🅑 🅘🅝🅕🅞) """ + color.darkblue + """
                     ---[ This code write by Ms.nope ]--- """ + color.red + """
                     ----[  https://github.com/msprogrammer2938/  ]------ """ + color.End)
print("{1}.start webinfo")
print("{2}.Exit")
choose = str(input(choose1))
if(str(choose) == '1'):
  time.sleep(1)
  os.system("clear")
  print(color.green)
  os.system("figlet webinfo")
  print(color.End)
  ip = str(input(web))
  time.sleep(2)
  os.system("clear")
  os.system("cowsay -f ghostbusters Hacking " + ip)
  print(color.red + "------------------------------------------------------------------------------------------------------" + color.End)
  os.system("whois " + ip)
  print(color.red + "------------------------------------------------------------------------------------------------------" + color.End)
  time.sleep(2)
  try1 = str(input("press Enter... "))
  if(str(try1) == ''):
    os.system("python3 webinfo.py")
  else:
      os.system("python3 webinfo.py")
elif(str(choose) == ""):
    os.system("python3 webinfo.py")
elif(str(choose) == " "):
    os.system("python3 webinfo.py")
elif(str(choose) == "  "):
    os.system("python3 webinfo.py")
elif(str(choose) == '2'):
    time.sleep(1)
    os.system("clear")
    time.sleep(1)
    print(quit)
    time.sleep(2)
    exit(1)
else:
    time.sleep(1)
    os.system("clear")
    print(Error)
    time.sleep(2)
    try2 = str(input("press Enter... "))
    if(str(try2) == ''):
      os.system("python3 webinfo.py")
    else:
        os.system("python3 webinfo.py")
