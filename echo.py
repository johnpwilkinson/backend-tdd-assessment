#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""An enhanced version of the 'echo' cmd line utility."""

__author__ = "John Wilkinson"


import sys
import argparse


def create_parser():
    """Returns an instance of argparse.ArgumentParser"""
    parser = argparse.ArgumentParser(description='echo input from user', epilog="Now you have received ECHO help")
    parser.add_argument('-u', '--upper', action="store_true", help="converts test to upper case")
    parser.add_argument('-l', '--lower', action="store_true", help="converts text to lower case")
    parser.add_argument('-t', '--title', action="store_true", help="converts text to title case")
    parser.add_argument('text', help="this is that the user has inputted" )

    if not sys.argv:
        parser.print_usage()
    return parser

def main(args):
    """Implementation of echo"""
    parser = create_parser()
    ns = parser.parse_args(args)
    if ns.upper:
        print(ns.text.upper())
    elif ns.lower:
        print(ns.text.lower())
    elif ns.title:
        print(ns.text.title())
    else:
        print(ns.text)
    return


if __name__ == '__main__':
    main(sys.argv[1:])
