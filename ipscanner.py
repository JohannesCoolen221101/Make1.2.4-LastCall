#!/usr/bin/env python
"""
info about project here
"""

import subprocess
...

__author__ = "Johannes Coolen"
__email__ = "johannes.coolen@student.kdg.be"
__status__ = "development"


def main():
    for ping in range(1, 10):
        address = "127.0.0." + str(ping)
        res = subprocess.call(['ping', '-c', '3', address])
        if res == 0:
            print("ping to", address, "OK")
        elif res == 2:
            print("no response from", address)
        else:
            print("ping to", address, "failed!")


if __name__ == '__main__':  # code to execute if called from command-line
    main()
