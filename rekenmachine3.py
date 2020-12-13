#!/usr/bin/env python
"""
info about project here
"""


__author__ = "Johannes Coolen"
__email__ = "johannes.coolen@student.kdg.be"
__status__ = "development"


def plus(x, y):
    try:
        print(x + y)
    except Exception as e:
        print(e)
        main()


def min(x, y):
    try:
        print(x - y)
    except Exception as e:
        print(e)
        main()


def maal(x, y):
    try:
        print(x * y)
    except Exception as e:
        print(e)
        main()


def delen(x, y):
    try:
        print(x / y)
    except Exception as e:
        print(e)
        main()


def main():
    try:
        getal1 = int(input("geef een natuurlijk getal"))
        getal2 = int(input("nu nog een alstublieft"))
        operator = input("wil je optellen(+) aftrekken(-) delen(/) of vermenigvuldigen(*)")
        if operator == '+':
            plus(getal1, getal2)

        elif operator == '-':
            min(getal1, getal2)

        elif operator == '*':
            maal(getal1, getal2)

        elif operator == '/':
            delen(getal1, getal2)
        else:
            raise Exception("ik vroeg +,-,*,/, aub")
            main()
    except Exception as e:
        print(e)
        main()


if __name__ == '__main__':  # code to execute if called from command-line
    main()
