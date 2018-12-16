#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from string import ascii_letters

def ui_input() -> str:
    """This function takes user string"""
    return input('Your string: ')

def encrypt(string: str) -> str:
    """This function encrypts user string using the algorythm: the letter replaced by the following letter"""
    result = str()
    for code in string:
        if code == 'z': result += 'a'
        elif code == 'Z': result += 'A'
        elif code in ascii_letters:
            result = result + (ascii_letters[(ascii_letters.index(code) + 1) % len(ascii_letters)])
        else:
            result += code
    return result

def ui_output(string: str) -> None:
    """This function prints the result string"""
    print('Result string = ', string)

ui_output(encrypt(ui_input()))


