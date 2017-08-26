#!/usr/bin/env python
# -*- coding: utf-8 -*-
#   _____   _             _   _      _____             __      __    __            ___
#  / ____| | |           | | | |    |  __ \            \ \    / /   /_ |          / _ \
# | (___   | |_    __ _  | | | | __ | |__) |  _   _     \ \  / /     | |         | | | |
#  \___ \  | __|  / _` | | | | |/ / |  ___/  | | | |     \ \/ /      | |         | | | |
#  ____) | | |_  | (_| | | | |   <  | |      | |_| |      \  /       | |    _    | |_| |
# |_____/   \__|  \__,_| |_| |_|\_\ |_|       \__, |       \/        |_|   (_)    \___/
#                                              __/ |
#                                             |___/
#-----------------------------------------------------------------------------
# @Author: Vaibhav Singh
# @Date: 2017-08-27
# @Email: vaibhav.singh.14cse@bml.edu.in
# @Github username: vaibhavsingh97
# @Website: https://vaibhavsingh97.me
# @Last Modified by: Vaibhav Singh
# @Last Modified Date: 2017-08-27
# @License: MIT License
# you can find your copy of the License
# https://vaibhavsingh97.mit-license.org/
#-----------------------------------------------------------------------------
import sys
import json
import requests
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from clint.textui import colored, puts


def head():
    """official banner for StalkPy printed in green color"""
    clear()
    stalkPyBanner = """
           _____   _             _   _      _____
          / ____| | |           | | | |    |  __ \\
         | (___   | |_    __ _  | | | | __ | |__) |  _   _
          \___ \  | __|  / _` | | | | |/ / |  ___/  | | | |
          ____) | | |_  | (_| | | | |   <  | |      | |_| |
         |_____/   \__|  \__,_| |_| |_|\_\ |_|       \__, |
                                                      __/ |
                                                     |___/

                                    - Vaibhav Singh (@ vaibhavsingh97)
                                    - Version 1.0
    """
    puts(colored.green(stalkPyBanner))


def clear():
    """for removing the clutter from the screen when necessary"""
    os.system('cls' if os.name == 'nt' else 'clear')


def space():
    """ for adding one linespace in the console"""
    print("")


def notification(flag):
    if flag == 1:
        puts(colored.red("Error: wrong value entered! Please enter correct value."))
        space()
        flag = 0
    elif flag == 2:
        puts(colored.green("Success: Social account found. :)"))
        flag = 0
    elif flag == 3:
        puts(colored.red("No Social accounts found. :("))
        flag = 0


def showDoc():
    documentation = """
    A simple python script to open the major social accounts connected to the
    specfic handle. Inspired from [HandleStalker](https://github.com/samanthakem/HandleStalker)

    - Simple to use: Built with love so it's easy to use.
    - single command will query any number of usernames
    - Text Highlighting is cross platform - Supports Linux, MAC, Windows for the terminal based highlighting.
    """
    puts(colored.cyan(documentation))
    space()


def CleanedLink(url, username):
    return "https://www." + url + username


class StalkPy():
    """docstring for ."""

    def __init__(self):
        with open('config.json') as data_file:
            self.data = json.loads(data_file.read())

    def OpenLinks(self, user):
        for social_account_name in self.data:
            r = requests.get(CleanedLink(self.data[social_account_name], user))
            if r.status_code == 200:
                notification(2)
                driver = webdriver.Firefox()
                driver.get(CleanedLink(self.data[social_account_name], user))
                puts(colored.green(social_account_name + ": ") +
                     colored.blue(CleanedLink(self.data[social_account_name], user)))
            r.close()


if __name__ == '__main__':
    head()
    showDoc()
    if (len(sys.argv) < 2):
        print("usage: \n python StalkPy.py <username1> <username2> ... <usernameN>")
        puts(colored.red("Exiting..."))
    else:
        for i in range(1, len(sys.argv)):
            space()
            puts(colored.magenta("User: %s" % sys.argv[i]))
            StalkPy().OpenLinks(sys.argv[i])
