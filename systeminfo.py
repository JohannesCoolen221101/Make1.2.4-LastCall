#!/usr/bin/env python
"""
info about project here
"""

import os
import time



...

__author__ = "Johannes Coolen"
__email__ = "johannes.coolen@student.kdg.be"
__status__ = "development"


def main():
    unumber = os.getuid()
    pnumber = os.getpid()
    where = os.getcwd()
    what = os.uname()
    used = os.times()
    now = time.time()
    means = time.ctime(now)

    print("User number", unumber)
    print("Process ID", pnumber)
    print("Current Directory", where)
    print("System information", what)
    print("System information", used)


if __name__ == '__main__':  # code to execute if called from command-line
    main()
