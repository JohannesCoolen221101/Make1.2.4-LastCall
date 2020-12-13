#!/usr/bin/env python
"""
info about project here
"""

import rekenmachine3
import randompassword
import systeminfo
import ipscanner
import openfirefox
import os
import subprocess
from gpiozero.pins.pigpio import PiGPIOFactory

#


__author__ = "Johannes Coolen"
__email__ = "johannes.coolenstudent.kdg.be"
__status__ = "development"


def main():
    ip = PiGPIOFactory(host='192.168.0.196')
    print("maak uw keuze: 1)rekenmachine \n 2)randomwachtwoord \n 3)ipconfig \n 4)updatepi.sh \n 5)installpi.sh ")
    print("6)systeminfo \n 7)ipscanner \n 8)open firefox \n 9) pinstatus")
    keuze = input("")

    if keuze == "1":
        rekenmachine3.main()
    elif keuze == "2":
        randompassword.main()
    elif keuze == "3":
        print(Subprocess.call[('ifconfig')])        #open op de rpi de terminal en geef ifconfig in
    elif keuze == "4":
        subprocess.Popen('updatepi.sh')             #runt het bestand updatepi.sh
    elif keuze == "5":
        subprocess.popen('installpi.sh')
    elif keuze == "6":
        systeminfo.main()
    elif keuze == "7":
        ipscanner.main()
    elif keuze == "8":
        openfirefox.main()
    elif keuze == "9":
        print(Subprocess.call[('pinout')])


if __name__ == '__main__':  # code to execute if called from command-line
    main()
