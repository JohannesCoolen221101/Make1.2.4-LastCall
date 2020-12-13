#!/usr/bin/env python
"""
info about project here
"""

import webbrowser



...

__author__ = "Johannes Coolen"
__email__ = "johannes.coolen@student.kdg.be"
__status__ = "development"


def main():
    url = 'duckduckgo.com/'
    webbrowser.register('firefox', None,
                        webbrowser.BackgroundBrowser("C://Program Files//Mozilla Firefox//firefox.exe"))
    webbrowser.get('firefox').open(url)


if __name__ == '__main__':  # code to execute if called from command-line
    main()
