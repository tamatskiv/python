#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def ui_input() -> str:
    """This function takes user string"""
    return input('Your string: ')

def make_frame(string: str) -> str:
    """"This function makes frame for user string"""
    frame = "*" * (len(string) + 4)
    result = frame + "\n* " + string + " *\n" + frame
    return result

def ui_output(result: str) -> None:
    """This function prints the result"""
    print(result)

ui_output(make_frame(ui_input()))


