#!/usr/bin/env python
"""
info about project here
"""
import random
import string


__author__ = "Johannes Coolen"
__email__ = "johannes.coolen@student.kdg.be"
__status__ = "development"


def genereerwachtwoord(lengte, tekens):
    wachtwoord = ""
    if tekens:
        password_characters = string.ascii_letters + string.digits + string.punctuation     # verzamel alle toegelaten karakters in een string
        for i in range(lengte):
            wachtwoord += random.choice(password_characters)                                # kies een willekeurige karakter uit de string
        return wachtwoord
    else:
        password_characters = string.ascii_letters + string.digits
        for i in range(lengte):
            wachtwoord += random.choice(password_characters)
        return wachtwoord


def main():
    try:
        lengte = int(input("hoe lang is het wachtwoord"))

        moeilijkheid = input("ook speciale tekens? (y/n)")
        if moeilijkheid == "y":
            tekens = True
        elif moeilijkheid == "n":
            tekens = False
        else:
            raise Exception("ik vroeg y of n")
        print(genereerwachtwoord(lengte, tekens))
    except Exception as e:
        print(e)
        main()


if __name__ == '__main__':  # code to execute if called from command-line
    main()
